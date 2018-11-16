import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 41)
y = x**2

function = plt.plot(x, y, 'r-');
plt.show(plt.grid(function))

# another schedule
t = np.linspace(0., 4 * np.pi, 101)
f = np.sin(t) + 3
schedule = plt.plot(t, f)

plt.axhline(3, color = 'lightgray', linestyle = '--')
plt.text(10.5, 3.05, 'Среднее')
plt.annotate('Local\nminimum', xy = (3*np.pi / 2, 2), 
             xytext = (3.7, 2.7),
             arrowprops = dict(arrowstyle = "->", color = 'red'));
plt.show()
