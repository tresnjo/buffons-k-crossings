import matplotlib.pyplot as plt
import numpy as np
import random as random
import math

# params
no_of_needles = 10000
l = 10.0
d = 2.0

# maximum number of crossings (0, 1, ..., m-1)
m = math.floor(l/d + 1)

# horizontal lines
ys = np.arange(d, m*d, d)
# list for storing crossings during needle dropping
crossings = np.zeros(m)

plt.figure(1)
# plot of parallell lines with distance 1 between
for i in range(0,m+1):
    plt.axhline(i*d, color = 'black')

# random color generator for plotting
def generate_random_colors(m):
    # Generate m random colors in the form of (R, G, B) tuples
    colors = [(random.random(), random.random(), random.random()) for _ in range(m)]
    return colors

colors = generate_random_colors(len(crossings))

# needle dropping loop
for i in range(no_of_needles):

    # randomly distributed number of position y in range [0, 1/2]
    y = random.uniform(0, d)
    # randomly distributed angles in range [0, pi/2]
    theta = random.uniform(0, np.pi/2)
    x_coords = [0, l * np.cos(theta)]
    y_coords = [y, y + l * np.sin(theta)]

    # creating a list starting for thetas of intersect ranging from 0 to pi/2
    y_ns = np.insert(ys,0,y)
    theta_ns = np.arcsin((y_ns - y) / l)

    #calculate no of crossings
    theta_ns_new = theta_ns.searchsorted(theta)
    no_of_crossings = theta_ns_new-1 

    # make a list of no_of_crossings for a single needle and store in list for plotting at end
    crossings[no_of_crossings] += 1

    # plotting the needle
    plt.plot(x_coords, y_coords, color = colors[no_of_crossings], label = no_of_crossings)

# creating legend without duplicate labels
def legend_without_duplicate_labels(figure):
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    figure.legend(by_label.values(), by_label.keys(), loc='lower right')


legend_without_duplicate_labels(plt.gcf())

# plotting the results
plt.title('Needle orientation and positions colored by no of crossings')
plt.figure(2)

# scatter plot of crossings
plt.scatter(np.arange(0,len(crossings)), crossings/no_of_needles, color = 'black', marker = 'o')
plt.plot(np.arange(0,len(crossings)), crossings/no_of_needles, color = 'red')
plt.title(r'Histogram of crossings')
plt.grid(True)
plt.show()
