import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Required for 3D projection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection # For plotting 3D polygons

def plot_cube_shape(side_length: float = 2.0):
    """
    Generates and plots a 3D cube shape.

    Args:
        side_length (float): The length of each side of the cube. Default is 2.0.
    """
    if side_length <= 0:
        print("Error: Side length must be a positive value.")
        return

    # Calculate half_side for easier vertex definition centered at origin
    half_side = side_length / 2.0

    # Define the 8 vertices of a cube
    # Each vertex is a list [x, y, z]
    vertices = np.array([
        [-half_side, -half_side, -half_side],  # 0: ---
        [ half_side, -half_side, -half_side],  # 1: +--
        [ half_side,  half_side, -half_side],  # 2: ++-
        [-half_side,  half_side, -half_side],  # 3: -+-
        [-half_side, -half_side,  half_side],  # 4: --+
        [ half_side, -half_side,  half_side],  # 5: +-+
        [ half_side,  half_side,  half_side],  # 6: +++
        [-half_side,  half_side,  half_side]   # 7: -++
    ])

    # Define the 6 faces of the cube using indices of the vertices
    # Each face is defined by 4 vertices in a specific order
    faces = [
        [0, 1, 2, 3], # Bottom face
        [4, 5, 6, 7], # Top face
        [0, 1, 5, 4], # Front face
        [2, 3, 7, 6], # Back face
        [1, 2, 6, 5], # Right face
        [0, 3, 7, 4]  # Left face
    ]

    # Create a new figure and a 3D subplot
    fig = plt.figure(figsize=(8, 8)) # Set figure size for better visualization
    ax = fig.add_subplot(111, projection='3d') # Add a 3D subplot

    # Prepare the faces for Poly3DCollection
    # We need a list of arrays, where each array contains the coordinates of the vertices for one face.
    face_coords = [vertices[face_indices] for face_indices in faces]

    # Create a Poly3DCollection object from the cube's faces
    # facecolors: sets the color of each face (can be a list of colors or a single color)
    # linewidths: sets the width of the lines drawing the edges
    # edgecolors: sets the color of the edges
    # alpha: sets the transparency
    cube_faces = Poly3DCollection(face_coords, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.6)

    # Add the collection of faces to the 3D plot
    ax.add_collection3d(cube_faces)

    # Set labels for the axes
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Set title for the plot
    ax.set_title(f'3D Cube Shape (Side Length = {side_length})')

    # Ensure equal aspect ratio for a proper cubic appearance
    # This prevents the cube from looking squashed or stretched.
    # We set limits based on the side length.
    max_dim = half_side * 1.5 # Add a little padding to the limits
    min_dim = -half_side * 1.5
    ax.set_xlim([min_dim, max_dim])
    ax.set_ylim([min_dim, max_dim])
    ax.set_zlim([min_dim, max_dim])

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # You can call the function with the default side length
    plot_cube_shape()

    # Or you can experiment with different side lengths
    # plot_cube_shape(side_length=3.5)
    # plot_cube_shape(side_length=1.0)
