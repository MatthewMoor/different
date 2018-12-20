import matplotlib.pyplot as plt
from random import randint
import random as rd

x = (1, 2, 3)
y = (0, 3, 0)

for dot in range(3):
	plt.scatter(x, y)

dice = rd.randrange(1, 7)
X = rd.randrange(1, 4)
Y = rd.randrange(1, 4)
initial = rd.randrange(X, Y)
plt.scatter(initial)
plt.show()
#if dice == 1 or dice == 2:
	
