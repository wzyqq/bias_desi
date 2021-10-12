import numpy as np
import matplotlib.pyplot as plt
import wrap


ndim = 2
parallel_max = 2
perpendicular_max = 14
perpendicular_min = 6
xi_start = 5

analysisw=np.ones(parallel_max*perpendicular_min)
data   = np.loadtxt('chain').reshape(50000,10,ndim)
ka     = np.loadtxt('ka_square')

ka_min = np.min(ka[1000:])
para   = data[np.where(ka==ka_min)][0]

wrap.supply()
wrap.wp(para,analysisw)
'''
plt.figure(figsize=(12,12))

nbins 		= 14  
bins 		= np.logspace(-1, 1.7, nbins + 1) # rp cen  
binsdummy 	= np.log10(bins)  
r 	 		= 10**( (binsdummy[1:]+binsdummy[:-1])/2) 

x1 = r[xi_start:xi_start+perpendicular_min]
x2 = r

y1 = analysisw.reshape([parallel_max,perpendicular_min])
y2 = np.loadtxt('w_mean')

covariance_matrix  = np.loadtxt('covariance')
covariance         = covariance_matrix.reshape((parallel_max*perpendicular_max,parallel_max*perpendicular_max))
bar = np.zeros(parallel_max*perpendicular_max)
for i in range(parallel_max*perpendicular_max):
	bar[i] = np.sqrt(covariance[i][i])


plt.errorbar(x2, y2[0*perpendicular_max:0*perpendicular_max+perpendicular_max], yerr=bar[0*perpendicular_max:0*perpendicular_max+perpendicular_max], 
	markeredgewidth=1, barsabove=False, capthick=1 , elinewidth=3, capsize=5, marker='s', markerfacecolor='white',
markeredgecolor='r', markersize=5, color='r', linestyle='', label='$\\rm data(all),\pi_{max} = 50 h^{-1}Mpc$')

plt.errorbar(x2, y2[1*perpendicular_max:1*perpendicular_max+perpendicular_max], yerr=bar[1*perpendicular_max:1*perpendicular_max+perpendicular_max],
markeredgewidth=1, barsabove=False, capthick=1 , elinewidth=3, capsize=5, marker='s', markerfacecolor='white',
markeredgecolor='g',markersize=5, color='g', linestyle='', label='$\\rm data(all),\pi_{max} = 100 h^{-1}Mpc$')


plt.plot(x1,y1[0],color='r', linewidth=3, marker='_', label='$\\rm model, \pi_{max} = 50 h^{-1}Mpc$')
plt.plot(x1,y1[1],color='g', linewidth=3, marker='_', label='$\\rm model, \pi_{max} = 100 h^{-1}Mpc$')


plt.xscale('log')
plt.yscale('log',nonposy='clip')
	
plt.xlabel("$\\rm r_{p}\ (h^{-1}Mpc)$",fontsize=6)
plt.ylabel('$\\rm w_{p}(r_{p})\ (h^{-1}Mpc)$',fontsize=6)
plt.ylim(1,600)
plt.xticks(fontsize=5,fontweight='bold'
#,fontweight='black'
	)
plt.yticks(fontsize=5,fontweight='bold'
#,fontweight='black'
)
#plt.title('projected correlation functions',fontsize=30)
plt.title('xi')

ax = plt.gca()
xl = ax.get_xlabel()
#	ax.set_xlabel("$\\rm r_{p}\ (h^{-1}Mpc)$",fontweight='black',position=(0.5,0))  
#	ax.set_ylabel("$\\rm w_{p}(r_{p})\ (h^{-1}Mpc)$",fontweight='black',position=(0,0.4)
#		)  
tl = ax.get_title()
ax.set_title(tl,fontweight='black',position=(0.5,0.8),fontsize=5)  	
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.legend(fontsize=4,loc='lower left')

#plt.tight_layout(2)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0, hspace=0)
plt.show()
'''
np.savetxt('w_analysis', analysisw, 			'%12.6lf')
np.savetxt('ka_min',     np.array([ka_min]),    '%12.6lf')
np.savetxt('sigma_bias', para,     				'%12.6lf')
