"""
:file: particle_model.py
:author: Pavlo Vlastos
"""
import numpy as np
from scipy.integrate import solve_ivp, RK45
from ..constants import constants as ct


class Particle_Model:
    """
    A dynamical model of a proton
    """

    def __init__(self, A=ct.A_1_proton, B=ct.B_1_proton, charge=ct.q_proton,
                 particle_type="proton"):
        """
        :brief: 
        This is a simplified particle model class. The default instantiation of
        this class is a proton.
        """

        self.x = np.zeros((ct.num_states_1_particle, 1))
        self.xdot = np.zeros((ct.num_states_1_particle, 1))
        self.A = A
        self.B = B
        self.u = np.zeros((3,1))
        self.u_m, self.u_n = self.u.shape
        self.x_m, self.x_n = self.x.shape
        self.charge = charge
        self.particle_type = particle_type

    def update(self, xdot=np.zeros((ct.num_states_1_particle, 1)),
               u=np.zeros((3,1))):
        """
        :brief: 
        :param xdot: the derivative of the state vector x
        :param u: The input 
        """

        for i in range(self.u_m):
            self.u[0][i] = u[0][i]

        self.xdot = self.A @ self.x + self.B @ self.u

        for i in range(self.x_m):
            xdot[i][0] = self.xdot[i][0]

        return xdot


    # def integrate(self, xdot=np.zeros((ct.num_states_1_particle, 1))):
    #     """
    #     :brief:
    #     :param u: The input
    #     """

    #     result = solve_ivp()
