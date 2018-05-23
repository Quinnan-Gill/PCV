import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(size = 1000)
plt.hist(x, normed=True, bins=30)
plt.ylabel('Probability');
plt.show()
