from vedo import load, Volume, settings, show
from vedo.pyplot import cornerHistogram
import numpy as np

dirname = "/home/musy/heart_data_analysis/original/C2/ko/"
settings.useParallelProjection = True

#################################################################
vname = "LQR_M_JJ_2829_ko_3.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .35,.35)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0), interactive=0)
# exit()

#################################################################
vname = "LQR_M_JJ_2829_ko_2.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .35,.35)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()

#################################################################
vname = "LQR_M_JJ_2829_ko_1.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.37,.35, .35,.35, .37,.42)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()

#################################################################
vname = "LQR_M_JJ_2425_ko_3.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .4,.3)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()

#################################################################
vname = "LQR_M_JJ_2425_ko_1.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.3, .35,.35, .4,.3)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()


#################################################################
vname = "LQR_M_JJ_2122_ko_4.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .45,.30)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()

#################################################################
vname = "LQR_M_JJ_2122_ko_3.vti"
volt = load(dirname+vname)
# ch0 = cornerHistogram(volt, logscale=1, pos='bottom-left', c='r')
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .35,.35)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()

#################################################################
vname = "LQR_M_JJ_2122_ko_2.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .50,.3)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()

#################################################################
vname = "LQR_M_JJ_2122_ko_1.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .49,.35)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()

#################################################################
vname = "LQR_M_JJ_1819_ko_3.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.38, .45,.35, .38,.38)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1100,0))
# exit()


#################################################################
vname = "LQR_M_JJ_1819_ko_2.vti"
volt = load(dirname+vname)
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .45,.3)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1000,0))
# exit()

#################################################################
vname = "LQR_M_JJ_1819_ko_1.vti"
volt = load(dirname+vname)
# ch0 = cornerHistogram(volt, logscale=1, pos='bottom-left', c='r')
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.3, .3,.3, .45,.3)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol = Volume(varr).write(vname)
show(vol, vname.replace('.vti',''), axes=1, pos=(1000,0))
# exit()

#################################################################
vname = "heart_290113_14sp_ko_3_c2.vti"
volt = load(dirname+vname)
ch0 = cornerHistogram(volt, logscale=1, pos='bottom-left', c='r')
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.3, .3,.3, .45,.3)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
vol = Volume(varr).write(vname)
ch1 = cornerHistogram(vol, logscale=1, pos='bottom-left')
show(vol,ch0, ch1, vname.replace('.vti',''), axes=1, pos=(1000,0))
# exit()

#################################################################
vname = "heart_110113_14sp_ko_2_c2.vti"
volt = load(dirname+vname)
ch0 = cornerHistogram(volt, logscale=1, pos='bottom-left', c='r')
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.3, .3,.3, .4,.4)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
vol = Volume(varr).write(vname)
ch1 = cornerHistogram(vol, logscale=1, pos='bottom-left')
show(vol,ch0, ch1, vname.replace('.vti',''), axes=1, pos=(1000,0))
# exit()

#################################################################
vname = "heart_110113_14sp_ko_1_c2.vti"
volt = load(dirname+vname)
ch0 = cornerHistogram(volt, logscale=1, pos='bottom-left', c='r')
volt.threshold(below=30, replaceWith=0.)
volt.crop(.31,.3, .39,.25, .45,.3)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
vol = Volume(varr).write(vname)
ch1 = cornerHistogram(vol, logscale=1, pos='bottom-left')
show(vol,ch0, ch1, vname.replace('.vti',''), axes=1, pos=(1000,0))
# exit()

#################################################################
vname = "heart_300113_10sp_ko_3_c2.vti"
volt = load(dirname+vname)
ch0 = cornerHistogram(volt, logscale=1, pos='bottom-left', c='r')
volt.threshold(below=30, replaceWith=0.)
volt.crop(.39,.35, .35,.35, .5,.25)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
vol = Volume(varr).write(vname)
ch1 = cornerHistogram(vol, logscale=1, pos='bottom-left')
show(vol,ch0, ch1, vname.replace('.vti',''), axes=1, pos=(1000,0))
# exit()

#################################################################
vname = "heart_300113_10sp_ko_2_c2.vti"
volt = load(dirname+vname)
ch0 = cornerHistogram(volt, logscale=1, pos='bottom-left', c='r')
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.35, .35,.35, .6,.2)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
vol = Volume(varr).write(vname)
ch1 = cornerHistogram(vol, logscale=1, pos='bottom-left')
show(vol,ch0, ch1, vname.replace('.vti',''), axes=1, pos=(1000,0))
# exit()

#################################################################
vname = "heart_300113_10sp_ko_1_c2.vti"
volt = load(dirname+vname)
ch0 = cornerHistogram(volt, logscale=1, pos='bottom-left', c='r')
volt.threshold(below=30, replaceWith=0.)
volt.crop(.3,.33, .5,.3, .5,.3)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
vol = Volume(varr).write(vname)
ch1 = cornerHistogram(vol, logscale=1, pos='bottom-left')
show(vol,ch0, ch1, vname.replace('.vti',''), axes=1, pos=(1000,0))
# exit()


#################################################################
exit() #################################################################
#################################################################


#################################################################
vname = "heart_300113_10sp_wt_1_c2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop (.42,.45, .48,.43, .65,.24)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "heart_300113_10sp_wt_3_c2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.44,.41, .57,.33, .59,.29)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "heart_300113_10sp_wt_4_c2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.48,.41, .55,.37, .52,.38)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "heart_300113_10sp_wt_5_c2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.42,.43, .49,.41, .51,.36)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()

#################################################################
vname = "heart_110113_14sp_wt_1_c2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.39, .45,.38, .38,.47)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "heart_110113_14sp_wt_2_c2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.39, .41,.40, .44,.39)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "heart_300113_14sp_wt_3_c2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.47,.37, .48,.43, .46,.42)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
################################################################
vname = "heart_300113_14sp_wt_4_c2.vti"
volt = load(dirname+vname).printInfo()
volt.printInfo()
volt.crop(.38,.44, .42,.4, .43,.43)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
varr = np.flip(varr, axis=0)
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()

#################################################################
vname = "LQR_M_JJ_1819_wt_1.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.41, .39,.4, .39,.44)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_1819_wt_2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.39,.43,  .41,.39, .44,.39)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_1819_wt_3.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.41, .40,.39, .43,.38)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_1819_wt_4.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.39,.42, .40,.38, .44,.38 )
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_1819_wt_5.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=25, replaceWith=0.)
volt.crop(.40,.39, .37,.44, .48,.35)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()

#################################################################
vname = "LQR_M_JJ_2122_wt_1.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.38,.41, .42,.34, .44,.38)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_2122_wt_2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.39,.37,.37,.35,.37,.40)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_2122_wt_3.vti"
volt = load(dirname+vname).printInfo()
volt.printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.39,.39,.36,.5,.31)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
################################################################
vname = "LQR_M_JJ_2122_wt_4.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.38,.37,.37,.47,.33)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_2122_wt_5.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.4,.4,.39,.36,.48,.33)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_2425_wt_1b.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.39,.35,.38,.38,.33,.45)# (.35,.41,.34,.40,.34,.42)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_2425_wt_2b.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.35,.41,.34,.40,.34,.42)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_2425_wt_3b.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.37,.41,.35,.39,.35,.43)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()


#################################################################
vname = "LQR_M_JJ_2829_wt_3.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.37,.35,.35,.34,.30,.40)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
#################################################################
vname = "LQR_M_JJ_2829_wt_1.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.37,.37,.37,.36,.40,.30)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printInfo().show(axes=1)
# exit()
################################################################
vname = "LQR_M_JJ_2829_wt_2.vti"
volt = load(dirname+vname).printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop(.37,.37,.37,.36,.37,.40)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
Volume(varr).write(vname).printHistogram().show(axes=1)
# exit()

#################################################################
volt = load("data/original/old_analysis/LQR_MJJ_heart_E95_2/C1_UV.slc").printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop (.41,.3, .29,.44, .3,.44)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol=Volume(varr).printInfo()
vol.show(axes=1)
vol.write('LQR_M_JJ_E95_2829_wt_5.vti')
# exit()
#################################################################
volt = load("data/original/old_analysis/LQR_MJJ_heart_E95_1/C1_UV.slc").printInfo()
volt.threshold(below=30, replaceWith=0.)
volt.crop (.41,.31, .35,.35, .35,.41)
varr = np.transpose(volt.getDataArray(), axes=[2,1,0])
vol=Volume(varr).printInfo()
vol.show(axes=1)
vol.write('LQR_M_JJ_E95_2829_wt_4.vti')
# exit()
#################################################################



# import polyscope
# settings.useParallelProjection = False
# m = load('data/wt/LQR_M_JJ_1819_wt_2.vti').isosurface(60).extractLargestRegion()
# m.rotateY(-45)
# polyscope.set_verbosity(0)
# polyscope.set_up_dir("z_up")
# polyscope.init()
# ps_mesh = polyscope.register_surface_mesh('My vedo mesh',
#                                           m.points(), m.faces(),
#                                           color=[0.5,0,0],
#                                           smooth_shade=True)
# ps_mesh.set_material("wax") # wax, mud, jade, candy
# polyscope.show()
# exit()