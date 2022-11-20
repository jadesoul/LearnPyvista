from threading import Thread
import time
import numpy as np
import pyvista as pv
import pyvistaqt as pvqt
from pyvista import examples

# import os
# os.environ['QT_DEVICE_PIXEL_RATIO']='4'

globe = examples.load_globe()

globe.point_data['scalars'] = np.random.rand(globe.n_points)
globe.set_active_scalars('scalars')


# p = pvqt.BackgroundPlotter(line_smoothing=True, point_smoothing=True, polygon_smoothing=True, window_size=(1000, 800), editor=False)
plotter = pvqt.BackgroundPlotter()
plotter.add_mesh(globe, lighting=False, show_edges=True, texture=True, scalars='scalars')
plotter.view_isometric()

# shrink globe in the background
def shrink():
    for i in range(50):
        globe.points *= 0.99
        # Update scalars
        globe.point_data['scalars'] = np.random.rand(globe.n_points)
        time.sleep(0.05)

thread = Thread(target=shrink)
thread.start()


pv.Plotter().show()
