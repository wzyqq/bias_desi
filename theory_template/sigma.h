#ifndef __SIGMA_H__
#define __SIGMA_H__

#define r_num  431
#define node   16
#define node_pho 1000
#define node_pho_more 1000
#define pi     3.141592653589793
#define sqrt_2pi   2.506628275
#define perpendicular_max   14
#define wp_number  2
#define wp_real_number  1
#define ndemension  2
#define distance_number 1600001

extern char Linear_matter_power_spectrum[200];     
extern int  Start_point;
extern int  Perpendicular_min;	
extern char Wp_mean[200];
extern char Inverse_matrix[200];
extern double Xi_redshift;
extern int K_num;
extern double Omega_m0;
extern double Omega_lambda0;

extern double Xi[node],Wi[node];
extern double R_corr[r_num];
extern double *K, *Pkl;
extern double *Perpendicular;
extern double Corr_mm[r_num]; 


double approximation(double pa_in, double pe_in);
void getwp(double *param, double *w_analysis);
void getwp2000(double *param, double *w_analysis);
void getwp_real(double *param, double *w_analysis_real);
void supplement(void);



struct Linear
{		
	double kl_r;
	double pkl_r;
};

struct z_distance
{
	double redshift, distance;
};

struct z_distance Distance_data[distance_number];

#endif
