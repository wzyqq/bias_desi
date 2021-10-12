cdef extern from "sigma.h":
	
	void supplement()
	void getwp(double *param, double *w_analysis)

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

#from libc.stdio cimport printf