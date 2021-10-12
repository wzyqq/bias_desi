beginTime=`date +%s`


suffix1=('z_0.1_0.3_absz' 'z_0.1_0.3_absz' 'z_0.1_0.3_absz' 
'z_0.2_0.4_absz' 'z_0.2_0.4_absz' 'z_0.2_0.4_absz' 'z_0.2_0.4_absz'  
'z_0.3_0.5_absz' 'z_0.3_0.5_absz' 'z_0.3_0.5_absz' 
'z_0.4_0.6_absz' 'z_0.4_0.6_absz' 'z_0.4_0.6_absz'
'z_0.5_0.7_absz' 'z_0.5_0.7_absz' 'z_0.5_0.7_absz' 
'z_0.6_0.8_absz' 'z_0.6_0.8_absz' 
'z_0.7_0.9_absz'
'z_0.8_1.0_absz')
suffix2=('_-20.0_-21.0' '_-21.0_-22.0' '_-22.0_-23.0'
'_-20.0_-20.5' '_-20.5_-21.0' '_-21.0_-22.0' '_-22.0_-23.0'
'_-20.5_-21.0' '_-21.0_-22.0' '_-22.0_-23.0' 
'_-21.0_-21.5' '_-21.5_-22.0' '_-22.0_-23.0' 
'_-21.0_-21.5' '_-21.5_-22.0' '_-22.0_-23.0'
'_-21.5_-22.0' '_-22.0_-23.0'
'_-22.0_-23.0'
'_-22.0_-23.0')

redshift=(0.2 0.2 0.2 
0.3 0.3 0.3 0.3
0.4 0.4 0.4
0.5 0.5 0.5
0.6 0.6 0.6
0.7 0.7
0.8
0.9)

theory_template_path="/home/wzy/work/clf/dr8_planck18/all/theory_template"

mkdir theory
cd theory

for ((i=0; i<20; i=i+1))
do
	cp -r ${theory_template_path} "theory_${suffix1[i]}${suffix2[i]}" 
	cd "theory_${suffix1[i]}${suffix2[i]}" 

    dm_path="/home/wzy/work/CAMB-Jan2017/mdpl2_planck2018_matterpower${redshift[i]}.dat"
    xi_mean_path="/home/wzy/work/clf/dr8_planck18/all/corr/${suffix1[i]}${suffix2[i]}/w_mean"
    xi_inv_path="/home/wzy/work/clf/dr8_planck18/all/corr/${suffix1[i]}${suffix2[i]}/inv_matrix_xi_diag_more" 
    xi_cov_path="/home/wzy/work/clf/dr8_planck18/all/corr/${suffix1[i]}${suffix2[i]}/covariance" 
    para_path="/home/wzy/work/clf/dr8_planck18/all/mcmc/mcmc_${suffix1[i]}${suffix2[i]}/sigma_bias"

    cp $dm_path ./
    cp $xi_mean_path ./
    cp $xi_inv_path ./
    cp $xi_cov_path ./
    cp $para_path ./

    new_dm_path="mdpl2_planck2018_matterpower${redshift[i]}.dat"
	sed -i '1d' ${new_dm_path}
	sed -i "1c ${new_dm_path}" infile
    sed -i "6c ${redshift[i]}" infile    
	dm_length=`wc ${new_dm_path}`
	sed -i "7c ${dm_length%  *}" infile
#    errormax=$(printf "%.2f" `echo "scale=2; ${redshift[i]}*0.5" | bc`)
#    sed -i "13c redshift    = ${redshift[i]}" mcmc_bias.py
	cd ..
done

cd ..

endTime=`date +%s`
echo "总共耗时:" $(($endTime-$beginTime)) "秒"