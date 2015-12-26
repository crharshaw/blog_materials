# Chris Harshaw
# December 2015
#
# newton_fract.py 
# Program 

import numpy as np
import general_newton as gn
import test_fun as tf

# create grid of complex numbers
re_lim = [-1.0, 1.0]
re_num = 1000
im_lim = [-1.0, 1.0]
im_num = 1000
Z = gn.complex_grid(re_lim, re_num, im_lim, im_num)

# generate polynomial functions
p = [  1.00000000e+00 +0.00000000e+00j,
         7.77156117e-16 +0.00000000e+00j,
         2.22044605e-16 -6.66133815e-16j,
         0.00000000e+00 -3.10755655e-16j,
        -2.05177676e-16 -5.11022966e-16j,
        -7.21644966e-16 -3.33066907e-16j,  -1.00000000e+00 +1.83186799e-15j]
dp = tf.poly_der(p)
params = {'p': p, 'dp': dp}
f_val = tf.poly_fun
df_val = tf.d_poly_fun

# run newton's method
roots, con_root, con_num = gn.newton_method(Z, f_val, df_val, params, a=0.6)

# print computed roots
print "Computed " + str(len(roots)) + " roots of " + f_val.__name__
if len(roots) < 8:
    for root in roots:
        print "%.4f \t+\t%.4fi" %(root.real, root.imag)

# plot newton fractal
col_source = 'matplotlib'
# col_params = {'lover': 'joy_of_summer', 'keywords': 'I like your Smile', 'cmap':'spring', 'col_num':len(p)}
col_params = {'lover': 'QitsuneQage', 'keywords': 'Almost Together', 'cmap':'jet', 'col_num':len(p)}
# col_params = {'lover': 'joy_of_summer', 'keywords': 'See The Light', 'cmap':'spectral', 'col_num':len(p)}
# col_params = {'lover': 'pseudo.cyborg', 'keywords': 'math music', 'cmap':'summer', 'col_num':len(p)}
# col_params = {'lover': 'silentHue', 'keywords': 'Mute Math EP', 'cmap':'winter', 'col_num':len(p)}
# col_params = {'lover': 'yakotta', 'keywords': 'blue hour', 'cmap':'gnuplot', 'col_num':len(p)}
# col_params = {'lover': 'owlies', 'keywords': 'endlessly.', 'cmap':'gnuplot', 'col_num':len(p)}
# col_params = {'lover': 'justjessi', 'keywords': 'groovy kind of xmas', 'cmap':'gnuplot', 'col_num':len(p)}
# col_params = {'lover': 'MarieBrandt', 'keywords': 'Barcelona', 'cmap':'gnuplot', 'col_num':len(p)}

colors = gn.config_colors(col_source, col_params)
save_path = "fractal_pictures/frac_33.png"
gn.newton_plot(con_root, con_num, colors, save_path)
