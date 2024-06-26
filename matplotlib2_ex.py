import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)

N=30
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi*(15*np.random.rand(N))**2
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()