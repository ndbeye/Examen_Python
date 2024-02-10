import matplotlib.pyplot as plt
import numpy as np

class Curve:
    def __init__(self, start, stop, nbr_points=5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points
