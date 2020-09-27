from vedo import Points, show, printc, Video
from vedo import Text2D, load, Line, interactive, settings
import heart_database as hdb
import numpy as np

dpath = hdb.data_path_ko
clm_data = load(dpath+'clm_ko_data.npy') # load regular numpy file

printc(clm_data['comment'], 'loaded')
# 'ray_points', 'set10', 'set14', 'set1819', 'set2122', 'set2425', 'set2829'
#               'files', 'ray_distances', 'clms'

vd = Video('step6.mp4', duration=16)
settings.rendererFrameAlpha=0.6
settings.rendererFrameColor='db'
settings.rendererFrameWidth=2

for shell in range(hdb.radius_res):
    for l in range(5): # just take the first 5 l values
        for m in range(-l,l+1):
            ms = m
            xvals = []
            yvals = []
            xmeans = hdb.nsomites
            ymeans = []
            for s in clm_data.keys():
                if 'set' not in s: continue
                clm_s = clm_data[s]['clms']
                ns = clm_data[s]['nsomites']
                nf = len(clm_data[s]['files'])
                if m<0:
                    mblock=1
                    m=-m
                else:
                    mblock=0
                ys = clm_s[:, shell, mblock,l,m] / 1.5 # visual scaling
                yvals = np.append(yvals, ys)
                xvals = np.append(xvals, np.zeros(nf) + ns)
                ymeans.append(np.mean(ys))

            vpts = Points(np.c_[xvals, yvals], r=5)
            mpts = Points(np.c_[xmeans, ymeans], r=8, c='r')
            xnew, ynew = hdb.spline(xmeans, ymeans, 100, 6)
            spts = Line(np.c_[xnew,ynew], lw=2)

            tr=''
            if l==0 and m==0:
                tr = ' R='+str(shell)

            plt = show(mpts, vpts, spts, vpts.box(),
                       Text2D("C("+str(l)+","+str(ms)+")"+tr, s=0.8, c='k'),
                       at=4+9*l+ms, shape=(5,9), sharecam=0, size=(1700,880),
                       title='Spherical Harmonics coefficients',
                       axes=0, bg='ly', bg2='w')
    interactive()
    vd.addFrame()
    for i in range(5*9):
        plt.clear(at=i)

vd.close()
interactive()



