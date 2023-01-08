"""
:file: ion_test.py

:author: Pavlo Vlastos

"""
import numpy as np

# Particle position vector
rx0 = 0.0
ry0 = 0.0
rz0 = 0.0

r_0 = np.array([[rx0],
                [ry0],
                [rz0]])
print("r.shape = {}".format(r_0.shape))

# Velocity vector
vx0 = 0.0
vy0 = 0.0
vz0 = 0.0

v_0 = np.array([[vx0],
                [vy0],
                [vz0]])
print("v.shape = {}".format(v_0.shape))

# Magnetic field vector
bx0 = -1.0
by0 = 0.0
bz0 = 0.0

b = np.array([[bx0],
              [by0],
              [bz0]])
print("b.T.shape = {}".format(b.T.shape))

# Charges
electron_charge_coulombs = 1.602176634*(10.0**(-19.0))
q_proton = 1.0
q_ion = q_proton*electron_charge_coulombs

# Distance between cathode and anode in meters
d_arc = 0.04

# Voltages
V_cathode = 50000.0
V_anode = 0.0
deltaV = V_cathode - V_anode

# Electric field magnitude between cathod and anode
E_mag = -deltaV/d_arc
print("E_mag = {}".format(E_mag))

# Electric field vector
Ex0 = 0.0
Ey0 = 0.0
Ez0 = -1.0

E = np.array([[Ex0],
              [Ey0],
              [Ez0]])*E_mag
print("E.T.shape = {}".format(E.T.shape))

r1 = E

# Force on an ion due to the electric field
# Units: Newtons (N), Coulombs (C)
# N = C * N / C
F_e = q_ion*E 
# epsilon_0 = 8.8541878128 * (10.0**(-12.0))
# F_e = 1/(4*np.pi*epsilon_0) * q_ion/(d_arc**2) * r1
print("F_e = {}".format(F_e))

# Mass of a proton in kg
m_proton = 1.67262192 * (10.0**(-27))
m_nitrogen_atom = 2.3258671 * (10.0**(-26))
m_oxygen_atom = 2.656 * (10.0**(-26))

m_ion = m_oxygen_atom

# Acceleration of ion due electric field
a_ion = F_e/m_ion
print("a_ion = {}".format(a_ion))

# Newtons equations of motion
# vf   = vi + a * t
# vf^2 = vi^2 + 2 * a * x
# x    = vi * t + (1/2) * a * t^2
vfz = np.sqrt((vz0**2) + (2*a_ion[2][0]*d_arc))

v_f = np.array([[0.0],
                [0.0],
                [vfz]])
print("vfz = {}".format(vfz))
print("c   = {}".format(2.998*(10.0**(8))))

t_traverse_z = (vfz - vz0)/a_ion[2][0]
print("t_traverse_z = {0:.9f}".format(t_traverse_z))

# Lorentz Force vector on an ion
# F_l = q*E.T + np.cross(q*v, b.T, axisa=0, axisb=1)
F_l = q_ion*E[:, 0] + np.cross(q_ion*v_f[:, 0], b[:, 0])
F_l = np.reshape(F_l, (3, 1))
print("F_l = {}".format(F_l))
print("F_l.shape = {}".format(F_l.shape))
