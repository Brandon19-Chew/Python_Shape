# CODE OF OBJECTS 

# 💻 The Logic Flow ( Donut )

1. np.linspace & np.meshgrid: These functions create a grid of points. Think of this like creating a flexible mesh "skin" that will be wrapped around the donut frame.
2. ax.plot_surface: This takes the calculated $x, y, z$ points and stretches the "skin" over them. The cmap='viridis' argument gives it that purple-to-yellow gradient color.
3. ax.set_xlim/ylim/zlim: This is a crucial step. Without it, Matplotlib might stretch one axis more than the others, making your donut look like a squashed pancake or a tall cylinder.

# 🔢 Donut Formula 

x = ( R + r cos ϕ ) cos ϕ
y = ( R + r cos ϕ ) sin ϕ
z = r sin θ

# 🛠️ Summary of Libraries 

1. NumPy: Handles the heavy lifting of trigonometry and large arrays of numbers.
2. Matplotlib: The engine that draws the window and the 3D axes.
3. mplot3d: A specific toolkit within Matplotlib that allows the plot to exist in 3D space rather than just 2D.
   
================================================================================================================================================================================================

# 💻 The Logic Flow ( Cube )

A cube has 8 corners. The script defines these using an array of $(x, y, z)$ coordinates.
To keep the cube perfectly centered at the origin $(0, 0, 0)$, the code uses half_side. If your side length is 2, the coordinates range from -1 to 1.

 * Bottom corners: $z$ is negative (-half_side).
 * Top corners: $z$ is positive (+half_side).


# 📐 2. Defining the Faces ( The Mesh )

Once the corners (dots) are placed, the computer needs to know how to "skin" them to create surfaces. This is done by grouping indices:

 * Faces list: This tells Python which four vertices connect to form a square. For example, [0, 1, 2, 3] connects the four bottom corners to create the floor of the cube.
 * Order matters: The vertices are listed in a specific order (usually counter-clockwise) so the computer knows which way the "face" is pointing.

# 🎨 3. Rendering with Poly3DCollection

This is the most important part of the code for drawing solid shapes:

 * Poly3DCollection: Unlike the donut's plot_surface (which works on a mathematical grid), this function is designed to take a list of custom polygons and turn them into a 3D object.
   
 * Aesthetics: * facecolors='cyan': Fills the squares with color.
   
     - edgecolors='r': Draws red lines on the edges so you can see the cube's skeleton.
     - alpha=0.6: Makes it slightly see-through, which is helpful in 3D so you can see the back edges through the front.

================================================================================================================================================================================================

# 💻 The Logic Flow ( Ball )

To map out every point on a sphere, the code uses two angles, similar to Longitude and Latitude on a map:

 * u (Azimuthal angle): Think of this as Longitude. It sweeps around the "equator" from 0 to 2π (360∘).
 * v (Polar angle): Think of this as Latitude. It sweeps from the North Pole (0) down to the South Pole ( π or 180∘).

# 📐 2. The Math Behind the Curve 

The script converts these two angles into 3D $(x, y, z)$ coordinates using the following parametric equations:

x = r . cos (u) . sin (v) 
y = r . sin (u) . sin (v) 
z = r . cos (u)

By multiplying everything by the Radius ($r$), you control how big the ball is. If the radius is $1$, it’s a "Unit Sphere."

# 🛠️ 3. How the Code Renders It

1. np.meshgrid(u, v): This creates a coordinate grid. Imagine taking a flat piece of graph paper and preparing to wrap it around a ball.
2. ax.plot_surface: This function takes that "graph paper" grid and stretches it over the $(x, y, z)$ coordinates calculated above.
3. cmap='plasma': This gives the sphere its color. "Plasma" is a vibrant color map that transitions from dark purple to bright yellow/orange.
4. Aspect Ratio: Just like your previous shapes, ax.set_xlim, ylim, and zlim are set to be equal. Without this, your sphere might look like an egg or a flattened pill.












