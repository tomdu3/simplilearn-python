# plotting library
# 1. correlation analysis of variables
# 2. visualize 95% confidence intervals of the models
# 3. outlier detection

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')

plt.show()