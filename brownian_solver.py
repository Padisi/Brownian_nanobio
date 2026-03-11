import numpy as np
import matplotlib.pyplot as plt
# Standard import of python. from folder(.subfolder).file import function_name
# Every folder/subfolder must have an __init__.py file to be recognized as a package.
# Even if the __init__.py file is empty, it is necessary for the import to work.
# __init__.py files are used to initialize the package and can also be used to define what is available when the package is imported.
from brownian.utils import plot_state
from brownian.forces import lennard_jones
from brownian.integrator import brownian_step

KbT = 1
D = 1
N = 100
L = np.array([8.0, 10.0, 10.0])
dt = 0.01
Nsteps = 1000
epsilon = 10.0
sigma = 0.1
pos = np.random.rand(N, 3)* L - L/2 # Initial pos

for i in range(Nsteps):
    F = lennard_jones(pos, epsilon=epsilon, sigma=sigma, pbc=True, L=L)
    pos = brownian_step(pos, F, D, KbT, dt, pbc=True, L=L)

plot_state(pos, L)