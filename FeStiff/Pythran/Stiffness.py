import numpy as np
#from StiffOut import *
import StiffOut as Sout
class Stiffness:
    def __init__(self):
        self.ji=np.empty((2,2))
        self.grads=np.empty((18,2))
        self.gq=np.array([[-1., -1.],
                          [ 1.,  1.],
                          [-1., -1.],
                          [ 1.,  0.],
                          [ 1.,  0.],
                          [-1.,  0.],
                          [ 0., -1.],
                          [ 0.,  1.],
                          [ 0.,  1.],
                          [ 0., -2.],
                          [-2., -2.],
                          [ 2.,  0.],
                          [ 0.,  2.],
                          [ 2.,  2.],
                          [ 2.,  0.],
                          [ 0.,  2.],
                          [-2., -2.],
                          [-2.,  0.]])


    def op(self,x,y,m):
        Sout.StiffOut(x,y,m,self.ji,self.grads,self.gq)
