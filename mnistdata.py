
import numpy as np



class MnistNines(object):

    def __init__(self, percentage = (0,1)):
        from sklearn.datasets import fetch_mldata
        mnist = fetch_mldata('MNIST original', data_home="mnist-data")

        self.data = mnist.data[mnist.target == 9, ]
        nrow = self.data.shape[0]
        self.data[ range( int( nrow*percentage[0] ), int( nrow*percentage[1]) ),  ]
        self.data = self.data / np.max(self.data) - 0.5

    def getData(self):
        return self.data

    def getBatch(self, npoints):
        index = np.random.random_integers(0, self.data.shape[0]-1, npoints)
        return self.data[index, :]

    def getDimension(self):
        return self.data.shape[1]




def main():
    pass

if __name__ == '__main__':
    main()

