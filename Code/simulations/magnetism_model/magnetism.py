"""
magnetism.py

:author: Pavlo Vlastos
"""
import numpy as np

class Magnetism:
    def __init__(self):
        self.F_sum = np.zeros((3,1))

    def calculate_B(self):
        """
        """