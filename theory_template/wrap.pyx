cdef extern from "sigma.h":
	
	void supplement()
	void getwp(double *param, double *w_analysis)
	void getwp2000(double *param, double *w_analysis)	
	void getwp_real(double *param, double *w_analysis_real)

import numpy as np

def supply():
	supplement()
	
def wp(para,analysiswp):

	if not para.flags['C_CONTIGUOUS']:
		para = np.ascontiguousarray(para)
	if not analysiswp.flags['C_CONTIGUOUS']:
		analysiswp = np.ascontiguousarray(analysiswp)
   
	cdef double[::1] para_memview = para
	cdef double[::1] analysiswp_memview = analysiswp

	getwp(&para_memview[0], &analysiswp_memview[0])

	return analysiswp

def wp2000(para,analysiswp):

	if not para.flags['C_CONTIGUOUS']:
		para = np.ascontiguousarray(para)
	if not analysiswp.flags['C_CONTIGUOUS']:
		analysiswp = np.ascontiguousarray(analysiswp)
   
	cdef double[::1] para_memview = para
	cdef double[::1] analysiswp_memview = analysiswp

	getwp2000(&para_memview[0], &analysiswp_memview[0])

	return analysiswp

def wp_real(para,analysiswp_real):

	if not para.flags['C_CONTIGUOUS']:
		para = np.ascontiguousarray(para)
	if not analysiswp_real.flags['C_CONTIGUOUS']:
		analysiswp_real = np.ascontiguousarray(analysiswp_real)
   
	cdef double[::1] para_memview = para
	cdef double[::1] analysiswp_real_memview = analysiswp_real

	getwp_real(&para_memview[0], &analysiswp_real_memview[0])

	return analysiswp_real

#from libc.stdio cimport printf