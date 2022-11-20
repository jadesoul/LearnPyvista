import pyvista as pv
import numpy as np

def make_points():
    """Helper to make XYZ points"""
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    return np.column_stack((x, y, z))

points = make_points()

def polyline_from_points(points):
    poly = pv.PolyData()
    poly.points = points
    the_cell = np.arange(0, len(points), dtype=np.int)
    the_cell = np.insert(the_cell, 0, len(points))
    poly.lines = the_cell
    return poly

polyline = polyline_from_points(points)
polyline["scalars"] = np.arange(polyline.n_points)
tube = polyline.tube(radius=0.1)
tube.plot(smooth_shading=True)


# Create spline with 1000 interpolation points
spline = pv.Spline(points, 1000)

# add scalars to spline and plot it
spline["scalars"] = np.arange(spline.n_points)
tube = spline.tube(radius=0.1)
tube.plot(smooth_shading=True)





# generate same spline with 400 interpolation points
spline = pv.Spline(points, 400)

# plot without scalars
spline.plot(line_width=4, color="k")