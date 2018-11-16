import matplotlib.pyplot as plt

figure = plt.figure() # Create object figure
print(figure.axes) # list area drawing empty
plt.scatter(1.0, 1.0) # method for applying marmarker in  dot
plt.show()
plt.savefig('figure\example 0321.png', fmt = 'png')


figure = plt.figure()

ax = figure.add_axes([0, 0, 1, 1], polar = True)
plt.scatter(0.0, 0.5)
plt.savefig('figure\example 0321b.png', fmt = 'png')
plt.show()

