# Chris Harshaw
# August 2015
#
# newton_fract.py 
# Program 

import numpy as np 
from cmath import *
from newton_plot import *

# grid point parameters
re_lim = [-1.2,1,2]
re_num = 750
im_lim = [-1.2,1.2]
im_num = 750

# create grid
re = np.linspace(re_lim[0], re_lim[1], num=re_num)
im = np.linspace(im_lim[0], im_lim[1], num=im_num)

# generate functions, roots, and colors
p = np.array([1.0, 0.416667, 1.5416667, 0.11458333, 0.28125])	
roots = np.roots(p)
colors = [(0,255,255), (128,128,255), (255,0,255), (255,128,128)]

# netwon plot parameters
a = 0.53
max_iter = 50
tol = 1e-5
save_path = "fractal_pictures/frac_test.png"
disp_time = True

newton_plot(re, im, p, a, max_iter, tol, roots, colors, save_path, disp_time)


