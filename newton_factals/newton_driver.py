# Chris Harshaw
# December 2015
#
# newton_fract.py 
# Program 

import numpy as np
import general_newton as gn
import test_fun as tf

# create grid of complex numbers
re_lim = [-1, 1]
re_num = 1000
im_lim = [-1, 1]
im_num = 1000
Z = gn.complex_grid(re_lim, re_num, im_lim, im_num)

# generate polynomial functions
p = [1.0, 0.0, -2.0, 2.0]
dp = tf.poly_der(p)
params = {'p': p, 'dp': dp}
f_val = tf.poly_fun
df_val = tf.d_poly_fun

# run newton's method
roots, con_root, con_num = gn.newton_method(Z, f_val, df_val, params)

# print computed roots
print "Computed " + str(len(roots)) + " roots of " + f_val.__name__
if len(roots) < 8:
    for root in roots:
        print "%.4f \t+\t%.4fi" %(root.real, root.imag)

# plot newton fractal
colors = [(0, 255, 255), (128, 128, 255), (255, 0, 255), (255, 128, 128)]
save_path = "fractal_pictures/frac_18.png"
gn.newton_plot(con_root, con_num, colors, save_path)
