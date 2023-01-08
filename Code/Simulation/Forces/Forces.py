"""
:file: Forces.py

:author: Pavlo Vlastos

"""
import numpy as np
from Constants import Constants as CT
from Particles import Particle as PL


def calculate_F_Lorentz(particle_a=PL.Particle_Model(),
                        E=np.zeros((3, 1)),
                        B=np.zeros((3, 1))):
    """
    :param particle_a: A particle: electron, proton, deuteron, etc.
    :param particle_a:
    """

    q_a = particle_a.get_charge()

    v = particle_a.get_velocity()

    F_Lorentz = q_a*(E[:, 0] + np.cross(v[:, 0], B[:, 0]))
    F_Lorentz = np.reshape(F_Lorentz, (3, 1))

    return F_Lorentz

def calculate_F_coulomb(particle_a=PL.Particle_Model(),
                        particle_b=PL.Particle_Model()):

    q_a = particle_a.get_charge()
    q_b = particle_b.get_charge()

    r_a = particle_a.get_position()
    r_b = particle_b.get_position()

    ell = r_a - r_b

    ell_norm = np.linalg.norm(ell)

    # Limit the closest distance between two particles to avoid division by zero
    if ((ell_norm < CT.dist_electron_proton_gnd_state) and
            (particle_a.particle_type != particle_b.particle_type)):

        ell_norm = CT.dist_electron_proton_gnd_state

    elif ((ell_norm < CT.fusion_proximity_distance) and
          (particle_a.particle_type == 'proton') and
            (particle_b.particle_type == 'proton')):

        particle_a.set_fusion_proximity_flag(True)
        particle_b.set_fusion_proximity_flag(True)

        ell_norm = CT.fusion_proximity_distance

        print("**** ********************************* ****")
        print("**** Force.py: Fusion proximity alert! ****")
        print("**** ********************************* ****")

    ellhat = ell/ell_norm

    k_e = CT.Coulomb_constant

    F_Coulomb = k_e * np.abs(q_a) * np.abs(q_b) * ellhat / (ell_norm**2.0)


def calculate_F_coulomb_all(particle_a=PL.Particle_Model(),
                            particle_list=[PL.Particle_Model()]):

    q_a = particle_a.get_charge()
    q_a_abs = np.abs(q_a)
    r_a = particle_a.get_position()

    F_sum = np.zeros((3, 1))

    for i, particle_i in enumerate(particle_list):

        if particle_a.get_id() != particle_i.get_id():
            q_b = particle_i.get_charge()

            r_b = particle_i.get_position()

            ell = r_a - r_b

            ell_norm = np.linalg.norm(ell)

            # Limit the closest distance between two particles to avoid division by zero
            if ((ell_norm < CT.dist_electron_proton_gnd_state) and
                    (particle_a.particle_type != particle_i.particle_type)):

                ell_norm = CT.dist_electron_proton_gnd_state

            if ((ell_norm < CT.fusion_proximity_distance) and
                (particle_a.particle_type == 'proton') and
                    (particle_i.particle_type == 'proton')):

                particle_a.set_fusion_proximity_flag(True)
                particle_i.set_fusion_proximity_flag(True)

                ell_norm = CT.fusion_proximity_distance

                print("** ********************************* **")
                print("** Force.py: Fusion proximity alert! **")
                print("** Particle a and Particle {}        **".format(i))
                print("** ********************************* **")

            ellhat = ell/ell_norm

            F_sum += (CT.k_e * q_a_abs * np.abs(q_b) * ellhat) / (ell_norm**2.0)

    return F_sum