import numpy as np
from .utils import apply_pbc

def lennard_jones(pos, epsilon, sigma, pbc=True, L=None):
    '''
    Calculate the Lennard-Jones force between particles.
    Parameters:
    -----------
    pos : np.ndarray
        Position vectors of all particles, shape (N, 3).
    epsilon : float
        Depth of the potential well.
    sigma : float
        Finite distance at which the inter-particle potential is zero.
    pbc : bool, optional
        Whether to apply periodic boundary conditions (default is True).
    L : np.ndarray, optional
        Length of the simulation box in each dimension.
    Returns:
    --------
    F : np.ndarray
        Force vectors on each particle, shape (N, 3).
    '''
    r_ij = (pos[:, np.newaxis] - pos[np.newaxis, :])
    if pbc:
        r_ij = apply_pbc(r_ij, L)
    modr = np.linalg.norm(r_ij, axis=2) # 2 to contract over the spatial dimension
    s_r = sigma / modr
    s_r[modr == 0] = 0 # Avoid division by zero for self-interaction
    s_r2 = s_r * s_r
    s_r6 = s_r2 * s_r2 * s_r2
    s_r12 = s_r6 * s_r6
    modF = 24 * epsilon * (2 * s_r12 - s_r6)
    F_ij = modF[:,:,np.newaxis] * r_ij * s_r[:,:,np.newaxis] / sigma # Normalize the force vector
    F = np.sum(F_ij, axis=1) # Sum over j to get the total force on each particle
    return F