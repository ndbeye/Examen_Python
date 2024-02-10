import matplotlib.pyplot as plt
import numpy as np

# Paramétres de la courbe x^5
tab_courbe = np.linspace(0, 1, 1000)
x_courbe = tab_courbe
y_courbe = tab_courbe**5

# Paramétrisation du carré
tab_square = np.linspace(0, 1, 5)
x_square = tab_square
y_square = tab_square

# Tracer la courbe et le carré
plt.plot(x_courbe, y_courbe, label='Courbe $x^5$')
plt.plot(x_square, y_square, 'ro-', label='Carré')
plt.fill_between(x_courbe, y_courbe, color='blue', alpha=0.3, where=(y_courbe > y_square))
plt.fill_between(x_courbe, y_courbe, color='green', alpha=0.3, where=(y_courbe <= y_square))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Courbe $x^5$ et Carré')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
