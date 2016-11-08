import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import argparse
import time

import ae
import mnistdata




#fix seed
tf.set_random_seed(10)
np.random.seed(2)

parser = argparse.ArgumentParser(description='Autoencoder for MNIST data set.')

parser.add_argument('--noise', type=float, nargs='?', default=20,
                   help='amount of noise added to data')

parser.add_argument('--dimension', type=int, nargs='+',
                   help='Layers of the autoencoder')

parser.add_argument('--weights', type=float, nargs='?', default=0.2,
                   help='Setup standard deviation for weight initalization')

parser.add_argument('--stochastic', metavar='N', type=int, nargs='?', default=0,
                   help='Number of points in stochastic optimization. On default(0) all points are used')
parser.add_argument('--sigma', type=float, nargs='?', default=0.,
                   help='Denoising autoencoder with Normal distribution noise with sdev sigma')

parser.add_argument('--alpha', type=float, nargs='?', default=0.,
                   help='Orthogonal penalty regularization')
parser.add_argument('--tortho', type=str, nargs='?', default="squared",
                   help='Orthogonal penalty type')
parser.add_argument('--beta', type=float, nargs='?', default=0.,
                   help='Jacobian penalty regularization')
parser.add_argument('--gamma', type=float, nargs='?', default=0.,
                   help='(gamma - sqrt(Jacobian))^2 penalty regularization')

parser.add_argument('--factor', type=float, nargs='?', default=1.,
                   help='global factor for all regulariztaion parameter')
parser.add_argument('--frate', type=float, nargs='?', default=0.,
                   help='Increase gobal factor after every iteration by frate')

parser.add_argument('--lrate', type=float, nargs='?', default=0.00001,
                   help='Learning rate for Adam optimizer')


parser.add_argument('--outer', type=int, nargs='?', default=40,
                   help='Number of outer optimization each of inner steps. Print after every outer iterations')
parser.add_argument('--inner', type=int, nargs='?', default=500,
                   help='Number of inner optimization.')
parser.add_argument('--file', type=str, nargs='?', default='./',
                   help='Store results in folder.')


args = parser.parse_args()

f = open(args.file + "/args.txt", 'w')
f.write( str(args) )
f.close()

f = open(args.file + "/log.txt", 'w')

data = mnistdata.MnistNines(percentage=(0,0.75) )
testdata = mnistdata.MnistNines(percentage=(0.75, 1) ) 


#setup autoencoder
aec = ae.AutoEncoder()
aec.addDimension( data.getDimension() )
for d in args.dimension :
  aec.addDimension( d )
aec.stochastic = args.stochastic
aec.sigma = args.sigma
aec.alpha = args.alpha
aec.tortho = args.tortho
aec.beta = args.beta
aec.gamma = args.gamma
aec.rate = args.frate
aec.factor = args.factor
aec.setup( sdev=args.weights, lrate=args.lrate )





trainRes = np.zeros((args.outer, 6))
testRes = np.zeros((args.outer, 6))

x = data.getData()
xt = testdata.getData()

x.tofile( args.file + "/train.npy" )
xt.tofile( args.file + "/test.npy" )

with tf.Session() as session:

  aec.initalize(session)


  tStart = time.clock()
  for i in range(args.outer):

    l, rl, ol, jl, jf, o, tl, trl, tol, tjl, tjf, to = aec.optimize(session, data, args.inner, testdata) 
    tCurrent = time.clock()
    f.write( "time elpased " + str(tCurrent - tStart) + "\n"  )
    #f.write( "train lloss %s" % ll
    f.write( "train loss " + str(l) + "\n" )
    f.write( "train rloss " + str(rl) + "\n"  )
    f.write( "train oloss " + str(ol) + "\n"  )
    f.write( "train Jloss " + str(jl) + "\n"  )
    f.write( "train regularization factor "  + str( aec.factor ) + "\n"  )
    f.write( "train factor * alpha * oloss " + str( aec.alpha * aec.factor * ol ) + "\n"  )
    f.write( "train factor * beta  * Jloss " + str( aec.beta  * aec.factor * jl ) + "\n" )
    f.write( "frob norm " + str( np.mean(np.sqrt(jf)) )  + "\n"  )
    f.write( "ortho " + str( np.sqrt(o) )  + "\n"  )



    rx = aec.xr[-1].eval( feed_dict={ aec.x: x, 
                                      aec.noise: np.zeros(x.shape)  })
    rxt = aec.xr[-1].eval( feed_dict={ aec.x: xt, 
                                      aec.noise: np.zeros(xt.shape)  })
    
    f.flush()
    rx.tofile( args.file + "/iteration-{:0>5d}-train.npy".format( (i+1)*args.inner ) )
    rxt.tofile( args.file + "/iteration-{:0>5d}-test.npy".format( (i+1)*args.inner ) )

    trainRes[i, :] = np.array(  [l,  rl,  ol,  jl,  np.mean(np.sqrt(jf)),  o] )
    testRes[i, :]  = np.array( [tl, trl, tol, tjl, np.mean(np.sqrt(tjf)), to] )
    


#plot risk progression 
plt.tick_params(axis='both', which='major', labelsize=24)
plt.tick_params(axis='both', which='minor', labelsize=17)
plt.plot( np.array(range(args.outer)) , 
          np.sqrt( trainRes[:, 1] ), c="#028C2F", linewidth=4)
plt.plot( np.array(range(args.outer)) , 
          np.sqrt( testRes[:, 1] ),  c="#3C007E", linewidth=4, ls="--")
plt.xlabel('Iterations (in {0})'.format(args.inner), fontsize=30)
plt.ylabel('Root mean square error', fontsize=30)
plt.ylim( ymin = 0, ymax=0.35 )
plt.tight_layout()
plt.savefig( args.file + "/loss.pdf" )
plt.clf()
    

    



