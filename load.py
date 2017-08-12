from scipy import ndimage, misc
import rebound
import numpy as np

def fromFile(f):
    ji = misc.imread(f)[:,:,0]
    sim = rebound.Simulation()
    while sim.N<1000:
        y, x = np.random.randint(ji.shape[0]),np.random.randint(ji.shape[1])
        if ji[y,x]==0:
            sim.add(m=1,x=x,y=-y,z=10*np.random.normal())
    sim.move_to_com()  
    sim.dt = 1
    sim.softening = 2
    return sim
