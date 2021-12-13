# @Author: Giovanni Dalmasso <gio>
# @Date:   15-Nov-2020
# @Email:  giovanni.dalmasso@embl.es
# @Project: FeARLesS
# @Filename: fig.py
# @Last modified by:   gio
# @Last modified time: 09-Sep-2021
# @License: MIT


from vedo import load, show, settings, screenshot, Ruler
import sys

settings.rendererFrameAlpha = 0
settings.useParallelProjection = False
settings.screeshotLargeImage = True


# #############################################################
# #############################################################
# ORIGINAL DATA
#

test = load("data/wt/*21*.vti")
print("loaded ", len(test), " volumes")

cam = dict(
    pos=(-232.6, -163.9, 663.6),
    focalPoint=(107.5, 123.0, 92.00),
    viewup=(-0.06093, -0.8771, -0.4765),
    distance=724.4,
    clippingRange=(375.3, 1166),
)

# x0, x1, y0, y1, z0, z1 = test[0].bounds()
# r1 = Ruler([x1, y1, z1], [x1, y0, z0], units=" \mum", axisRotation=45)


axes_opts = dict(
    xtitle="\mum",  # latex-style syntax
    ytitle="\mum",
    ztitle="\mum",  # many unicode chars are supported (type: vedo -r fonts)
    # yValuesAndLabels=[(-3.2,'Mark^a_-3.2'), (-1.2,'Carmen^b_-1.2'), (3,'John^c_3')],
    # textScale=1.3,       # make all text 30% bigger
    # numberOfDivisions=5, # approximate number of divisions on longest axis
    # axesLineWidth= 2,
    # gridLineWidth= 1,
    # zxGrid2=True,        # show zx plane on opposite side of the bounding box
    # yzGrid2=True,        # show yz plane on opposite side of the bounding box
    # xyPlaneColor='green7',
    # xyGridColor='dg',    # darkgreen line color
    # xyAlpha=0.2,         # grid opacity
    # xTitlePosition=0.5,  # title fractional positions along axis
    # xTitleJustify="top-center", # align title wrt to its axis
    # yTitleSize=0.02,
    # yTitleBox=True,
    # yTitleOffset=0.05,
    # yLabelOffset=0.4,
    # yHighlightZero=True, # draw a line highlighting zero position if in range
    # yHighlightZeroColor='red',
    # zLineColor='blue',
    # zTitleColor='blue',
    # zTitleBackfaceColor='v', # violet color of axis title backface
    # labelFont="Quikhand",
    # yLabelSize=0.025,    # size of the numeric labels along Y axis
    # yLabelColor='dg',    # color of the numeric labels along Y axis
)

show(test[0], axes=axes_opts)
sys.exit()


# heartsData10 = load('data/wt/*10*.vti')
# heartsData14 = load('data/wt/*14*.vti')
# heartsData18 = load('data/wt/*18*.vti')
# heartsData21 = load('data/wt/*21*.vti')
# heartsData24 = load('data/wt/*24*.vti')
# heartsData28 = load('data/wt/*28*.vti')
#
# heartsDataPlots = []
# heartsDataPlots.append(heartsData10[0].isosurface(threshold=75).extractLargestRegion().phong().c('red').lighting('glossy'))
# heartsDataPlots.append(heartsData14[2].isosurface(threshold=50).extractLargestRegion().phong().c('red').lighting('glossy'))
# heartsDataPlots.append(heartsData18[2].isosurface(threshold=80).extractLargestRegion().phong().c('red').lighting('glossy'))
# heartsDataPlots.append(heartsData21[2].isosurface(threshold=80).extractLargestRegion().phong().c('red').lighting('glossy'))
# heartsDataPlots.append(heartsData24[2].isosurface(threshold=80).extractLargestRegion().phong().c('red').lighting('glossy'))
# heartsDataPlots.append(heartsData28[0].isosurface(threshold=80).extractLargestRegion().phong().c('red').lighting('glossy'))
#
#
# plt = show(heartsDataPlots,
#            shape=[3, 2])
#
#
# for i, a in enumerate(heartsDataPlots):
#     a.write('fig/' + f'mesh_{i}.vtk')
#
# quit()
#
# #############################################################
# #############################################################


hearts = load("output/wt/isos_abs_scale/iso35*.vtk")

heartsData = load("fig/*.vtk")

col = "ghostwhite"

heartsDataPlots = []
for j in range(len(heartsData)):
    heartsDataPlots.append(
        heartsData[j].extractLargestRegion().phong().c(col)  # .lighting("glossy")
    )

cam1 = dict(
    pos=(513.0, 136.6, -250.1),
    focalPoint=(146.6, 136.9, 156.6),
    viewup=(-0.5057, -0.7331, -0.4549),
    distance=547.4,
    clippingRange=(228.2, 950.6),
)


show(
    heartsDataPlots, shape=[2, 3], camera=cam1  # , size=(600, 2000)
)  # .screenshot('data.png', scale=None).close()
# sys.exit()

heartsPlots = []

for j in range(12):
    if j == 11:
        heartsPlots.append(
            hearts[-1].extractLargestRegion().phong().c(col)  # .lighting("glossy")
        )
    else:
        heartsPlots.append(
            hearts[0 + j * 17]
            .extractLargestRegion()
            .phong()
            .c(col)  # .lighting("glossy")
        )
    print(0 + j * 17)


cam2 = dict(
    pos=(169.7, 110.1, 84.70),
    focalPoint=(4.024, -2.249, 2.088),
    viewup=(-0.6381, 0.6910, 0.3397),
    distance=216.6,
    clippingRange=(70.59, 394.4),
)

show(heartsPlots, N=len(heartsPlots), camera=cam2).screenshot(
    "res.png", scale=None
).close()
