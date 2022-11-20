import pyvista as pv
from pyvistaqt import BackgroundPlotter
plotter = BackgroundPlotter()
_ = plotter.add_mesh(pv.Sphere())
# plotter.show()


import pyvista as pv
p=pv.Plotter()
p.show()