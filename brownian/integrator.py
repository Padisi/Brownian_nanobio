import numpy as np
from .utils import apply_pbc

def brownian_step(pos, forces, D, KbT, dt, pbc=True, L=None):
    N = np.shape(pos)[0]
    mu = D / KbT
    noise = np.sqrt(2*KbT*D*dt) * np.random.randn(N, 3)
    new_pos = pos + noise + mu * forces * dt
    if pbc and L is not None:
        new_pos = apply_pbc(new_pos, L)
    return new_pos
