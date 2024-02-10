import matplotlib.pyplot as plt
import numpy as np

# Paramétres de la courbe x^5
tab_courbe = np.linspace(0, 1, 1000)
x_courbe = tab_courbe
y_courbe = tab_courbe**5

# Tracer la courbe et le carré
plt.plot(x_courbe, y_courbe, label='Courbe $x^5$')
plt.plot(x_square, y_square, 'ro-', label='Carré')
plt.fill_between(x_courbe, y_courbe, color='blue', alpha=0.3, where=(y_courbe > y_square))
plt.fill_between(x_courbe, y_courbe, color='green', alpha=0.3, where=(y_courbe <= y_square))
plt.xlabel('x')
plt.ylabel('y')
plt.title(' Courbe d’équation x⁵ sur l’intervalle [0;1]')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
