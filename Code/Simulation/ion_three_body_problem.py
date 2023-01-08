"""
:file: ion_three_body_problem.py

:author: Pavlo Vlastos

"""
import numpy as np
import Constants.Constants as CT
import Particles.Particle as PL
import Forces.Forces as FC
import matplotlib.pyplot as plt

###############################################################################
# Time
num_steps = 100
first_step = 0
last_step = num_steps
step = 1
dt = 1.0/CT.speed_of_light
# dt = 0.1
steps = np.arange(first_step, last_step, step, dtype=np.int64)
t = np.zeros((num_steps, 1))

###############################################################################
# Distance between cathode and anode in meters
d_arc = 0.04

# Voltages
V_cathode = 50000.0
V_anode = 0.0
deltaV = V_cathode - V_anode

# Electric field magnitude between cathod and anode
E_mag = -deltaV/d_arc

###############################################################################
# Setup 3 particles: two protons and an electron
p_0 = PL.Particle_Model(id=0, dt_sim=dt, A=CT.A_1_proton,
                        B=CT.B_1_proton,
                        particle_type='proton',
                        charge=CT.q_proton*CT.electron_charge_coulombs)

p_1 = PL.Particle_Model(id=1, dt_sim=dt, A=CT.A_1_proton,
                        B=CT.B_1_proton,
                        particle_type='proton',
                        charge=CT.q_proton*CT.electron_charge_coulombs)

p_2 = PL.Particle_Model(id=2, dt_sim=dt, A=CT.A_1_electron,
                        B=CT.B_1_electron,
                        particle_type='electron',
                        charge=CT.q_electron*CT.electron_charge_coulombs)
x0 = 1.0*(10.0**(-9.0))
y0 = 1.0*(10.0**(-9.0))
z0 = 1.0*(10.0**(-9.0))
p_0.set_position(np.array([[-x0], [0.0], [0.0]]))
p_1.set_position(np.array([[x0], [-y0], [0.0]]))
p_2.set_position(np.array([[-x0], [-y0], [0.0]]))

particle_list = [p_0, p_1, p_2]

position_matrix = np.zeros((3, 3, num_steps))
velocity_matrix = np.zeros((3, 3, num_steps))

# Electric field
E = np.array([[0.0],
              [0.0],
              [-1.0]])*E_mag

# Magnetic field
B = np.array([[0.0],
              [1.0],
              [0.0]])*1.0

F_c   = np.zeros((3,1))
F_l   = np.zeros((3,1))
F_sum = np.zeros((3,1))

###############################################################################
# Main loop
for k in steps:

    # Loop through all particles
    for i, particle in enumerate(particle_list):

        # calculate forces at current time step
        F_c = FC.calculate_F_coulomb_all(particle, particle_list)
        F_l = FC.calculate_F_Lorentz(particle, E, B)
        F_sum = F_c + F_l

        # Update the particle states
        particle.update_discrete(F_sum)

        r = particle.get_position()
        
        rdot = particle.get_velocity()

        position_matrix[i][0][k] = r[0][0]
        position_matrix[i][1][k] = r[1][0]
        position_matrix[i][2][k] = r[2][0]

        velocity_matrix[i][0][k] = rdot[0][0]
        velocity_matrix[i][1][k] = rdot[1][0]
        velocity_matrix[i][2][k] = rdot[2][0]

    t[k] = k*dt

###############################################################################

fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('P_0 Position')
# print("position_matrix.shape = {}".format(position_matrix.shape))
# print("t.shape               = {}".format(t.shape))
axs[0].plot(t, position_matrix[0][0][:], label='P_0 x')
axs[1].plot(t, position_matrix[0][1][:], label='P_0 y')
axs[2].plot(t, position_matrix[0][2][:], label='P_0 z')

axs[0].grid()
axs[1].grid()
axs[2].grid()

axs[2].set_xlabel("Time (seconds)")

axs[0].set_ylabel("X (meters)")
axs[1].set_ylabel("Y (meters)")
axs[2].set_ylabel("Z (meters)")

plt.show()

###############################################################################

fig, axs = plt.subplots(3, sharex=True)
fig.suptitle('P_0 Velocity')
axs[0].plot(t, velocity_matrix[0][0][:], label='P_0 vx')
axs[1].plot(t, velocity_matrix[0][1][:], label='P_0 vy')
axs[2].plot(t, velocity_matrix[0][2][:], label='P_0 vz')

axs[0].grid()
axs[1].grid()
axs[2].grid()

axs[2].set_xlabel("Time (seconds)")

axs[0].set_ylabel("VX (m/s)")
axs[1].set_ylabel("VY (m/s)")
axs[2].set_ylabel("VZ (m/s)")

plt.show()
###############################################################################
# Plot
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(position_matrix[0][0][:],
             position_matrix[0][1][:],
             position_matrix[0][2][:], label='P_0')

ax.scatter3D(position_matrix[1][0][:],
             position_matrix[1][1][:],
             position_matrix[1][2][:], label='P_1')

ax.scatter3D(position_matrix[2][0][:],
             position_matrix[2][1][:],
             position_matrix[2][2][:], label='P_2')

ax.set_xlabel("X (meters)")
ax.set_ylabel("Y (meters)")
ax.set_zlabel("Z (meters)")

ax.legend()
plt.show()
