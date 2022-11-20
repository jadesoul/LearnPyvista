import pyvista as pv
import pyvistaqt as pvqt
from pyvista import examples
import time

mesh=examples.load_globe()

p = pvqt.BackgroundPlotter()
p.add_mesh(mesh)
p.show_bounds(grid=not True, location='back')
p.view_isometric()

begin=time.time()
cnt=0
def update():
    global cnt
    # print(cnt)
    cnt+=1
    p.camera.Azimuth(0.1)
    p.update()
    if cnt%100==0:
        end=time.time()
        print(f'Frame={cnt}, Time={end-begin:.2f}s, FPS={cnt/(end-begin):.2f}')

p.add_callback(update, 1)

pv.Plotter().show(window_size=[1,1])
