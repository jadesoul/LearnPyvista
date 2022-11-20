import pyvista as pv
from pyvista import examples

# mesh=examples.load_ant()
mesh=examples.load_hexbeam()

print(mesh)

p=pv.Plotter()
p.add_mesh(mesh)
p.show()
