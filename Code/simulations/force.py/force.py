"""
:file: ion_test.py

:author: Pavlo Vlastos

"""
import numpy as np
from ..particle_model import particle as pl


def calculate_F(self, q_particle=1.0,
                particle_a_position_xyz=np.zeros((3, 1)),
                particle_b_position_xyz=np.zeros((3, 1))):

    ell = particle_a_position_xyz - particle_b_position_xyz

    ell_norm = np.linalg.norm(ell)

    # Limit the closest distance between two particles for now
    if ell_norm > ct.dist_electron_proton_gnd_state:

        ell_norm = ct.dist_electron_proton_gnd_state

    ellhat = ell/np.linalg.norm(ell)
    F = ct.Coulomb_constant * ct.q_proton * np.abs(q_particle) *
