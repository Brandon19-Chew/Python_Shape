import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Required for 3D projection

def plot_ball_shape(radius: float = 1.0):
    """
    Generates and plots a 3D ball (sphere) shape.A

    Args:
        radius (float): The radius of the sphere. Default is 1.0.
    """
    if radius <= 0:
        print("Error: Radius must be a positive value.")
        return

    # Create parameter arrays for the sphere (angles u and v)
    # u (azimuthal angle) sweeps around the equator, from 0 to 2*pi
    # v (polar angle) sweeps from pole to pole, from 0 to pi
    u = np.linspace(0, 2 * np.pi, 100) # Azimuthal angle
    v = np.linspace(0, np.pi, 100)    # Polar angle

    # Create 2D grids for u and v using np.meshgrid
    # This allows us to apply the equations to all combinations of u and v
    u, v = np.meshgrid(u, v)

    # Parametric equations for a sphere:
    # x = radius * cos(u) * sin(v)
    # y = radius * sin(u) * sin(v)
    # z = radius * cos(v)
    x = radius * np.cos(u) * np.sin(v)
    y = radius * np.sin(u) * np.sin(v)
    z = radius * np.cos(v)

    # Create a new figure and a 3D subplot
    fig = plt.figure(figsize=(8, 8)) # Set figure size for better visualization
    ax = fig.add_subplot(111, projection='3d') # Add a 3D subplot

    # Plot the surface of the sphere
    # cmap='plasma' sets the color map for the surface
    # alpha=0.8 sets the transparency of the surface
    ax.plot_surface(x, y, z, cmap='plasma', alpha=0.8)

    # Set labels for the axes
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Set title for the plot
    ax.set_title(f'3D Ball (Sphere) Shape (Radius = {radius})')

    # Ensure equal aspect ratio for a proper spherical appearance
    # This is important so the sphere doesn't look stretched.
    # We set limits based on the radius.
    max_dim = radius * 1.2 # Add a little padding to the limits
    min_dim = -radius * 1.2
    ax.set_xlim([min_dim, max_dim])
    ax.set_ylim([min_dim, max_dim])
    ax.set_zlim([min_dim, max_dim])

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # You can call the function with the default radius
    plot_ball_shape()

    # Or you can experiment with different radii
    # plot_ball_shape(radius=2.5)
    # plot_ball_shape(radius=0.7)
