import numpy as np
import matplotlib.pyplot as plt

def apply_pbc(pos, L):
    '''
    Apply periodic boundary conditions to the position vectors.
    Parameters:
    -----------
    pos : np.ndarray
        Position vectors of all particles, shape (N, 3).
    L : np.ndarray
        Length of the simulation box in each dimension.
    Returns:
    --------    
    pos : np.ndarray
        Position vectors after applying periodic boundary conditions, shape (N,3).
    '''
    return pos - L * np.round(pos / L)

def plot_state(pos, L=None):
    '''
    Plot the current state of the system in 3D.
    Parameters:
    -----------
    pos : np.ndarray
        Position vectors of all particles, shape (N, 3).
    L : np.ndarray
        Length of the simulation box in each dimension.
    '''
    plt.scatter(pos[:, 0], pos[:, 1], s=10)
    if L is not None:
        plt.hlines((-L[1]/2,L[1]/2), -L[0]/2, L[0]/2, colors=['black'])
        plt.vlines((-L[0]/2,L[0]/2), -L[1]/2, L[1]/2, colors=['black'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Brownian Motion of Particles')
    plt.axis('equal')
    plt.show()