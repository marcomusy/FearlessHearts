from vedo import Points, printc, spher2cart, applications
from vedo import load, precision, settings, ProgressBar
from heart_database import data_path_wt, data_path_ko, nsomites, spline, radius_res
import numpy as np
import pyshtools

dpath = data_path_wt
dset = load(dpath+'clm_wt_data.npy') # load regular numpy file

printc(dset['comment'], '- loaded.', c='g', invert=True)

#######################################
def linear_interpolate_clms(dset, step=0.1):
    # linear interpolation
    keys=[]
    for name in dset.keys():
        if 'set' not in name: continue
        keys.append(name)

    interpolated_dset = dict()
    for i in range(len(keys)-1):
        name0 = keys[i]
        name1 = keys[i+1]
        t0 = dset[name0]['nsomites']
        t1 = dset[name1]['nsomites']
        clms0 = dset[name0]['clms']
        clms1 = dset[name1]['clms']
        clms_average0 = np.mean(clms0, axis=0)
        clms_average1 = np.mean(clms1, axis=0)
        newtimes = np.arange(t0,t1, step).tolist()
        if i == len(keys)-2: # add the last timepoint
            newtimes.append(t1)
        for t in newtimes:
            w = (t-t0)/(t1-t0)
            clms_average_t = clms_average0 * (1-w) + clms_average1 * w
            interpolated_dset.update({t: clms_average_t})
    return interpolated_dset

#######################################
def spline_interpolate_clms(dset, res=186, smooth=6):
    clms_means = []
    for name in dset.keys():
        if 'set' not in name: continue
        clms = dset[name]['clms']
        clms_mean = np.mean(clms, axis=0)
        clms_means.append(clms_mean)
    clms_means = np.array(clms_means) #shape (6, 50, 2, 25, 25)

    nsoms = np.array(nsomites)
    _, nshells, blocks, lvals, mvals = clms_means.shape
    clms_new = np.zeros([res, nshells, blocks, lvals, mvals])

    pb = ProgressBar(0,nshells)
    for shell in range(nshells):
        pb.print('splining Clm')
        for block in range(blocks):
            for l in range(lvals):
                for m in range(l+1):
                    v = clms_means[:, shell, block, l, m]
                    _, vnew = spline(nsoms, v, res, smooth) # interpolate
                    clms_new[:, shell, block, l, m] = vnew

    newtimes = np.linspace(nsoms[0], nsoms[-1], res)
    interpolated_dset = dict()
    for i,t in enumerate(newtimes):
        interpolated_dset.update({t: clms_new[i]})
    return interpolated_dset

##########################################################
interpolated_dset = spline_interpolate_clms(dset)
#interpolated_dset = linear_interpolate_clms(dset)
##########################################################

clouds = []
pb = ProgressBar(0,len(interpolated_dset.keys()))
for t in interpolated_dset.keys():

    clms = interpolated_dset[t]

    scals, pts = [], []
    for shell in range(radius_res):
        cml_shell = clms[shell]

        coeffs = pyshtools.SHCoeffs.from_array(cml_shell)
        arr_shell = coeffs.expand().to_array()
        ni, nj = arr_shell.shape

        for i, lat in enumerate(np.linspace(90, -90, num=ni)):
            for j, long in enumerate(np.linspace(0, 360, num=nj)):
                th = np.deg2rad(90 - lat)
                ph = np.deg2rad(long)
                p = spher2cart(shell, th, ph)
                value = arr_shell[i][j]
                if value>-1:
                    pts.append(p)
                    scals.append(value)

    vpts = Points(pts, r=6).cmap('jet', scals)
    vpts.clean(0.005) # remove multiple or too close points
    vpts.write('output/nrsom_'+precision(t,3)+'.vtk')
    pb.print('output/reco_clouds/nrsom_*')
    vpts.name = 'nr. of somites '+precision(t,3)

    vpts.threshold('PointScalars', above=40) # only for the sake of visualization
    clouds.append(vpts)
    settings.collectable_actors=[] # clean cache

applications.Browser(clouds).show()
print('move nrsom_* to output/wt or wt reco_clouds')

