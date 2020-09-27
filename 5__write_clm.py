from vedo import Points, show, printc, Glyph, Cube, Box
from vedo import buildAxes, Text2D, Volume, Video, settings
from heart_database import dataset_wt, dataset_ko, grid_res, radius_res
import numpy as np
import pyshtools

dset = dataset_wt # the db that we want to fill now
vd = Video('step5.mp4', duration=16)

# For each group of hearts
for hset in dset.keys():
    if not hset.startswith('set'): continue
    printc('Processing group of hearts:', hset, c='y', invert=1)

    # For each heart
    for h in dset[hset]['files']:
        printc('\t..processing heart:', h)
        vpts = Points(h+'_rays.vtk')
        pts = vpts.points()
        arr = vpts.getPointArray('input_scalars')
        Mpts = pts.reshape(radius_res, grid_res*2*grid_res, 3)
        Marr = arr.reshape(radius_res, grid_res * 2*grid_res) #theta*phi resolution
        dset['ray_points'] = Marr

        if 'ko_1' in h: # prepare for later plotting
            vh = Volume(h+'.vti').isosurface(90).extractLargestRegion().normalize()
            s2d = vh.clone2D(pos=[.02,.77], coordsys=3, c='k', alpha=.2, scale=.15)
            cube = Cube().clean()

        # For each ray (or "shell")
        hclm = []
        for rn in range(radius_res):
            ptsn = Mpts[rn,:,:]
            arrn = Marr[rn,:]
            grid = pyshtools.SHGrid.from_array(arrn.reshape(grid_res, 2*grid_res))
            clm = grid.expand().to_array()
            hclm.append(clm)

            if 'ko_1' in h: # do some plotting
                cpts,zs=[],[]
                for x in range(int(grid_res/2)):
                    for y in range(int(grid_res/2)):
                        z0 = clm[0][x][y]/10
                        z1 = clm[1][x][y]/10
                        cpts.append([x,  y, abs(z0)])
                        cpts.append([x, -y, abs(z1)])
                        zs.extend([z0,z1])
                cpts = np.array(cpts)
                zs = np.sqrt(np.abs(np.array(zs)))
                pvals = Points(cpts).addPointArray(zs, 'clm')
                cvals = Glyph(pvals, cube, scaleByScalar=True).cmap('jet', vmin=0, vmax=2)
                ax = buildAxes(xrange=[0,grid_res/2], yrange=[-25,25], zrange=[0,0],
                               xtitle='l', ytitle='m', ztitle='C_lm')
                tf = Text2D(h.split('/')[-1], pos=(0.01,0.73), s=0.9, c='k')
                tr = Text2D('radius = ' + str(rn), pos='bottom-left', s=1.25)
                shell_pts = Points(ptsn).cmap('jet', arrn).scale(0.1).addPos(-15,0,0)
                bx = Box(size=(25,50,25), pos=(-15,0,0), alpha=0).wireframe()
                plt = show(cvals, ax, tf, tr, shell_pts, bx, s2d,
                           "Stage: "+hset.replace('set',''),
                           zoom=1.25, interactive=0, size=(1000,1000))
                vd.addFrame()
                plt.clear()
                break
        dset[hset]['clms'].append(np.array(hclm))
    dset[hset]['clms'] = np.array(dset[hset]['clms'])

vd.close()
np.save('clm_data.npy', np.array(dset), allow_pickle=True)
printc('Saved clm_data.npy Move it to data_path',
       'manually (add _wt_ or _ko_)', box='-')
# eg: mv clm_data.npy data/wt/clm_wt_data.npy

