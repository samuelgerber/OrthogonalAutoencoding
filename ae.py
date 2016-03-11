import tensorflow as tf
import numpy as np


class AutoEncoder(object):

    def __init__(self):
        #dimensionality of layers
        self.dimensions = []
        # + alpha * Ortho constarint
        self.alpha = 0
        # + beta *(gamma - Jacobain Frobenious norm)^2
        self.beta = 0
        self.gamma = 0

        self.tortho = "squared"
    
        self.rate = 0
        self.maxFactor = 1
        self.factor = 1

        self._lrate = 1
        

        

        #Use stochastic batch sizes. If 0 no stoachastic training
        self.stochastic = 0
        #Nosie level for denosiing optimization
        self.sigma = 0
        #use linear decoder
        self.linear = False

        #Encoding vars
        self.W =  []
        self.b =  []

        #Decoding vars
        self.Wt = []
        self.bt = []


    def addDimension( self, dim ):
        self.dimensions.append(dim)
            

    def layerwise( self ):
        self.lxr = []
        self.loptimizer = []
        self.lloss = [] 
        tmpLoss = tf.Variable(tf.constant(0., shape=[1]) )
        l = len(self.Wt)
        for i in range( l) :
            tmp = self.z[i+1] 

            for d in range( i+1 ) :
                index = l - i + d - 1
                if self.linear:
                   tmp = tf.matmul(tmp, self.Wt[index]) + self.bt[index]  
                else:
                   tmp =  tf.nn.tanh( (tf.matmul(tmp, self.Wt[index]) + self.bt[index]) )

            self.lxr.append( tmp )
            tmpLoss = tmpLoss +  tf.reduce_mean( tf.square(tmp - self.x) ) 
            
            self.loptimizer.append( tf.train.AdamOptimizer(1e-4).minimize( tmpLoss   ) ) 


    def setup( self, sdev=0.2, lrate = 0.00002 ):
        dims = self.dimensions
        
        self.x =  tf.placeholder("float", shape=[None, dims[0]]) 
        self.noise =  tf.placeholder("float", shape=[None, dims[0]]) 

        for d in range( 1, len(dims) ) :

          self.W.append( tf.Variable( tf.truncated_normal([dims[d-1], dims[d]],
              stddev= sdev) ) )
          #W.append( tf.Variable( identity ) )
          self.b.append( tf.Variable( tf.constant(0., shape=[ dims[d] ]) ) )
          #self.b.append( tf.Variable( tf.truncated_normal( stddev = 0.1, shape=[ dims[d] ]) ) )
          #self.b0.append( tf.Variable( tf.constant(0., shape=[ dims[d] ]) ) )
          #self.b0.append( tf.Variable( tf.truncated_normal( stddev = 0.3, shape=[ dims[d] ]) ) )
          if self.linear == False:
            self.Wt.append( tf.Variable( tf.truncated_normal( [ dims[d], dims[d-1] ],
                      stddev=sdev) ) )
            #Wt.append( tf.Variable( identity ) )
            self.bt.append( tf.Variable( tf.constant( 0., shape=[ dims[d-1] ]) ) )
            #self.bt.append( tf.Variable( tf.truncated_normal( stddev = 0.1, shape=[ dims[d-1] ]) ) )
            #self.bt0.append( tf.Variable( tf.constant( 0., shape=[ dims[d-1] ]) ) )
            #self.bt0.append( tf.Variable( tf.truncated_normal( stddev = 0.3, shape=[ dims[d-1] ]) ) )

        if self.linear:
           self.Wl = tf.Variable( tf.truncated_normal( [dims[-1], dims[0]], stddev=sdev) )
           self.bl = tf.Variable( tf.constant(0., shape=[ dims[0] ]) )
        else:
           self.Wl = tf.Variable( np.identity(dims[0], np.float32 ) ) #tf.truncated_normal( [dims[0], dims[0]], stddev=0.5) )
           self.bl = tf.Variable( tf.constant(0., shape=[ dims[0] ]) )

        self.Wt.reverse()
        self.bt.reverse()

        


        ##endcoding and decoding

        self.z = [ tf.add(self.x, self.noise) ]
        for d in range( len( self.W ) )  :
          self.z.append( tf.nn.tanh( ( tf.matmul( self.z[-1], self.W[d] ) + self.b[d] ) ) )
          #p =  tf.matmul( self.z[-1], self.W[d] ) 
          #self.z.append( (1+tf.tanh( p + self.b0[d] ) ) / 2. * tf.tanh(p+self.b[d]) )


        self.xr = [ self.z[-1] ]
        for d in range( len( self.Wt ) ) :
          if self.linear:
            self.xr.append( tf.matmul(self.xr[-1], self.Wt[d]) + self.bt[d] ) 
            #p =  tf.matmul( self.xr[-1], self.Wt[d] ) 
            #self.xr.append( (1+tf.tanh( p + self.bt0[d] )) / 2. * tf.tanh(p+self.bt[d]) )
          else:
            self.xr.append( tf.nn.tanh( (tf.matmul(self.xr[-1], self.Wt[d]) + self.bt[d]) ) )

        #self.xr.append( tf.matmul(self.xr[-1], self.Wl) + self.bl) 
        


        ##reconstruction loss
        self.residual  = self.x - self.xr[-1] 
        self.residual2 = tf.square( self.residual  )
        self.l2loss = tf.reduce_mean( self.residual2  ) 
        #self.l2loss = tf.square( tf.reduce_mean( self.residual  ) )  
       
        ##joint loss
        self.loss = self.l2loss
        
        
        ##Dimensionality regularization 
        self.Jparts = []
        #compute Jacobian 
        for d in range(self.dimensions[0]):
            self.Jparts.append( [] )
            self.Jparts[d].append( tf.mul( 1 - tf.square( self.z[1]), 
                                   tf.slice( self.W[0], [d, 0],[1,-1] ) ) ) 
            for i in range( 1, len(self.W) ):
                   self.Jparts[d].append( tf.mul( 1 - tf.square( self.z[i+1] ), 
                                          tf.matmul( self.Jparts[d][-1], self.W[i] ) ) )

            for i in range( len(self.Wt) ):
                   self.Jparts[d].append( tf.mul( 1 - tf.square( self.xr[i+1] ),
                                          tf.matmul( self.Jparts[d][-1], self.Wt[i] ) ) )
                  #self.Jparts[d].append( tf.matmul( self.Jparts[d][-1], self.Wl ) ) 

        #compute Frobenius norm
        self.JF = tf.constant( 0., shape=[1] ) 
        for J in self.Jparts:
            self.JF = self.JF + tf.reduce_sum( tf.square( J[-1] ), 1 )
            

        if self.gamma > 0:
            self.Jloss = tf.square( self.gamma  - tf.reduce_mean( self.JF )  ) 
        else:
            self.Jloss = tf.reduce_mean( self.JF )   
        
        self._beta = tf.placeholder("float", [1])
        if self.beta > 0:
            self.loss = self.loss + self._beta * self.Jloss


        ##Orthogonal contraction penalty
        #self.o = [self.residual ]
        self.o = [ (self.residual + self.noise) ]
           
        for i in range( len( self.W  ) ) :
            self.o.append( tf.mul( 1 - tf.square( self.z[i+1] ), tf.matmul( self.o[-1], self.W[i]   ) ) )

        for i in range( len( self.Wt ) ) :
            self.o.append( tf.mul( 1 - tf.square( self.xr[i+1] ), tf.matmul( self.o[-1], self.Wt[i] ) ) )
        #self.o.append( tf.matmul( self.o[-1], self.Wl ) )

        rl2 = tf.reduce_sum( tf.square( self.o[0] ), 1) 
        self.ortho = tf.reduce_mean( tf.reduce_sum( tf.square( self.o[-1] ), 1) / rl2 )
        if self.tortho == "squared" :
            self.oloss = self.ortho
        elif self.tortho == "sqrt":
            self.oloss = tf.reduce_mean( tf.reduce_sum( tf.square( self.o[-1] ), 1) / tf.sqrt(rl2) )
        else:
            self.oloss = tf.reduce_mean( tf.square( self.o[-1] ) )
        #self.oloss = tf.reduce_mean( tf.sqrt( tf.square( self.o[-1] ) ) )
        
        self._alpha = tf.placeholder("float", [1])
        if self.alpha > 0 :
            self.loss = self.loss + self._alpha * self.oloss



        #optmizer
        #self.optimizer = tf.train.AdamOptimizer( learning_rate = lrate, beta1=0.3, beta2=0.31).minimize( self.loss ) 
        self.optimizer = tf.train.AdamOptimizer( learning_rate = lrate ).minimize( self.loss ) 
        #self.optimizer = tf.train.GradientDescentOptimizer( lrate ).minimize( self.loss )
        
    
        if False:
         self.gdo = tf.train.AdamOptimizer( lrate )
         self.grad = self.gdo.compute_gradients(self.loss)
         self.grad_scaling = tf.placeholder( "float", shape=[1] )
         self.gradstop = []
         self.grads = []
         for gp in self.grad:
             if (gp[0] is None) == False:
                self.grads.append(gp[0])
                g =  tf.stop_gradient( gp[0] * self.grad_scaling )
                self.gradstop.append( (g, gp[1] ) )
            #self.gradstop.append( ( gp[0], gp[1]) )
         self.gdo_apply = self.gdo.apply_gradients( self.gradstop  )





    def initalize (self, session):
        init = tf.initialize_all_variables();
        session.run([init])#, feed_dict={ identity: 1.*np.identity(dims[0]) } )
      



    def linesearch(self, session, inp, noise):
        lStart = session.run([self.loss], feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor )
                              } )

        session.run( self.grads, feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor )
                              } )
        op = session.run( [self.gdo_apply], 
                  feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor ),
                              self.grad_scaling: np.full([1], self._lrate) } )

        l = session.run( [self.loss], feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor )
                              } )

        
        if False: #l[0] < lStart[0]:
           pl = lStart
           while l < pl:
              pl = l
              op = session.run( [self.gdo_apply], 
                  feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor ),
                              self.grad_scaling: np.full([1], self._lrate) } )
              l = session.run( [self.loss], feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor )
                              } )
              self._lrate *= 2
           
           self._lrate /= 2
           op = session.run( [self.gdo_apply], 
                  feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor ),
                              self.grad_scaling: np.full([1], self._lrate) } )
           l = session.run( [self.loss], feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor )
                              } )

        else:
           while l > lStart :
              self._lrate *= 0.9
              op = session.run( [self.gdo_apply], 
                  feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor ),
                              self.grad_scaling: np.full([1], self._lrate) } )
              l = session.run( [self.loss], feed_dict={ self.x: inp, self.noise: noise, 
                              self._alpha: np.full([1], self.alpha * self.factor),  
                              self._beta: np.full([1], self.beta * self.factor )
                              } )
              if self._lrate < 0.000001:
                  break





    def optimize(self, session, data, nsteps):

       if self.stochastic == 0:
          inp = data.getData()
  
       for i in range(nsteps):

           if self.stochastic > 0:
              inp = data.getBatch(self.stochastic)

           if self.sigma > 0:
              #noise = np.random.uniform(-self.sigma, self.sigma, inp.shape)
              noise = np.random.normal(0, self.sigma, inp.shape) 
           else:
              noise = np.zeros(inp.shape) 
         
           #self.linesearch(session, inp, noise) 
           
           opt = session.run( [ self.optimizer ],  feed_dict={ self.x: inp, 
                               self.noise: noise, self._alpha: np.full([1], 
                               self.alpha * self.factor), 
                               self._beta: np.full([1], self.beta * self.factor ) } ) 
           
           
           #self.alpha = 0.1/l
           self.factor = min(self.factor + self.rate, self.maxFactor)
       
       l, rl, ol, jl, jf, o = session.run( [ self.loss, self.l2loss, self.oloss,
                                          self.Jloss, self.JF, self.ortho ], feed_dict={ self.x: inp, 
                                          self.noise: noise, self._alpha: np.full([1], 
                                          self.alpha * self.factor),  self._beta:
                                          np.full([1], self.beta * self.factor ) } )

       return l, rl, ol, jl, jf, o
   


    def optimizelayers(self, session, data, nsteps):

       if self.stochastic == 0:
          inp = data.getData()
  
       for opt in self.loptimizer:
           for i in range(nsteps):

               if self.stochastic > 0:
                  inp = data.getBatch(self.stochastic)

               if self.sigma > 0:
                  #noise = np.random.uniform(-self.sigma, self.sigma, inp.shape) 
                  noise = np.random.normal(0, self.sigma, inp.shape) 
               else:
                  noise = np.zeros(inp.shape) 
          
               res,  = session.run( [ opt  ], 
                                feed_dict={ self.x: inp, self.noise: noise } ) 
          


def main():
    pass


if __name__ == '__main__':
    main()
    
