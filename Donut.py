import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Required for 3D projection

def plot_donut_shape(R: float = 2.0, r: float = 1.0):
    """
    Generates and plots a 3D donut (torus) shape.

    Args:
        R (float): The major radius of the torus (distance from the center of the hole
                   to the center of the tube). Default is 2.0.
        r (float): The minor radius of the torus (radius of the tube itself).
                   Default is 1.0.
    """
    if r >= R:
        print("Error: Minor radius (r) must be less than major radius (R) to form a proper donut.")
        return

    # Create parameter arrays for the torus (angles phi and theta)
    # phi goes from 0 to 2*pi, sweeping around the major circle
    # theta goes from 0 to 2*pi, sweeping around the minor circle (the tube itself)
    phi = np.linspace(0, 2 * np.pi, 100)  # Major angle (around the donut hole)
    theta = np.linspace(0, 2 * np.pi, 100) # Minor angle (around the tube itself)

    # Create 2D grids for phi and theta using np.meshgrid
    # This allows us to apply the equations to all combinations of phi and theta
    phi, theta = np.meshgrid(phi, theta)

    # Parametric equations for a torus:
    # x = (R + r * cos(theta)) * cos(phi)
    # y = (R + r * cos(theta)) * sin(phi)
    # z = r * sin(theta)
    x = (R + r * np.cos(theta)) * np.cos(phi)
    y = (R + r * np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)

    # Create a new figure and a 3D subplot
    fig = plt.figure(figsize=(8, 8)) # Set figure size for better visualization
    ax = fig.add_subplot(111, projection='3d') # Add a 3D subplot

    # Plot the surface of the donut
    # cmap='viridis' sets the color map for the surface
    # alpha=0.9 sets the transparency of the surface
    ax.plot_surface(x, y, z, cmap='viridis', alpha=0.9)

    # Set labels for the axes
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Set title for the plot
    ax.set_title(f'3D Donut (Torus) Shape (R={R}, r={r})')

    # Ensure equal aspect ratio for a proper spherical/toroidal appearance
    # This is important so the donut doesn't look stretched.
    # We calculate the limits based on the radii.
    max_dim = R + r
    min_dim = -(R + r)
    ax.set_xlim([min_dim, max_dim])
    ax.set_ylim([min_dim, max_dim])
    ax.set_zlim([min_dim, max_dim])

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # You can call the function with default radii
    plot_donut_shape()

    # Or you can experiment with different radii
    # plot_donut_shape(R=3.0, r=0.8)
    # plot_donut_shape(R=1.5, r=0.5)
