"""
:file: ion_model.py
:author: Pavlo Vlastos
"""
import numpy as np
from scipy.integrate import solve_ivp, RK45
from ...constants import constants as ct


def __init__(self):
    """
    :brief: 
    """

    self.x = np.zeros((ct.num_states, 1))
    self.xdot = np.zeros((ct.num_states, 1))
    self.A = np.zeros((ct.num_states, ct.num_states))
    self.B = np.zeros((ct.num_states, 1))
    self.u = np.zeros((1, ct.num_states))


def calculate_u(self):
    """
    :brief: 
    """
    self.u[0][0] = 0.0
    self.u[1][0] = 0.0
    self.u[2][0] = 0.0
    self.u[3][0] = 0.0
    self.u[4][0] = 0.0
    self.u[5][0] = 0.0

    fc = 


def update(self, xdot=np.zeros((ct.num_states, 1)),
           u=np.zeros((1, ct.num_states))):
    """
    :brief: 
    :param xdot: the derivative of the state vector x
    :param u: The input 
    """

    self.xdot = self.A @ self.x + self.B @ self.u

    xdot = self.xdot

    return xdot


# def integrate(self, xdot=np.zeros((ct.num_states, 1))):
#     """
#     :brief:
#     :param u: The input
#     """

#     result = solve_ivp()
