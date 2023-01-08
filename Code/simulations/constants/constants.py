"""
Constants.py

A bunch of constants, vectors, and matrices

:author: Pavlo Vlastos
"""
import numpy as np

# Tolerances


# Useful constants
electron_charge_coulombs = 1.602176634*(10.0**(-19.0))
speed_of_light = 2.998*(10.0**(8.0))  # m/s
vacuum_magnetic_permeability = 1.25663706212*(10.0**(-6.0))  # N A^(-2)
standard_uncertainty = 0.00000000019*(10.0**(-6.0))  # N A^(-2)
Coulomb_constant = 8.9875517923*(10.0**(9.0))  # (N m^2)/(C^2)
k_e = Coulomb_constant
dist_electron_proton_gnd_state = 5.29*(10.0**(-11.0))
fusion_proximity_distance = 1.0*(10.0**(-15.0))

# Charge
q_proton = 1.0
q_electron = -1.0

# The energy it takes for an electron to escape the nucleus
# of a hydrogen atom, i.e. ionize
e_escape = 13.6 * electron_charge_coulombs

# Mass of a proton in kg
m_proton = 1.67262192 * (10.0**(-27))
m_electron = 9.1093837 * (10.0**(-31))
m_hydrogen = m_proton + m_electron
m_nitrogen_atom = 2.3258671 * (10.0**(-26))
m_oxygen_atom = 2.656 * (10.0**(-26))

# States
num_states_1_particle = 6

# Continuos Dynamics Matrices

# Proton Dynamics
# State[xdot, ydot, zdot, xddot, yddot, zddot]'
A_1_proton = np.array([[0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

B_1_proton = np.array([[0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0],
                      [1.0/m_proton, 0.0, 0.0],
                      [0.0, 1.0/m_proton, 0.0],
                      [0.0, 0.0, 1.0/m_proton]])


# Electron Dynamics
# State[xdot, ydot, zdot, xddot, yddot, zddot]'
A_1_electron = np.array([[0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

B_1_electron = np.array([[0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0],
                         [1.0/m_electron, 0.0, 0.0],
                         [0.0, 1.0/m_electron, 0.0],
                         [0.0, 0.0, 1.0/m_electron]])
