import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [2, 4, 6]
y = [3, 6, 9]

x2 = [1, 3, 5]
y2 = [2, 4, 6]

plt.plot(x, y, 'g', label='line one', linewidth=5)
plt.plot(x2, y2, 'c', label='line two', linewidth=5)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()

plt.show()