import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Define constants
k_max = 10
k_min = 1
k_p = 100
x_max = 10
x_p = 100

# Define the function I(x, k)
def I(x, k):
    return 2/np.pi * ((k+1)*x**(-1)*np.arcsin((k+1)*x**(-1))
                      - k*x**(-1)*np.arcsin(k*x**(-1))
                      + np.sqrt(1-(k+1)**2*x**(-2))
                      - np.sqrt(1-k**2*x**(-2)))

# Define the function pr()
def pr():
    # Generate x and k values
    x_values = np.linspace(k_min, x_max, x_p)
    k_values = np.linspace(k_min, k_max, k_p)
    
    # Initialize result array
    pr_result = np.zeros((len(k_values), len(x_values)))  
    
    # Compute pr_result
    for i, k in enumerate(k_values):
        for j, x in enumerate(x_values):
            pr_result[i, j] = I(x, k) - I(x, k - 1)
    
    return pr_result

# Compute prbs
prbs = pr()

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface P(x, k)
x_values, k_values = np.meshgrid(np.linspace(k_min, x_max, x_p), np.linspace(k_min, k_max, k_p))
surf = ax.plot_surface(x_values, k_values, prbs, cmap='viridis')
fig.colorbar(surf)

# Set labels and title for the main surface plot
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$k$')
ax.set_zlabel(r'$P$')
ax.set_title(r'$P(x,k)$')

# Plot the plane k = x - 1
x_values, z_values = np.meshgrid(np.linspace(k_min, x_max, x_p), np.linspace(0, np.max(prbs), 100))
y = x_values - 1
ax.plot_surface(x_values, y, z_values, color='blue', alpha=0.1)

# Add label for the plane
ax.text((k_min + x_max) / 2, (k_min + k_max) / 2, 0.5, r"$k=x-1$", color='red')

# Show the plot
plt.show()
