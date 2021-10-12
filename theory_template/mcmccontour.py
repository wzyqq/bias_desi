import numpy as np
import matplotlib.pyplot as plt
import corner

ndim = 2
data = np.loadtxt('chain')
data = data.reshape(50000,10,ndim)
#data = np.delete(data, 17, 1)
draw = data[:,:,:]
ka = np.loadtxt('ka_square')
ka_min = np.loadtxt('ka_min')
sample = (draw[10000:, np.where(ka[10000,:]<ka_min*1.05) , :].reshape([-1,ndim]))
#sample = data

#value1 = np.array([13.38, 0.60, 13.35, 14.20, 1.09, 400])
#value2 = np.mean(sample, axis=0)

figure = corner.corner(sample,bins=20,levels=(0.683,
# 0.954, 0.997
),
labels=[r"$\sigma$", r"$bias$"
],
smooth=True,
plot_datapoints=False,plot_contours=True,quantiles=[
#0.0013, 0.0228, 
0.1587, 
#0.5, 
0.8413, 
#0.9772, 0.9987
],
show_titles=True,title_kwargs={"fontsize": 10},label_kwargs={"fontsize": 5},title_fmt=".4f",contour_kwargs=dict(linewidths=3),
hist_kwargs=dict(linewidth=3))


axes = np.array(figure.axes).reshape((ndim, ndim))
# Loop over the diagonal
for i in range(ndim):
    ax = axes[i, i]
#    ax.axvline(value1[i], color="g")
    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)       
#    ax.axvline(value2[i], color="r")

# Loop over the histograms
for yi in range(ndim):
    for xi in range(yi):
        ax = axes[yi, xi]
#        ax.axvline(value1[xi], color="g")
#        ax.axvline(value2[xi], color="r")
#        ax.axhline(value1[yi], color="g")
#        ax.axhline(value2[yi], color="r")
#        ax.plot(value1[xi], value1[yi], "sg")
#        ax.plot(value2[xi], value2[yi], "sr")
        ax.spines['top'].set_linewidth(2)
        ax.spines['right'].set_linewidth(2)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['left'].set_linewidth(2) 

for xi in np.int_(np.linspace(1,ndim-1,ndim-1)):
    ax = axes[xi,0]
#    xtk = ax.get_xticks()
#    ax.set_xticklabels(xtk,fontweight='black')
    ytk = ax.get_yticks()
    ax.set_yticklabels(['%.3f'%y for y in ytk],fontweight='black',
      fontsize=4 )
#    xl  = ax.get_xlabel()
#    ax.set_xlabel(xl,fontweight='black')        
    yl  = ax.get_ylabel()
    ax.set_ylabel(yl,#fontweight='black'
        )    

for yi in range(ndim):
    ax = axes[ndim-1,yi]
    xtk = ax.get_xticks()
    ax.set_xticklabels(['%.3f'%x for x in xtk],fontweight='black',
      fontsize=4   )
#    ytk = ax.get_yticks()
#    ax.set_yticklabels(ytk,fontweight='black')
    xl  = ax.get_xlabel()
    ax.set_xlabel(xl,#fontweight='black',
        position=(0.5,-0.33))        
#    yl  = ax.get_ylabel()
#    ax.set_ylabel(yl,fontweight='black')          
#sigam_best = np.percentile(sample[:,0],50)
#sigam_less = np.percentile(sample[:,0],16)
#sigma_more = np.percentile(sample[:,0],84)
#bias_best = np.percentile(sample[:,1],50)
#bias_less = np.percentile(sample[:,1],16)
#bias_more = np.percentile(sample[:,1],84)
#print(sigam_best,sigam_less,sigma_more,bias_best,bias_less,bias_more)
np.savetxt('sample', sample, '%10.6lf')
figure.savefig('result.pdf')
