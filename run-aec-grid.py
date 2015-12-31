import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import argparse
import time

import ae
import data2d

#fix seed
tf.set_random_seed(10)
np.random.seed(1)

parser = argparse.ArgumentParser(description='Autoencoder for spiral data set.')
parser.add_argument('--npoints', metavar='N', type=int, nargs='?', default=300,
                   help='number of points in grid data')
parser.add_argument('--noise', type=float, nargs='?', default=0.1,
                   help='amount of noise for orthogonal noise in grid data')

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
                   help='Learning rate fro Adam optimizer')


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



data = data2d.Grid(npoints=args.npoints, sigma = args.noise)



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
aec.setup( sdev=args.weights, lrate=args.lrate)







def drawgrid( xmin = -0.9, xmax = 0.9, ymin=-0.9, ymax=0.9, xspacing = 20, yspacing=20, nsamples=100, xrVar = aec.xr[-1] ) :
    for s in np.linspace(xmin, xmax, xspacing):
        y = np.linspace(ymin, ymax, nsamples)
        x = np.repeat(s, nsamples);
       
        xp = xrVar.eval( feed_dict={ aec.x: np.transpose( np.vstack([x, y, np.zeros([len(x)]) ]) ),
           aec.noise: np.zeros([len(x), 3] ) })
        plt.plot(xp[:,0], xp[:,1], color="0.2", linewidth=1.5, zorder=2)
        plt.plot(x, y, color="0.8", linewidth=1, zorder=1)
  
    for s in np.linspace(ymin, ymax, yspacing):
        x = np.linspace(xmin, xmax, nsamples)
        y = np.repeat(s, nsamples);
       
        xp = xrVar.eval( feed_dict={ aec.x: np.transpose( np.vstack([x, y, np.zeros([len(x)]) ] ) ),
           aec.noise: np.zeros([len(x), 3] ) })
        plt.plot(xp[:,0], xp[:,1], color="0.2", linewidth=1.5, zorder=2)
        plt.plot(x, y, color="0.8", linewidth=1, zorder=1)



x =  data.getData()
with tf.Session() as session:

  aec.initalize(session)

  drawgrid( xspacing=np.sqrt(args.npoints), yspacing = np.sqrt(args.npoints) ) 
  plt.axis('scaled')
  plt.tick_params(axis='both', which='major', labelsize=18)
  plt.tick_params(axis='both', which='minor', labelsize=12)
  plt.xlim(-1.05, 1.05)
  plt.ylim(-1.05, 1.05)
  plt.savefig( args.file + "/init.pdf" )
  #plt.show()
  plt.clf()
 
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


    rx = aec.xr[-1].eval( feed_dict={ aec.x: x, 
                                      aec.noise: np.zeros(x.shape)  })

    plt.scatter(x[:,0], x[:,1], c="#16AADB", marker=".", s=300, zorder=3, alpha=0.5)
    plt.scatter(rx[:,0], rx[:, 1], c="#F29E0C", marker=".", s=300, zorder=4, alpha=0.5)
    
    drawgrid( xspacing=np.sqrt(args.npoints), yspacing = np.sqrt(args.npoints) ) 
     
    plt.axis('scaled')
    plt.tick_params( axis='both', which='major', labelsize=18 )
    plt.tick_params( axis='both', which='minor', labelsize=12 )
    plt.xlim(-1.05, 1.05)
    plt.ylim(-1.05, 1.05)
    plt.savefig( args.file + "/xy-iteration-{:0>5d}.pdf".format( (i+1)*args.inner ) )
    #plt.show()
    plt.clf()

    plt.scatter(x[:,0], x[:,2], c="#16AADB", marker=".", s=300, zorder=3, alpha=0.5)
    plt.scatter(rx[:,0], rx[:, 2], c="#F29E0C", marker=".", s=300, zorder=4, alpha=0.5)
     
    plt.axis('scaled')
    plt.tick_params( axis='both', which='major', labelsize=18 )
    plt.tick_params( axis='both', which='minor', labelsize=12 )
    #plt.xlim(-1.05, 1.05)
    #plt.ylim(-1.05, 1.05)
    plt.savefig( args.file + "/xz-iteration-{:0>5d}.pdf".format( (i+1)*args.inner ) )
    #plt.show()
    plt.clf()
    
    tCurrent2 = time.clock()
    f.write("Plotting time " + str(tCurrent2 -  tCurrent) + "\n\n")
    f.flush()

  

    


