import numpy as np
from numpy.linalg import inv

suffix1 = ['z_0.1_0.3_absz', 'z_0.1_0.3_absz', 'z_0.1_0.3_absz', 
'z_0.2_0.4_absz', 'z_0.2_0.4_absz', 'z_0.2_0.4_absz', 'z_0.2_0.4_absz',  
'z_0.3_0.5_absz', 'z_0.3_0.5_absz', 'z_0.3_0.5_absz', 
'z_0.4_0.6_absz', 'z_0.4_0.6_absz', 'z_0.4_0.6_absz',
'z_0.5_0.7_absz', 'z_0.5_0.7_absz', 'z_0.5_0.7_absz', 
'z_0.6_0.8_absz', 'z_0.6_0.8_absz', 
'z_0.7_0.9_absz',
'z_0.8_1.0_absz']
suffix2 = ['_-20.0_-21.0', '_-21.0_-22.0', '_-22.0_-23.0',
'_-20.0_-20.5', '_-20.5_-21.0', '_-21.0_-22.0', '_-22.0_-23.0',
'_-20.5_-21.0', '_-21.0_-22.0', '_-22.0_-23.0', 
'_-21.0_-21.5', '_-21.5_-22.0', '_-22.0_-23.0', 
'_-21.0_-21.5', '_-21.5_-22.0', '_-22.0_-23.0',
'_-21.5_-22.0', '_-22.0_-23.0',
'_-22.0_-23.0',
'_-22.0_-23.0']

points = 6
parallel_max = 2
perpendicular_max = 14

for m in range(20):
	suffix = suffix1[m]+suffix2[m]
	covariance = np.zeros((points*parallel_max,points*parallel_max))
	covariance_inverse = np.zeros((points*parallel_max,points*parallel_max))
	covariance_old = np.loadtxt('corr/%s/covariance'%suffix)
	for i in range(points*parallel_max):
		for j in range(points*parallel_max):
			covariance[i][j] = covariance_old[int(i/points)*perpendicular_max+5+i%points,int(j/points)*perpendicular_max+5+j%points]
	covariance_inverse = inv(np.diag(np.diag(covariance)))
	np.savetxt('corr/%s/inv_matrix_xi_diag_more'%suffix, covariance_inverse, fmt='%.8f')