import numpy as np
from random import random
from exceptions import *

class qsys:
    def __init__(self, nstates = 2, initstate = None):
        if initstate is None:
            initstate = np.zeros((nstates,), dtype=np.complex128)
            initstate[0] = 1+0j
            self.state = initstate
        else:
            if len(initstate) != nstates: raise NumberOfStatesError("len(initstate) != nstates")
            self.state = np.array(initstate)
    def __len__(self):
        return len(self.state)
    @property
    def ps(self):
        return self.state*[c.conjugate() for c in self.state]
    def measurement(self):
        r=random()
        for n, p in enumerate(self.ps):
            if r<p:
                self.state = np.zeros(len(self.state), dtype=np.complex128)
                self.state[n] = 1+0j
                return self.state.copy()
            else: r-=p
    def tenmult(self, other):
        return qsys(
            len(self.state)*len(other.state),
            [self.state[int(i/len(self.state))]*other.state[i%len(other.state)] for i in range(len(self.state)*len(other.state))]
            )


        
    
