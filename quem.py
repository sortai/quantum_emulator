import numpy as np

class qsys:
    def __init__(self, nstates = 2, initstate = None):
        if initstate is None:
            initstate = np.zeros((nstates,), dtype=np.complex128)
            initstate[0] = 1+0j
            self.state = initstate
        else:
            self.state = initstate.copy()
    def __len__(self):
        return len(self.state)
        
