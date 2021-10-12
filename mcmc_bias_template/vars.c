#include "sigma.h"
char Linear_matter_power_spectrum[200];     
int  Start_point;
int  Perpendicular_min;	
char Wp_mean[200];
char Inverse_matrix[200];
double Xi_redshift;
int K_num;
double Omega_m0;
double Omega_lambda0;

double Xi[node]={0},Wi[node]={0};
double R_corr[r_num]={0};
double *K, *Pkl;
double *Perpendicular;
double Corr_mm[r_num]={0}; 