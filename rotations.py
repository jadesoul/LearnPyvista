import pyvista as pv
from pyvista import examples
import time


# Define camera and axes. Setting axes origin to ``(3.0, 3.0, 3.0)``.

mesh = pv.Cube((5, 5, 5), 10, 10, 10)
mesh2 = pv.Cube((-5, -5, -5), 10, 10, 10)
# mesh = examples.load_ant()
# mesh.points /= 10  # scale the mesh

camera = pv.Camera()
camera.position = (30.0, 10.0, 10.0)
camera.focal_point = (5.0, 5.0, 5.0)


axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
# axes.origin = (3.0, 3.0, 3.0)
axes.origin = (0, 0, 0)

# Plot original mesh. Add axes actor to Plotter.

p = pv.Plotter()

p.add_text("Mesh", font_size=24)
p.add_actor(axes.actor)
p.camera = camera
p.add_mesh(mesh)
# p.add_mesh(mesh2)
p.show_grid()
p.show_axes()
p.show(window_size=[2000, 2000], interactive_update=True)

import os, threading; print(os.getppid(), os.getpid(), threading.currentThread().ident)

for i in range(10000):
    camera.Azimuth(5)
    mesh.rotate_x(45 * i, point=axes.origin, inplace=False)
    p.update(10)
    time.sleep(0.001)
    

p.close()





