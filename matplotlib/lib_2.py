import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()
lag = 0.1
x = np.arange(0.0, 2*np.pi+lag, lag)
y = np.cos(x)

plt.plot(x, y)

plt.text(0, 0, '3 yaxis', fontsize = 26, rotation = 90)
plt.text(2.75, 0, '1 Axes' fontsize = 30)
plt.show()