import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import argparse
import time

import ae
import data2d

#fix seed
tf.set_random_seed(10)
np.random.seed(2)

parser = argparse.ArgumentParser(description='Autoencoder for spiral data set.')
parser.add_argument('--npoints', metavar='N', type=int, nargs='?', default=300,
                   help='number of points in spiral data')
parser.add_argument('--noise', type=float, nargs='?', default=0.03,
                   help='amount of noise for spiral data')
parser.add_argument('--width', type=float, nargs='?', default=0.,
                   help='create snake data set with width width')

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



if args.width > 0.:
    data = data2d.SineSnake(npoints=args.npoints, width = args.width, sigma = args.noise)
else:
    data = data2d.Sine(npoints=args.npoints, sigma = args.noise)




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





def sineline(npoints = 10000) :

    phi = np.linspace(0, np.pi, npoints)    
    arc = np.vstack([  np.cos(phi), np.sin(phi)  ] )
    arc[0,:] = arc[0,:] / 1.5
    arc[1,:] = (arc[1,:] -0.5) / 1.5
    arc = np.transpose(arc)

    xr = aec.xr[-1].eval( feed_dict={ aec.x: arc, 
                                      aec.noise: np.zeros(arc.shape) }) 
    plt.plot(xr[:,0], xr[:,1], color="0.2", linewidth=2.5, zorder=2)
    plt.plot(arc[:, 0], arc[:,1], color="0.8", linewidth=2, zorder=1)

def polargrid(radii = np.linspace(0.05, 1.5, 20), phi = np.linspace(0, np.pi,
    101), every=5, xrVar = aec.xr[-1] ) :
    arc = np.vstack([  np.cos(phi), np.sin(phi)  ] )
    arcs = []
    orcs = []
    for r in radii:
        a = arc * r
        a[0,:] = a[0,:]/1.5
        a[1,:] = (a[1,:]-0.5)/1.5
        orcs.append(a)
        arcs.append( xrVar.eval( feed_dict={ aec.x: np.transpose(a), 
                                             aec.noise: np.transpose( np.zeros(arc.shape) ) }) )

        plt.plot(arcs[-1][:,0], arcs[-1][:,1], color="0.2", linewidth=1.5, zorder=2)
        plt.plot(a[0, :], a[1,:], color="0.8", linewidth=1, zorder=1)
   
    if every < len(phi):
        for i in range( int( len(phi)/every)+1 ):
            l = np.zeros( [len(arcs), 2] )
            lo = np.zeros( [len(arcs), 2] )
            for j in range( len(arcs) ):
                l[j,:] = arcs[j][i*every, :]
                lo[j,:] = orcs[j][:, i*every]
        
            plt.plot(l[:,0], l[:,1], color="0.2", linewidth=1.5, zorder=2)
            plt.plot(lo[:,0], lo[:,1], color="0.8", linewidth=1, zorder=1)





x =  data.getData()
with tf.Session() as session:

  aec.initalize(session)

  polargrid() 
  plt.axis('scaled')
  plt.tick_params(axis='both', which='major', labelsize=18)
  plt.tick_params(axis='both', which='minor', labelsize=12)
  plt.xlim(-1.05,1.05)
  plt.ylim(-0.5,0.7)
  plt.savefig( args.file + "/init.pdf" )
  plt.clf()
  #plt.show()
 
  tStart = time.clock()
  for i in range(args.outer):

    l, rl, ol, jl, jf, o = aec.optimize(session, data, args.inner) 
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



    plt.scatter(x[:,0], x[:,1], c="#16AADB", marker=".", s=300, zorder=3, alpha=0.5)
    rx = aec.xr[-1].eval( feed_dict={ aec.x: x, 
                                      aec.noise: np.zeros(x.shape)  })
    plt.scatter(rx[:,0], rx[:, 1], c="#F29E0C", marker=".", s=300, zorder=4, alpha=0.5)
    
    #polargrid()
    sineline()
     
    plt.axis('scaled')
    plt.tick_params( axis='both', which='major', labelsize=18 )
    plt.tick_params( axis='both', which='minor', labelsize=12 )
    plt.xlim(-1.05,1.05)
    plt.ylim(-0.6,0.7)
    plt.savefig( args.file + "/iteration-{:0>5d}.pdf".format( (i+1)*args.inner ) )
    plt.clf()
    #plt.show()
    
    tCurrent2 = time.clock()
    f.write("Plotting time " + str(tCurrent2 -  tCurrent) + "\n\n")
    f.flush()

  

    


