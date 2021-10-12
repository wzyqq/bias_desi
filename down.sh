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

mkdir corr
cd corr

for ((i=0; i<20; i=i+1))
do
	mkdir "${suffix1[i]}${suffix2[i]}"
	cd    "${suffix1[i]}${suffix2[i]}"
	path="wzyqqq:/home/publicdata/hjxu/dr8/lumin_z_bin_files_wspecz_nocolorcut_planck2018/${suffix1[i]}${suffix2[i]}/wp_jkf.npz"
	scp $path ./
	cd ..
done