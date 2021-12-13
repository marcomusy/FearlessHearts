from vedo import Plotter, Volume, printc, loadTransform
from vedo import buildRulerAxes, Text2D, writeTransform, interactive
import heart_database
import os

#########################################################################
dset = heart_database.dataset_wt
group = 'set1819'  # do first timecourse then all the others
threshold = 60

#########################################################################
volfiles = dset[group]['files']
special = dset[group]['ref_nr']

plt2 = Plotter(bg='ly', bg2='w')

surf_special = Volume(volfiles[special]+'.vti').isosurface(threshold).extractLargestRegion()
surf_special.c('grey').alpha(0.2).pickable(False)
matfile = volfiles[special]+".mat"

if os.path.isfile(matfile):
    T = loadTransform(matfile)[0]
    printc('\nFound REFERENCE mat file', matfile, c='grey')
    surf_special.applyTransform(T)

ax = buildRulerAxes(surf_special, units='\mum')
for i, s in enumerate(volfiles):
    if i == special:
        continue
    surfi = Volume(s+".vti").isosurface(threshold).extractLargestRegion()
    surfi.c(i+2).lighting('glossy')
    matfile = s+".mat"
    if os.path.isfile(matfile):
        TC = loadTransform(matfile)
        printc('Found mat file', matfile, TC[1], c=i+2)
        surfi.applyTransform(TC[0])
    plt2.clear()
    plt2.show(surf_special, surfi, ax,
              Text2D(s, font='Calco'),
              Text2D('Press:\na to toggle shifting and zooming' +
                     '\nq to proceed when happy\nF1 to abort session.',
                     pos='bottom-left', font='Quikhand', s=0.8, c='grey', bg='lb'),
              )
    printc("(Over)write "+matfile+' [y/n/break/abort]? ', c=i+2, end='')
    r = input()
    if 'y' in r:
        writeTransform(surfi, matfile, comment='manual alignment')
        printc('Wrote file', matfile, c=i+2, invert=1)
    elif r.startswith('b'):
        printc('Not saved, break loop.', c=i+2)
        break
    elif r.startswith('a'):
        printc('Not saved, abort execution.', c=i+2)
        exit(0)
    else:
        printc('Not saved, file skipped.', c=i+2)


#########################################################################
plt3 = Plotter(N=len(volfiles), axes=7)
for i, s in enumerate(volfiles):
    vol = Volume(s+'.vti')
    surfi = vol.isosurface(threshold).c(i+2).lighting('glossy')
    matfile = s+".mat"
    if os.path.isfile(matfile):
        TC = loadTransform(matfile)
        printc('Using mat file', matfile, TC[1])
        surfi.applyTransform(TC[0])
    plt3.show(surfi, Text2D(s), at=i, interactive=0)

interactive()
