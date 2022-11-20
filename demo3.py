import pyvista as pv
import pyvistaqt as pvqt
from pyvista import examples
import numpy as np

# Load example beam grid
grid = pv.UnstructuredGrid(examples.hexbeamfile)

# Create fictitious displacements as a function of Z location
d = np.zeros_like(grid.points)
d[:, 1] = grid.points[:, 2]**3/100


cpos = [(11.915126303095157, 6.11392754955802, 3.6124956735471914),
        (0.0, 0.375, 2.0),
        (-0.42546442225230097, 0.9024244135964158, -0.06789847673314177)]

plotter = pvqt.BackgroundPlotter(show = True)
plotter.add_mesh(grid, scalars=d[:, 1], scalar_bar_args={'title': 'Y Displacement'}, show_edges=True,
              rng=[-d.max(), d.max()], interpolate_before_map=True)
plotter.add_axes()
plotter.camera_position = cpos

def update():
    grid.points += d
    for phase in np.linspace(0, 2*np.pi, 5):
        grid.points += d*np.cos(phase)
        plotter.update()
        
plotter.add_callback(update, interval=100)

pv.Plotter().show()

