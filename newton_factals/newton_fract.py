# Chris Harshaw
# August 2015
#
# newton_fract.py 
# Program 

import numpy as np 
from cmath import *
from fast_newton import newton_plot

# grid point parameters
re_lim = [-1,1]
re_num = 500
im_lim = [-1,1]
im_num = 500

# create grid
re = np.linspace(re_lim[0], re_lim[1], num=re_num)
im = np.linspace(im_lim[0], im_lim[1], num=im_num)

# generate functions, roots, and colors
p = np.array([1.0, 0.0, -2.0, 2.0])	
roots = np.roots(p)
colors = [(0,255,255), (128,128,255), (255,0,255), (255,128,128)]

# netwon plot parameters
a = 1.0
max_iter = 50
tol = 1e-5
save_path = "fractal_pictures/frac_9.png"
disp_time = True

newton_plot(re, im, p, max_iter, tol, roots, colors, save_path, a, disp_time)


