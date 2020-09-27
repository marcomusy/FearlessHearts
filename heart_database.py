#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from scipy.interpolate import splev, splrep

data_path_wt = 'data/wt/'
data_path_ko = 'data/ko/'
grid_res     = 50
radius_res   = 50
nsomites     = [10, 14, 18.5, 21.5, 24.5, 28.5]

dataset_ko = dict(

    comment='Arid3b Knock-Out dataset containing ray intensities and Clm values',

    ray_points=[],

    timecourse = dict(files=[
                                data_path_ko+'LQR_M_JJ_1819_ko_3',
                                data_path_ko+'LQR_M_JJ_2122_ko_1',
                                data_path_ko+'LQR_M_JJ_2425_ko_1',
                                data_path_ko+'LQR_M_JJ_2829_ko_2',
                                data_path_ko+'heart_290113_14sp_ko_3_c2',
                                data_path_ko+'heart_300113_10sp_ko_2_c2',
                    ],
                    ref_nr=0,
        ),

    set10 = dict( nsomites=10,
                  files = [
                            data_path_ko+'heart_300113_10sp_ko_1_c2',
                            data_path_ko+'heart_300113_10sp_ko_2_c2',
                            data_path_ko+'heart_300113_10sp_ko_3_c2',
                           ],
                  ray_distances=[],
                  clms=[], # list of length = nr of files
                  comment='',
                  ref_nr=1,
    ),

    set14 = dict( nsomites=14,
                  files = [
                            data_path_ko+'heart_110113_14sp_ko_1_c2',
                            data_path_ko+'heart_110113_14sp_ko_2_c2',
                            data_path_ko+'heart_290113_14sp_ko_3_c2',
                           ],
                  ray_distances=[],
                  clms=[], # list of length = nr of files
                  comment='',
                  ref_nr=2,
    ),

    set1819 = dict( nsomites=18.5,
                    files = [
                              data_path_ko+'LQR_M_JJ_1819_ko_1',
                              data_path_ko+'LQR_M_JJ_1819_ko_2',
                              data_path_ko+'LQR_M_JJ_1819_ko_3',
                            ],
                    ray_distances=[],
                    clms=[], # list of length = nr of files
                    comment='',
                    ref_nr=2,
    ),

    set2122 = dict( nsomites=21.5,
                    files = [
                              data_path_ko+'LQR_M_JJ_2122_ko_1',
                              data_path_ko+'LQR_M_JJ_2122_ko_2',
                              data_path_ko+'LQR_M_JJ_2122_ko_3',
                              data_path_ko+'LQR_M_JJ_2122_ko_4',
                             ],
                    ray_distances=[],
                    clms=[], # list of length = nr of files
                    comment='',
                    ref_nr=0,
    ),

    set2425 = dict( nsomites=24.5,
                    files = [
                              data_path_ko+'LQR_M_JJ_2425_ko_1',
                              data_path_ko+'LQR_M_JJ_2425_ko_3',
                             ],
                    ray_distances=[],
                    clms=[], # list of length = nr of files
                    comment='',
                    ref_nr=0,
    ),

    set2829 = dict( nsomites=28.5,
                    files = [
                              data_path_ko+'LQR_M_JJ_2829_ko_1',
                              data_path_ko+'LQR_M_JJ_2829_ko_2',
                              data_path_ko+'LQR_M_JJ_2829_ko_3',
                             ],
                    ray_distances=[],
                    clms=[], # list of length = nr of files
                    comment='',
                    ref_nr=1,
    ),
)

##########################################################################
dataset_wt = dict(

    comment='Wild type dataset containing the ray intensities and Clm values',

    ray_points=[],

    timecourse = dict(files=[
                                data_path_wt+'LQR_M_JJ_1819_wt_2', #
                                data_path_wt+'LQR_M_JJ_2122_wt_1',
                                data_path_wt+'LQR_M_JJ_2425_wt_2b',
                                data_path_wt+'LQR_M_JJ_2829_wt_3',
                                data_path_wt+'heart_110113_14sp_wt_2_c2',
                                data_path_wt+'heart_300113_10sp_wt_4_c2',
                            ],
                        ref_nr=0,
    ),

    set10 = dict(
                   nsomites=10,
                   files = [
                            data_path_wt+'heart_300113_10sp_wt_1_c2',
                            data_path_wt+'heart_300113_10sp_wt_3_c2',
                            data_path_wt+'heart_300113_10sp_wt_4_c2', #
                            data_path_wt+'heart_300113_10sp_wt_5_c2',
                           ],
                   ray_distances=[],
                   clms=[], # list of length = nr of files
                   comment='',
                   ref_nr=2,
    ),

    set14 = dict(
                   nsomites=14,
                   files = [
                            data_path_wt+'heart_110113_14sp_wt_1_c2',
                            data_path_wt+'heart_110113_14sp_wt_2_c2', #
                            data_path_wt+'heart_300113_14sp_wt_3_c2',
                            data_path_wt+'heart_300113_14sp_wt_4_c2',
                           ],
                   ray_distances=[],
                   clms=[],
                   comment='',
                   ref_nr=1,
    ),

    set1819 = dict(
                   nsomites=18.5,
                   files = [
                            data_path_wt+'LQR_M_JJ_1819_wt_1',
                            data_path_wt+'LQR_M_JJ_1819_wt_2', #
                            data_path_wt+'LQR_M_JJ_1819_wt_3',
                            data_path_wt+'LQR_M_JJ_1819_wt_4',
                            data_path_wt+'LQR_M_JJ_1819_wt_5',
                           ],
                   ray_distances=[],
                   clms=[],
                   comment='',
                   ref_nr=1,
    ),

    set2122 = dict(
                   nsomites=21.5,
                   files = [
                            data_path_wt+'LQR_M_JJ_2122_wt_1', #
                            data_path_wt+'LQR_M_JJ_2122_wt_2',
                            data_path_wt+'LQR_M_JJ_2122_wt_3',
                            data_path_wt+'LQR_M_JJ_2122_wt_4',
                            data_path_wt+'LQR_M_JJ_2122_wt_5',
                           ],
                   ray_distances=[],
                   clms=[],
                   comment='',
                   ref_nr=0,
    ),

     set2425 = dict(
                   nsomites=24.5,
                   files = [
                            data_path_wt+'LQR_M_JJ_2425_wt_1b',
                            data_path_wt+'LQR_M_JJ_2425_wt_2b', #
                            data_path_wt+'LQR_M_JJ_2425_wt_3b',
                           ],
                   ray_distances=[],
                   clms=[],
                   comment='',
                   ref_nr=1,
    ),

     set2829 = dict(
                   nsomites=28.5,
                   files = [
                            data_path_wt+'LQR_M_JJ_2829_wt_1',
                            data_path_wt+'LQR_M_JJ_2829_wt_2',
                            data_path_wt+'LQR_M_JJ_2829_wt_3', #
                            data_path_wt+'LQR_M_JJ_E95_2829_wt_4',
                            data_path_wt+'LQR_M_JJ_E95_2829_wt_5',
                           ],
                   ray_distances=[],
                   clms=[],
                   comment='',
                   ref_nr=2,
    ),
)

def spline(x, y, res, smooth):
    """
    Return a spline that doesnt necessarly pass exactly throught all points.
    smooth = smoothing factor (0 = interpolate points exactly, 1 = average point positions)
    """
    xnew = np.linspace(x[0], x[-1], res)
    ynew = splev(xnew, splrep(x, y, s=smooth), der=0)
    return xnew, ynew

