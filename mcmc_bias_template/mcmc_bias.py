import numpy as np
import emcee
import wrap
from multiprocessing import Pool



xi_start = 5
xi_point = 6
xi_point_all = 14
xi_number= 2

redshift	= 0.1
error_upper	= redshift*0.5
observe_xi 	= np.loadtxt("w_mean")
w_observe  	= (observe_xi.reshape(2,-1)[:,xi_start:xi_start+xi_point]).reshape(1,-1)
xi_covariance_inverse = np.loadtxt("inv_matrix_xi_diag_more")


analysisw=np.ones((xi_number*xi_point))
#diff_xi = np.zeros((xi_number*xi_point))

wrap.supply()


def log_prior(theta):
	sigma, bias = theta

	if 0.0001 < sigma < error_upper and 0.01 < bias < 10.0 :
		return 0.0

	return -np.inf

def log_likelihood(theta):
	sigma, bias = theta
#	print('theta=',theta)

	ka_square = 0

	wrap.wp(theta,analysisw)
#	print('analysisw=',analysisw)
	diff_xi = w_observe[0] - analysisw
#	print(diff_xi)
	ka_square = ka_square + np.dot( diff_xi,np.dot(xi_covariance_inverse,diff_xi) )
#	print('ka_square=',ka_square)

	return -0.5*(ka_square)

def log_probability(theta):
    lp = log_prior(theta)
    if(np.any(np.isnan(lp))):
    	print(theta)
    if not np.isfinite(lp):
    	return -np.inf, -np.inf
    ll = log_likelihood(theta)
    if(np.any(np.isnan(ll))):
    	print(theta)
    return lp + ll, ll*(-2)


nwalkers = 10
ndim = 2

pos0 = np.array([error_upper*0.5, 5.0])

init_mag=np.array([0.02,1.0])
#init_mag=np.zeros(ndim)
#pos = np.vstack([ pos0,np.repeat( np.array([pos0]),nwalkers-1,axis=0 ) ])
pos = np.vstack([ pos0,np.repeat( np.array([pos0]),nwalkers-1,axis=0 )+init_mag*np.random.randn(nwalkers-1, ndim) ])


with Pool(20) as pool:
#	move = emcee.moves.StretchMove(a=0.1)
#	sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, pool=pool, moves=[move])
	sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, pool=pool)
	sampler.run_mcmc(pos, 50000, progress=True)

likelihood_samps = sampler.get_blobs()
flat_samples = sampler.get_chain(discard=0, thin=1, flat=True)

np.savetxt('chain',flat_samples,'%12.6lf')
np.savetxt('ka_square',likelihood_samps,'%12.6lf')

print('at=',sampler.get_autocorr_time())
print('af=',sampler.acceptance_fraction)






