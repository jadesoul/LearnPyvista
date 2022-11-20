import pyvista as pv
from pyvista import examples
import numpy as np

x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x ** 2 + y ** 2)
z = np.sin(r)

grid = pv.StructuredGrid(x, y, z)

print(grid.points)
grid.plot()

# Plot mean curvature as well
grid.plot_curvature(clim=[-1, 1])

