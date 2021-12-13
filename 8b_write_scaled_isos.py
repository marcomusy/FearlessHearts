from vedo import applications, load, loadTransform, printc, Text3D, precision
from vedo.pyplot import plot
import numpy as np
import scipy.optimize as opt
import glob
import os

srcdir = 'data/wt/'
outdir = 'output/wt/'

###################################################################
flist = sorted(glob.glob(srcdir+'*.mat'))
pts = []
for f in flist:
    s = 1 / loadTransform(f)[0].GetScale()[0]
    if '10sp' in f:
        t = 10.0
    if '14sp' in f:
        t = 14.0
    if '1819' in f:
        t = 18.5
    if '2122' in f:
        t = 21.5
    if '2425' in f:
        t = 24.5
    if '2829' in f:
        t = 28.5
    pts.append([t, s])

plt = plot(pts, '.', xtitle='nr. of somites', ytitle='volumetric factor')

# use scipy to fit
t, s = np.array(pts).T
def linear(x, a, b): return a*x + b


pars, pcov = opt.curve_fit(linear, t, s, p0=[1, 0])
perr = np.sqrt(np.diag(pcov))/np.sqrt(6)
printc('pars =', pars, '\pm', perr, box=True, c='t')
x = np.linspace(9, 30, 100)
y = linear(x, *pars)

plt += plot(x, y, '-r', lw=15)
plt += plot(x, linear(x, *(pars+perr)), '-r', la=0.25)
plt += plot(x, linear(x, *(pars-perr)), '-r', la=0.25)
plt += Text3D('Fit params:\n' + precision(pars, 3), pos=(11, 1.4), c='dr', s=.5)
plt.show().close()

###################################################################
printc('Generating abs scaled isosurfaces in', outdir+'isos_abs_scale/')
isos = load(outdir+'isos/iso35*.vtk')
times = np.linspace(10, 28.5, num=len(isos))
scales = linear(times, *pars)
for i, iso in enumerate(isos):
    iso.scale(scales[i]).c('gold').lighting('glossy')
    fname = os.path.basename(iso.filename)
    iso.write(outdir+'isos_abs_scale/'+fname)

applications.Browser(isos).show(axes=dict(yzGrid=False))
