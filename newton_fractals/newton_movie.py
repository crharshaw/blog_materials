# Chris Harshaw
# December 2015
#

import numpy as np
import general_newton as gn
import test_fun as tf
import subprocess
import os
import shutil

# movie to be created
directory = "fractal_videos/fractal_stills2"
filename = "newton_fractal2.avi"
imagename = "fractal"

# create directory
if not os.path.exists(directory):
	os.makedirs(directory)
else:
	shutil.rmtree(directory)
	os.makedirs(directory)

# create grid of complex numbers
re_lim = [-5, 5]
re_num = 1000
im_lim = [-5, 5]
im_num = 1000
Z = gn.complex_grid(re_lim, re_num, im_lim, im_num)

# generate polynomial functions
p = [1.0, 0.0, -2.0, 2.0]
dp = tf.poly_der(p)
params = {'p': p, 'dp': dp}
f_val = tf.poly_fun
df_val = tf.d_poly_fun
known_roots = np.roots(p)

# frame parameters
vid_len = 5  # length of gif
frame_ps = 18  # number of frames per second
quality = 22 # the quality of the encoding

# colors
colors = [(0, 255, 255), (128, 128, 255), (255, 0, 255), (255, 128, 128)]

# generalized newton parameter, a
a_seq = np.linspace(1.5, 0.6, 600)

# create image sequence
i = 1
for a in a_seq:
    # print progress
    img_file_name = directory + '/' + imagename + '%05d' % i + '.png'
    print 'Creating frame ' + str(i) + ' of ' + str(a_seq.size)
    i += 1

    # newton's method
    roots, con_root, con_num = gn.newton_method(Z, f_val, df_val, params, a=a, disp_time=False, known_roots=known_roots)

    # create image in folder
    gn.newton_plot(con_root, con_num, colors, save_path=img_file_name)

# create the movie
ctrlStr = 'ffmpeg -r %d -i %s%%05d.png -c:v libx264 -preset slow -crf %d %s' %(frame_ps, directory + '/' + imagename, quality, filename)
subprocess.call(ctrlStr, shell=True)