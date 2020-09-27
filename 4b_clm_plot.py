from vedo import Points, show, Glyph, Cube
import pyshtools, heart_database as hdb
import numpy as np

dpath = hdb.data_path_wt

vpts = Points(dpath+'LQR_M_JJ_1819_wt_1_rays.vtk')
rn = 28 # choose the radius shell

pts = vpts.points()
arr = vpts.getPointArray('input_scalars')
Mpts = pts.reshape(hdb.radius_res, hdb.grid_res*2*hdb.grid_res, 3)
Marr = arr.reshape(hdb.radius_res, hdb.grid_res*2*hdb.grid_res)

ptsn = Mpts[rn,:,:]
arrn = Marr[rn,:]

grid = pyshtools.SHGrid.from_array(arrn.reshape(hdb.grid_res, 2*hdb.grid_res))

clm = grid.expand()
carr = clm.to_array()

cpts, zs = [], []
for x in range(25):
    for y in range(25):
        z0 = carr[0][x][y]/10
        z1 = carr[1][x][y]/10
        if z0:
            cpts.append([x, y, z0])
            zs.append(z0)
        if z1:
            cpts.append([x, -y, z1])
            zs.append(z1)
cpts = np.array(cpts)
zs = np.power(np.abs(np.array(zs)), 1/3)

pvals = Points(cpts).addPointArray(zs, 'clm')
cvals = Glyph(pvals, Cube().scale([1,1,1]), scaleByScalar=True).cmap('rainbow')
cvals.lighting('ambient', diffuse=0.2)
cvals.addScalarBar3D(title="|C_lm | [arb.units]",c='w').addPos(2,0,0)
show(cvals,
     bg='bb',
     axes=dict(xrange=(0,25), xtitle='l', ytitle='m', ztitle='C_lm', yHighlightZero=1))


