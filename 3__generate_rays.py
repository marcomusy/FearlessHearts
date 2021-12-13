from vedo import spher2cart, Volume, loadTransform, settings
from vedo import Point, Points, printc, closePlotter, ask
import heart_database as hdb
import numpy as np

ask('this needs lots of memory - close unnecessary apps before running it',
    'then press return')

dpath = hdb.data_path_wt
dataset = hdb.dataset_wt
refheart = 'LQR_M_JJ_1819_wt_2.vti'  # ->THE SACRED REF for wt
# refheart= 'LQR_M_JJ_1819_ko_3.vti' # ->THE SACRED REF for KO

vref = Volume(dpath+refheart)
vref_center = Point(vref.center(), c='g', alpha=0.6, r=20)
C = vref_center.points(0)
printc('center of reference =', C)

############################################################
# here we set up the common structure of the rays
rmax = 125
printc('rmax =', rmax, 'grid_res =', hdb.grid_res, 'radius_res =', hdb.radius_res)

pts = []
for r in np.linspace(0, rmax, hdb.radius_res, endpoint=True):
    for th in np.linspace(0, np.pi, hdb.grid_res, endpoint=True):  # must be both true
        for ph in np.linspace(0, 2*np.pi, 2*hdb.grid_res, endpoint=True):  # must be both true
            p = spher2cart(r, th, ph)
            # if p[0]>0 and p[1]>0 and p[2]<0: #test
            pts.append(p)

vpts = Points(pts+C)
printc('total nr of points =', len(pts))

##############################################################
printc('..please wait, this can take ~1h', c='m', box=True)
for group in dataset.keys():
    if 'set' not in group:
        continue
    printc('Processing group:', group, c='y', invert=1)
    closePlotter()  # clean up the cache of actors
    for volfile in dataset[group]['files']:
        # if 'LQR_M_JJ_E95_2829_wt_5' not in volfile: continue #test
        vol = Volume(volfile+'.vti')
        surf = vol.isosurface(90).alpha(0.1).c('b')
        vol_center = Point(vol.center(), c='b', alpha=0.6)

        T = loadTransform(volfile+'.mat')[0]

        volpts = vol.toPoints()   # get the volume as points
        volpts.applyTransform(T)  # send it to 1819_2's reference frame

        vpts_copy = vpts.clone().interpolateDataFrom(volpts, N=4, kernel='linear')

        outf = (volfile+'_rays.vtk').split('/')[-1]
        vpts_copy.addPos(-C).write(outf)
        printc('\twrote:', outf, c='lg')
        settings.collectable_actors = []

printc("Type: vedo -n -p 5 -a 0.02 -c w -x1 *2425*.vtk", c='lg', box='=')
printc("(press 4 in each window)", c='lg')
printc("If all is OK move files to data/wt or data/ko", c='lg')
