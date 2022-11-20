import pyvista as pv
import numpy as np

# mesh points
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0.5, 0.5, -1]])

# mesh faces,这个还不知道是什么意思，怎么定义？
faces = np.hstack([[4, 0, 1, 2, 3],  # square
                   [3, 0, 1, 4],     # triangle
                   [3, 1, 2, 4]])    # triangle

surf = pv.PolyData(vertices, faces)
surf.cell_arrays['scalars'] = np.arange(3)
# plot each face with a different color
# surf.plot(scalars=np.arange(3), cpos=[-1, 1, 0.5])

p = pv.Plotter() ## 建一个普通画板
# p = pv.BackgroundPlotter() ## 建一个交互式画板
p.camera_position = [-1, 1, 0.5]
p.add_mesh(surf)
p.show()