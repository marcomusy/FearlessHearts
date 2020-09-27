# Recontstruct the averages time points without splining, just linearly
from vedo import Points, show, printc, spher2cart, load, interactive
import heart_database as hdb
import numpy as np
import pyshtools

dpath = hdb.data_path_ko
dset = load(dpath+'clm_ko_data.npy') # load regular numpy file

printc(dset['comment'], '- loaded.', c='g', invert=True)

iat = 0
for name in dset.keys():
    if 'set' not in name: continue

    clms = dset[name]['clms']
    clms_average_on_hearts = np.mean(clms, axis=0)
    scals, pts = [], []
    for shell in range(hdb.radius_res):
        cml_shell = clms_average_on_hearts[shell]

        coeffs = pyshtools.SHCoeffs.from_array(cml_shell)
        arr_shell = coeffs.expand().to_array()
        ni, nj = arr_shell.shape

        for i, lat in enumerate(np.linspace(90, -90, num=ni)):
            for j, long in enumerate(np.linspace(0, 360, num=nj)):
                th = np.deg2rad(90 - lat)
                ph = np.deg2rad(long)
                p = spher2cart(shell, th, ph)
                value = arr_shell[i][j]
                if value>40:
                    pts.append(p)
                    scals.append(value)

    vpts = Points(pts, r=6).cmap('jet', scals).clean(0.01)

    printc(name, vpts.N())
    show(vpts, name, at=iat, N=6, axes=1, interactive=0)
    iat += 1

interactive()
