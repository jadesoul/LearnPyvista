import pyvista as pv
import pyvistaqt as pvqt
import numpy as np
import time

cmap='viridis'    
nx,ny,nz = 60, 40, 42
nc = nx*ny*nz

np.random.seed(0)
inidata = np.random.randint(1, 100, nc)

# generate random data for updating
data = [np.random.randint(1, 1000, nc), 
        np.random.randint(1, 1e4, nc),
        np.random.randint(1, 1e5, nc),
        np.random.randint(1, 1e6, nc)]

gridata = np.ones((nx,ny,nz))

mesh = pv.UniformGrid()
mesh.dimensions = np.array(gridata.shape) + 1 


mesh.origin = (0, 0, 0)  # The bottom left corner of the data set
mesh.spacing = (30, 30, 2.5)  # These are the cell sizes along each axis

mesh.cell_arrays["Data"] = inidata

plotter = pvqt.BackgroundPlotter()

# Add slices
xslice = mesh.slice(normal='x')
yslice = mesh.slice(normal='y')
zslice = mesh.slice(normal='z')
rslice = mesh.slice(normal=[1,1,0])

# Plot
plotter.add_mesh(mesh.outline(), color="k")
plotter.add_mesh(xslice, cmap=cmap)
plotter.add_mesh(yslice, cmap=cmap)
plotter.add_mesh(zslice, cmap=cmap)
plotter.add_mesh(rslice, cmap=cmap)

def update():
    for dat in data:
        plotter.update_scalars(dat, mesh=mesh)
        # time.sleep(1)
        plotter.update()
        
plotter.add_callback(update, interval=100)

pv.Plotter().show()