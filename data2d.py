
import numpy as np



class Sine(object):

    def __init__(self, npoints, sigma=0.1):
        self.npoints = npoints
        self.sigma = sigma
        phi = np.random.uniform(0, 1, npoints) * np.pi
        arc = np.vstack([  np.cos(phi)/1.5, (np.sin(phi)-0.5)/1.5 ] )
        if self.sigma > 0 :
           arc = arc + np.random.normal(0, self.sigma, arc.shape)

        self.data = np.transpose(arc)


    def getData(self):
        return self.data

    def getBatch(self, npoints):
        index = np.random.random_integers(0, self.data.shape[0]-1, npoints)
        return self.data[index, :]

    def getDimension(self):
        return 2



class SineSnake(object):

    def __init__(self, npoints, width=0.2, sigma=0.2):
        self.npoints = npoints
        self.sigma = sigma
        self.width = width
        
        phi = np.random.uniform(0, 1, npoints) * np.pi
        arc = np.vstack([  np.cos(phi), np.sin(phi) ] )
        arc = arc * (1+np.exp(-(phi-np.pi/2)**2 / self.sigma ) * np.random.uniform(-self.width, self.width, arc.shape)) 
        arc[0, :] = arc[0,:] / 1.5
        arc[1, :] = (arc[1,:] - 0.5) / 1.5
        arc = np.vstack([arc, np.random.normal(0, sigma/10., npoints)])
        self.data = np.transpose(arc)


    def getData(self):
        return self.data

    def getBatch(self, npoints):
        index = np.random.random_integers(0, self.data.shape[0]-1, npoints)
        return self.data[index, :]
        
    
    def getDimension(self):
        return 2




class Spiral(object):

    def __init__(self, npoints, sigma=0.01):
        self.npoints = npoints
        self.sigma = sigma
        
        phi = np.random.uniform(0.5, 3.5, npoints) 
        
        arc = np.vstack([  np.cos(phi*np.pi), np.sin(phi*np.pi) ] ) * (0.1+phi/3.5)
        arc = arc / 1.5
        
        if self.sigma > 0 :
           arc = arc + np.random.normal(0, self.sigma, arc.shape) 
        
        self.data = np.transpose(arc)


    def getData(self):
        return self.data

    def getBatch(self, npoints):
        index = np.random.random_integers(0, self.data.shape[0]-1, npoints)
        return self.data[index, :]
        
    
    def getDimension(self):
        return 2



def main():
    pass

if __name__ == '__main__':
    main()

