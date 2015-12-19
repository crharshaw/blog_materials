# Chris Harshaw
# August 2015
#
# newton_fract.py 
# Program 

import numpy as np 
import general_newton as gn

# create grid of complex numbers
re_lim = [-1,1]
re_num = 500
im_lim = [-1,1]
im_num = 500
Z = gn.complex_grid(re_lim, re_num, im_lim, im_num)

# run newton's method
roots, con_root, con_num = gn.newton_method(Z, f_val, df_val, params)

# print computed roots
print "Computed roots of " + f_val.__name__ 
for root in roots:
	print "%.3f" %(root)

# plot newton fractal
colors = [(0,255,255), (128,128,255), (255,0,255), (255,128,128)]
save_path = "fractal_pictures/frac_9.png"
gn.newton_plot(con_root, con_num, colors, save_path)


