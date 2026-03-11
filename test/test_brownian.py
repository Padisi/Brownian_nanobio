def test_import():
    from brownian.integrator import brownian_step
    from brownian.forces import lennard_jones
    from brownian.utils import plot_state
    assert brownian_step is not None
    assert lennard_jones is not None
    assert plot_state is not None

import numpy as np

def test_pbc():
    from brownian.utils import apply_pbc
    L = np.array([10.0, 10.0, 10.0])
    pos = np.array([[11.0, 12.0, 13.0], [-11.0, -12.0, -13.0]])
    pos_pbc = apply_pbc(pos, L)
    # Check a simple case where I know the solution
    assert np.all(pos_pbc[0] == [1.0, 2.0, 3.0])
    assert np.all(pos_pbc[1] == [-1.0, -2.0, -3.0])

def test_lennard_jones():
    from brownian.forces import lennard_jones
    pos = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
    epsilon = 1.0
    sigma = 1.0
    F = lennard_jones(pos, epsilon=epsilon, sigma=sigma, pbc=False)
    # Check that the force is repulsive at r=sigma
    assert np.all(F[0] == [-24.0, 0.0, 0.0])
    assert np.all(F[1] == [24.0, 0.0, 0.0])

def test_brownian_step():
    from brownian.integrator import brownian_step
    pos = np.array([[0.0, 0.0, 0.0]*10000]).reshape(-1, 3)
    F = np.array([[0.0, 0.0, 0.0]*10000]).reshape(-1, 3)
    D = 1.0
    KbT = 1.0
    dt = 1
    # Check gaussian noise
    pos_new = brownian_step(pos, F, D, KbT, dt, pbc=False)
    noise = pos_new - pos
    print("Mean of noise:", np.mean(noise, axis=0))
    print("Variance of noise:", np.var(noise))
    assert np.allclose(np.mean(noise, axis=0), 0.0, atol=0.1) # we check the mean is close to zero with tolerance  (atol) of 0.1
    assert np.isclose(np.var(noise), 2*KbT*D*dt, rtol=0.05) # we check the variance is close to 2*KbTD*dt with relative tolerance (rtol) of 0.05
    # This test can fail occasionally due to the randomness, but should pass most of the time. If it fails, try running it again.
    # This is a bad example of testing randomness that we comment in class. If you develop a better way to test this, please share it with the class!
