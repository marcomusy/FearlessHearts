from vedo import show, interpolateToVolume, pyplot, load, ProgressBar
import os

outdir = 'output/ko/'

######################################################### test plot
apts = load(outdir+'reco_clouds/nrsom_22.6.vtk')
vol = interpolateToVolume(apts, N=4, dims=(50,50,50))
vol.mode(1).c(["b","g","r"]).alpha([0, 0.8, 1])
vol.addScalarBar3D(title=apts.filename.replace('_', "-"))

ch = pyplot.cornerHistogram(vol, logscale=True, pos='bottom-left')

lego = vol.legosurface(vmin=40).c('lg')
show(vol, lego, ch,
     "Interpolate the point cloud onto a Volume dataset",
     axes=1).close()

########################################################## generate volumes
clouds = load(outdir+'reco_clouds/nrsom*.vtk')
pb = ProgressBar(0, len(clouds))
for apts in clouds:
    pb.print("writing vti and isos")

    bn = os.path.basename(apts.filename)

    vol = interpolateToVolume(apts, N=4, dims=(100,100,100))
    vol.write(outdir+'volumes/'+bn.replace('.vtk','.vti'))

    vol.isosurface(20).write(outdir+'isos/'+bn.replace('nrsom_','iso20_nrsom_'))
    vol.isosurface(40).write(outdir+'isos/'+bn.replace('nrsom_','iso40_nrsom_'))
    vol.isosurface(60).write(outdir+'isos/'+bn.replace('nrsom_','iso60_nrsom_'))
