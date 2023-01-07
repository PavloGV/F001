"""
:file: ion_three_body_problem.py

:author: Pavlo Vlastos

"""
import numpy as np
import Constants.Constants as CT
import Particle_Model.Particle as PL
import Forces.Forces as FC

# Setup 3 particles: two protons and an electron
proton_0 = PL.Particle_Model(A=CT.A_1_proton,
                             B=CT.B_1_proton,
                             particle_type='proton',
                             charge=CT.q_proton)

proton_1 = PL.Particle_Model(A=CT.A_1_proton,
                             B=CT.B_1_proton,
                             particle_type='proton',
                             charge=CT.q_proton)

electron_0 = PL.Particle_Model(A=CT.A_1_electron,
                               B=CT.B_1_electron,
                               particle_type='electron',
                               charge=CT.q_electron)

proton_0.set_position(np.array((-0.01, 0.0, 0.0)))
proton_1.set_position(np.array((0.01, -0.01, 0.0)))
electron_0.set_position(np.array((-0.01, -0.02, 0.0)))

# Time
num_steps = 1000.0
first_step = 0.0
last_step = num_steps
step = 1.0
dt = 1.0/CT.speed_of_light
t0 = 0.0
tf = dt*num_steps
steps = np.arange(first_step, last_step, step)

# Main loop
for k in steps:

    # calculate forces at current time step

    # Update the particle states

    # Integrate their acceleration

# Plot
