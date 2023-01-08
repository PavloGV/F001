"""
:file: energy.py

:auhtor: Pavlo Vlastos

"""
import numpy as np

radius_minor = 0.01 # meters
radius_major = 0.05 # 

pressure_air = 1.0 # atmosphere

volume_torus = (np.pi * radius_minor) * (2.0 * np.pi * radius_major)

ideal_gas_constant = 0.082057366080960 # L*atm*K^{-1}mol^{-1}

temperature_air = 295.0 # degrees Kelvin

amount_of_substance = (pressure_air * volume_torus) / (ideal_gas_constant * temperature_air)

# mass_plasma_total = 

print("volume_torus =           {}".format(volume_torus))

print("amount_of_substance =    {}".format(amount_of_substance))

print("amount_of_substance =    {}".format(amount_of_substance))
