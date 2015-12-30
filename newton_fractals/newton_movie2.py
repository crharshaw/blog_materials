# Chris Harshaw
# December 2015
#

import numpy as np
from numpy.polynomial import polynomial as poly
import general_newton as gn
import test_fun as tf
import subprocess
import os
import shutil

# gif to be created
directory = "fractal_videos/fractal_stills5"
filename = "newton_fractal3.avi"
imagename = "fractal"

# create directory
if not os.path.exists(directory):
	os.makedirs(directory)
else:
	shutil.rmtree(directory)
	os.makedirs(directory)

# create grid of complex numbers
re_lim = [-1.5, 1.5]
re_num = 1000
im_lim = [-1.5, 1.5]
im_num = 1000
Z = gn.complex_grid(re_lim, re_num, im_lim, im_num)

# frame parameters
vid_len = 45  # length of gif
frame_ps = 20  # number of frames per second
quality = 22 # the quality of the encoding

# colors
col_source = 'colourlovers'
col_params = {'lover': 'yakotta', 'keywords': 'blue hour'}
colors = gn.config_colors(col_source, col_params)

# polynomial test functions
f_val = tf.poly_fun
df_val = tf.d_poly_fun
params = {}

# get parameterized roots
speeds = np.array([1,4,1,4])
num_times = vid_len * frame_ps
param_roots = tf.parameterized_roots1(speeds, num_times)
max_iter = 50

# create image sequence
for i in range(num_times):
    # print progress
    img_file_name = directory + '/' + imagename + '%05d' % (i+1) + '.png'
    print 'Creating frame ' + str(i+1) + ' of ' + str(num_times)

    # create polynomial from roots
    known_roots = param_roots[i,:]
    p = np.flipud(poly.polyfromroots(known_roots))
    dp = tf.poly_der(p)

    # update param dictionary
    params['p'] = p
    params['dp'] = dp

    # newton's method
    roots, con_root, con_num = gn.newton_method(Z, f_val, df_val, params, disp_time=False, known_roots=known_roots, max_iter = max_iter)

    # create image in folder
    gn.newton_plot(con_root, con_num, colors, save_path=img_file_name, max_shade=max_iter)

# create the movie
ctrlStr = 'ffmpeg -r %d -i %s%%05d.png -c:v libx264 -preset slow -crf %d %s' %(frame_ps, directory + '/' + imagename, quality, filename)
subprocess.call(ctrlStr, shell=True)