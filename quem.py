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
    @staticmethod
    def kron(*syss):
        if len(syss) == 1:
            return syss[0]
        res = qsys.kron(*syss[1:])
        return qsys(
            len(syss[0])*len(res),
            np.kron(a.state, res.state)
            )

def bqsys(self, nbits = 1, initstate = None):
        return qsys(nstates = 2**nbits, initstate)

class qgate:
    def __init__(self, nstates = 2, mat = None):
        if mat.size[0] != nstates: raise NumberOfStatesError("mat.size[0] != nstates")
        self.mat = np.array(mat)
    def __len__(self):
        return self.mat.shape[0]
    @staticmethod
    def kron(*gates):
        if len(gates) == 1:
            return gates[0]
        res = qgate.kron(*gates[1:])
        return qgate(
            len(gates[0])*len(res),
            np.kron(a.mat, res.mat)
            )
    
