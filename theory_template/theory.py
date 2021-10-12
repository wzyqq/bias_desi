import numpy as np
import wrap


xi_start = 0
xi_point = 14
xi_point_all = 14
xi_number= 2

redshift    = 0.2
error_upper	= redshift*0.5
observe_xi 	= np.loadtxt("w_mean")
w_observe  	= (observe_xi.reshape(2,-1)[:,xi_start:xi_start+xi_point]).reshape(1,-1)


#diff_xi = np.zeros((xi_number*xi_point))

wrap.supply()
pos0 = np.loadtxt('sigma_bias')

analysisw=np.ones((xi_number*xi_point))
wrap.wp(pos0,analysisw)
print('analysisw=',analysisw)
np.savetxt('analysisw', analysisw, '%.6lf')

analysisw2000=np.ones((xi_point))
wrap.wp2000(pos0,analysisw2000)
print('analysisw2000=',analysisw2000)
np.savetxt('analysisw2000', analysisw2000, '%.6lf')

analysisw_real=np.ones((xi_point))
wrap.wp_real(pos0,analysisw_real)
print('analysisw_real=',analysisw_real)

w_real=analysisw_real*(w_observe/analysisw)[0,xi_point:]
np.savetxt('w_real', w_real, '%.6lf')

w_cov = np.loadtxt('covariance')
w_cov_real = np.sqrt(np.diag(w_cov))
np.savetxt('w_cov_real', w_cov_real, '%.6lf')








