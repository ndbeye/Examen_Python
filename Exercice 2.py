import matplotlib.pyplot as plt
import numpy as np

class Curve:
    def __init__(self, start, stop, nbr_points = 5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points

    def _calculate_y(self, x):
        return x**5

    def plot_curve(self):
        t_curve = np.linspace(self.start, self.stop, self.nbr_points)
        x_curve = t_curve
        y_curve = self._calculate_y(t_curve)

        plt.plot(x_curve, y_curve, label='Courbe $x^5$')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Courbe $x^5$')
        plt.grid(True)
        plt.legend()
        plt.show()

    def point_position(self, x, y):
        curve_y = self._calculate_y(x)
        if y > curve_y:
            return "Above"
        elif y < curve_y:
            return "Below"
        else:
            return "Sur la courbe"

    def generate_points(self):
        t_points = np.linspace(self.start, self.stop, self.nbr_points)
        x_points = t_points
        y_points = self._calculate_y(t_points)

        plt.plot(x_points, y_points, label='Courbe $x^5$')
        for x, y in zip(x_points, y_points):
            if y > self._calculate_y(x):
                plt.plot(x, y, 'bx')
            else:
                plt.plot(x, y, 'go')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Courbe $x^5$ avec Points')
        plt.grid(True)
        plt.legend()
        plt.show()

    def calculate_areas(self):
        dx = (self.stop - self.start) / self.nbr_points
        x_values = np.linspace(self.start, self.stop, self.nbr_points)
        y_values = self._calculate_y(x_values)

        area_blue = sum(y_values[i] * dx for i in range(self.nbr_points) if y_values[i] > self._calculate_y(x_values[i]))
        area_green = sum(y_values[i] * dx for i in range(self.nbr_points) if y_values[i] <= self._calculate_y(x_values[i]))

        return area_blue, area_green
