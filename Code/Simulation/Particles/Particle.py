"""
:file: Particle.py
:author: Pavlo Vlastos
"""
import numpy as np

from scipy.linalg import expm
from scipy.integrate import solve_ivp, RK45
from Constants import Constants as CT


class Particle_Model:
    """
    A dynamical model of a proton
    """

    def __init__(self, id=-1, dt_sim=0.1, A=CT.A_1_proton, B=CT.B_1_proton,
                 charge=(CT.q_proton*CT.electron_charge_coulombs),
                 particle_type='proton'):
        """
        :brief: 
        This is a simplified particle model class. The default instantiation of
        this class is a proton.
        """

        self.id = id

        self.dt_sim = dt_sim

        self.position = np.zeros((3, 1))  # [ x,  y,  z]'
        self.velocity = np.zeros((3, 1))  # [vx, vy, vz]'
        self.x = np.zeros((CT.num_states_1_particle, 1))
        self.xdot = np.zeros((CT.num_states_1_particle, 1))
        self.A = A
        self.B = B

        AB = np.concatenate((self.A, self.B), axis=1)
        m, n = AB.shape
        Z = np.zeros((n-m, n))
        AB_Z = np.concatenate((AB, Z), axis=0)
        self.PhiGamma_ZI = expm(AB_Z*self.dt_sim)
        _, An = self.A.shape
        self.Phi = self.PhiGamma_ZI[0:m, 0:An]
        self.Gamma = self.PhiGamma_ZI[0:m, An:]

        self.u = np.zeros((3, 1))
        self.charge = charge
        self.particle_type = particle_type
        self.fusion_proximity_flag = False

    def update_discrete(self,  u=np.zeros((3, 1))):
        """
        :brief: 
        :param u: The input 
        """

        self.u = u

        self.x = self.Phi @ self.x + self.Gamma @ self.u

        self.position[0][0] = self.x[0][0]
        self.position[1][0] = self.x[1][0]
        self.position[2][0] = self.x[2][0]

        self.velocity[0][0] = self.x[3][0]
        self.velocity[1][0] = self.x[4][0]
        self.velocity[2][0] = self.x[5][0]

    def update_continous(self, xdot=np.zeros((CT.num_states_1_particle, 1)),
                         u=np.zeros((3, 1))):
        """
        :brief: 
        :param xdot: the derivative of the state vector x
        :param u: The input 
        """

        self.u = u

        self.xdot = self.A @ self.x + self.B @ self.u

        xdot = self.xdot

        return xdot

    # def integrate(self, xdot=np.zeros((CT.num_states_1_particle, 1))):
    #     """
    #     :brief:
    #     :param u: The input
    #     """

    #     result = solve_ivp()

    def set_fusion_proximity_flag(self, status=False):
        """
        :param status: True or False
        """
        self.fusion_proximity_flag = False

    def set_position(self, position=np.zeros((3, 1))):
        """
        :param position: A 3x1 position vector
        """
        self.position = position

    def set_velocity(self, velocity=np.zeros((3, 1))):
        """
        :param velocity: A 3x1 velocity vector
        """
        self.velocity = velocity

    def set_id(self, id=-1):
        """
        :param id:
        """
        self.id = id

    def get_position(self):
        """
        :rtype: float
        """

        return self.position

    def get_velocity(self):
        """
        :rtype: float
        """

        return self.velocity

    def get_charge(self):
        """
        :rtype: float
        """

        return self.charge

    def get_id(self):
        """
        :rtype int
        """
        return self.id
