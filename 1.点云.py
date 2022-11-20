import pyvista as pv
import numpy as np

## 生成一组点云的坐标，然后构建点云的mesh
points = np.random.rand(30000, 3)
point_cloud = pv.PolyData(points)
print(np.allclose(points, point_cloud.points))#检测是否一致
# 画点云
# point_cloud.plot(eye_dome_lighting=True)


## 给点云赋值，这里就把z轴坐标的值赋值给点云
data = points[:,-1]
point_cloud["value"] = data
point_cloud.plot(render_points_as_spheres=True)
