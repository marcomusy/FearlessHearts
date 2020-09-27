# generate histogram for the probing rays
from vedo import spher2cart, probeLine, merge, Volume, show
from vedo.pyplot import plot
import numpy as np
import heart_database as hdb

N=50

volpath = hdb.data_path_ko+'LQR_M_JJ_2122_ko_'

###############################
def rays(vol):

    plt=None
    p1 = vol.center()
    v0, v1 = vol.scalarRange()
    rmax = max(vol.bounds())/2

    lines, aplots = [], []
    for it, th in enumerate(np.linspace(0, np.pi, N, endpoint=False)):
        for ph in np.linspace(0, 2*np.pi, N, endpoint=False):
            p2 = spher2cart(rmax, th, ph)
            pl = probeLine(vol, p1, p1+p2)
            lines.append(pl)
        if it==10 or it==20 or it==30 or it==40:
            xvals = range(pl.N())
            yvals = pl.getPointArray()
            plt = plot(xvals, yvals,
                       xtitle='ray point nr',
                       ytitle='voxel intensity',
                       xlim=(0,pl.N()),
                       ylim=(0,150),
                       lc=i,#'k',   # line color
                       marker=".",  # marker style
                       mc='k',      # marker color
                       ms=0.5,      # marker size
                      )
            aplots.append(plt)

    mlines = merge(lines).cmap('ocean_r', 'input_scalars', vmin=v0, vmax=v1)
    mlines.alpha(0.2).lw(4)
    return mlines, aplots

###############################
alines, lplots = [],[]
for i in range(1,4):
    vol = Volume(volpath+str(i)+'.vti')
    rys = rays(vol)
    mlines = rys[0]
    mplots = rys[1]
    if i==3: mlines.addScalarBar3D(title='Voxel Intensity')
    alines.append(mlines)
    lplots += mplots

show(alines, N=3, axes=1)
cam = dict(pos=(50.1, 34.3, 173),
           focalPoint=(50.1, 34.3, 2.20e-10),
           viewup=(0, 1.00, 0),
           distance=173,
           clippingRange=(162, 187))
show(lplots[:12], N=12, camera=cam, sharecam=0, new=True)

sumplt = lplots[0]
for i in range(1,10):
    sumplt += lplots[i]
show(sumplt, new=True)


