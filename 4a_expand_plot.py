from vedo import Points, show, spher2cart, printc
from scipy.interpolate import griddata
import pyshtools
import numpy as np
import heart_database as hdb

lmax=24

vpts = Points(hdb.data_path_wt + 'LQR_M_JJ_1819_wt_3_rays.vtk')

pts = vpts.points()
arr = vpts.getPointArray('input_scalars')
Mpts = pts.reshape(hdb.radius_res, hdb.grid_res*2*hdb.grid_res, 3)
Marr = arr.reshape(hdb.radius_res, hdb.grid_res*2*hdb.grid_res)

rn = 28
ptsn = Mpts[rn,:,:]
arrn = Marr[rn,:]

grid = pyshtools.SHGrid.from_array(arrn.reshape(hdb.grid_res, 2*hdb.grid_res))

clm = grid.expand()
printc('\ngrid\n', grid, c='t')
printc('\nclm\n', clm, c='v')
grid_reco = clm.expand(lmax=lmax).to_array()  # cut "high frequency" components


#############################################################
# interpolate to a finer grid
ll = []
for i, long in enumerate(np.linspace(0, 360, num=grid_reco.shape[1], endpoint=True)):
    for j, lat in enumerate(np.linspace(90, -90, num=grid_reco.shape[0], endpoint=True)):
        th = np.deg2rad(90 - lat)
        ph = np.deg2rad(long)
        p = spher2cart(grid_reco[j][i], th, ph)
        ll.append((lat, long))

radii = grid_reco.T.ravel()
n = 200j
lnmin, lnmax = np.array(ll).min(axis=0), np.array(ll).max(axis=0)
grid = np.mgrid[lnmax[0]:lnmin[0]:n, lnmin[1]:lnmax[1]:n]
grid_x, grid_y = grid
grid_reco_finer = griddata(ll, radii, (grid_x, grid_y), method='cubic')

pts2 = []
for i, long in enumerate(np.linspace(0, 360, num=grid_reco_finer.shape[1], endpoint=False)):
    for j, lat in enumerate(np.linspace(90, -90, num=grid_reco_finer.shape[0], endpoint=True)):
        th = np.deg2rad(90 - lat)
        ph = np.deg2rad(long)
        r= np.sqrt(grid_reco_finer[j][i]+10) ##### NOTE !!! sqrt(..+10) only for better viz
        p = spher2cart(r, th, ph)
        pts2.append(p)

mesh2 = Points(pts2, r=5, c="r", alpha=0.5)

vmypts = Points(ptsn, r=10).cmap('jet', arrn)
vmypts.addScalarBar3D(title='scalar for r='+str(rn))

show(vmypts, at=0, N=2, axes=1, sharecam=0)
show(mesh2, 'Spherical harmonics\nexpansion of order '+str(lmax),
     at=1, axes=12, interactive=True)

