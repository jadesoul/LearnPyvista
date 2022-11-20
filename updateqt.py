import pyvista as pv
import pyvistaqt as pvqt
from pyvista import examples



mesh=examples.load_airplane()

p = pvqt.BackgroundPlotter()
p.add_mesh(mesh)
p.show_bounds(grid=not True, location='back')
p.view_isometric()

cnt=0
def update():
    global cnt
    print(cnt)
    cnt+=1
    p.camera.Azimuth(0.1)
    p.update()

p.add_callback(update, 1)

pv.Plotter().show(window_size=[1,1])

