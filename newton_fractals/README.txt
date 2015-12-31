Plug and Chug
Post 1: Newton Fractals
Chris Harshaw

Thanks for visiting my blog, Plug and Chug! This READ ME file 
covers the code used in the post, "Newton Fractals".

Required Software:
===================================
Python 2.7, packages include
	- numpy
	- PIL
	- matplotlib
	- colourlovers

ffmpeg, used for encoding videos: https://www.ffmpeg.org/
I used the libx264 encoder. Here are steps to compile it
https://trac.ffmpeg.org/wiki/How%20to%20quickly%20compile%20libx264

Description of Files
===================================
general_newton.py
	- runs newton's method for an array of complex numbers
	- visualizes results of newton's method
	- uses array processing for fast computations

newton_driver.py
	- driver for newton's method
	- creates single visualizations

newton_movie.py
	- creates videos of newton fractals by changing parameter alpha

newton_movie2.py
	- creates videos of newton fractals by parametrizing the roots 
		of a polynomial

test_fun.py
	- contains functions to run Newton's method on