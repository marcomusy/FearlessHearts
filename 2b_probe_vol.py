from vedo import spher2cart, probeLine, merge, Volume, show, loadTransform
from vedo import Point, Points
import numpy as np

N=10

###############################
def rays(vol, center):
    if isinstance(center, Points):
        center = center.points()[0]
    v0, v1 = vol.scalarRange()
    rmax = max(vol.bounds())/2
    lines = []
    for it, th in enumerate(np.linspace(0, np.pi, N, endpoint=True)):
        for ph in np.linspace(0, 2*np.pi, 2*N, endpoint=False):
            p2 = spher2cart(rmax, th, ph)
            pl = probeLine(vol, center, center+p2)
            lines.append(pl)
            if th>3.14 or th<1.57/N: break
    mlines = merge(lines).cmap('hot_r', 'input_scalars', vmin=v0, vmax=v1)
    return mlines.alpha(0.2).lw(4)

###############################
vref = Volume('data/wt/LQR_M_JJ_1819_wt_2.vti') # >THE REF
sref = vref.isosurface(90).alpha(0.1)
vref_center = Point(vref.center(), c='g', alpha=0.6)

vol = Volume('data/wt/LQR_M_JJ_2829_wt_1.vti')
surf = vol.isosurface(90).alpha(0.1).c('b')
vol_center = Point(vol.center(), c='b', alpha=0.6)

T  = loadTransform('data/wt/LQR_M_JJ_2829_wt_1.mat')[0]
TI = T.GetInverse()

# Find the center of the sphere using TI so that when will Transform back
# it will end up in the center of reference 1819_wt_2
center = vref_center.applyTransform(TI).c('r')

# probe the volume and send it to 1819_2's reference frame
proberays = rays(vol, center)
proberays.applyTransform(T)
proberays.addScalarBar3D(title='Voxel Intensity along '+str(N)+'^2  Rays', c='w')

vig1 = proberays.vignette('Heart probe\nsomites 2829-wt-1').followCamera()
vig2 = sref.vignette('Reference_1819', c='lg').followCamera()

show(sref, proberays, vig1, vig2, axes=1, bg='bb')


