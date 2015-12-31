# Chris Harshaw
# December 2015
#
# newton_fract.py 
# Program 

import numpy as np
import general_newton as gn
import test_fun as tf

# create grid of complex numbers
re_lim = [-0.2, 0.2]
re_num = 1000
im_lim = [-0.2, 0.2]
im_num = 1000
Z = gn.complex_grid(re_lim, re_num, im_lim, im_num)

# generate rational functions
p = np.array([1.0, 0.0, -2.0, 2.0])
q = np.array([2, 0, -10])
dp = tf.poly_der(p)
dq = tf.poly_der(q)
params = {'p': p, 'dp': dp, 'q':q, 'dq':dq}
f_val = tf.poly_fun
df_val = tf.d_poly_fun
max_iter = 50

# run newton's method
roots, con_root, con_num = gn.newton_method(Z, f_val, df_val, params, max_iter=max_iter)

# print computed roots
print "Computed " + str(len(roots)) + " roots of " + f_val.__name__
if len(roots) < 8:
    for root in roots:
        print "%.4f \t+\t%.4fi" %(root.real, root.imag)

# plot newton fractal
col_source = 'colourlovers'
# col_params = {'lover': 'joy_of_summer', 'keywords': 'I like your Smile', 'cmap':'spring', 'col_num':len(p)}
# col_params = {'lover': 'QitsuneQage', 'keywords': 'Almost Together', 'cmap':'jet', 'col_num':len(p)}
# col_params = {'lover': 'joy_of_summer', 'keywords': 'See The Light', 'cmap':'spectral', 'col_num':len(p)}
# col_params = {'lover': 'pseudo.cyborg', 'keywords': 'math music', 'cmap':'summer', 'col_num':len(p)}
# col_params = {'lover': 'silentHue', 'keywords': 'Mute Math EP', 'cmap':'winter', 'col_num':len(p)}
# col_params = {'lover': 'yakotta', 'keywords': 'blue hour', 'cmap':'gnuplot', 'col_num':len(p)}
# col_params = {'lover': 'owlies', 'keywords': 'endlessly.', 'cmap':'gnuplot', 'col_num':len(p)}
col_params = {'lover': 'justjessi', 'keywords': 'groovy kind of xmas', 'cmap':'gnuplot', 'col_num':256}
# col_params = {'lover': 'MarieBrandt', 'keywords': 'Barcelona', 'cmap':'gnuplot', 'col_num':len(p)}

colors = gn.config_colors(col_source, col_params)
save_path = "fractal_pictures/frac_40.png"
gn.newton_plot(con_root, con_num, colors, save_path)

# replace the above line with 
#		gn.newton_plot(con_num, con_num, colors, save_path)
# to color by number of iterations
