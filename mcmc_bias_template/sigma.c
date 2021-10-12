#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <gsl/gsl_math.h>
#include <gsl/gsl_integration.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_spline.h>
#include <gsl/gsl_sf_erf.h>
#include <gsl/gsl_sf_expint.h>
#include <unistd.h>
#include "sigma.h"

void supplement(void)
{

	struct Linear *li;
	int i, j, num;
	double xi_res[node]={0},wi_res[node]={0};

	FILE *fl;
	FILE *parafile;
	FILE *fdistance;


	parafile = fopen("infile","r");
	fscanf(parafile, "%s ", Linear_matter_power_spectrum);	
	fscanf(parafile, "%d",  &Start_point);
	fscanf(parafile, "%d",  &Perpendicular_min);	
	fscanf(parafile, "%s",  Wp_mean);	
	fscanf(parafile, "%s",  Inverse_matrix);	
	fscanf(parafile, "%lf", &Xi_redshift);
	fscanf(parafile, "%d",  &K_num);	
	fscanf(parafile, "%lf", &Omega_m0);	
	fscanf(parafile, "%lf", &Omega_lambda0);	

	K = (double *)malloc(K_num*sizeof(double));
	Pkl = (double *)malloc(K_num*sizeof(double));
	Perpendicular = (double *)malloc(Perpendicular_min*sizeof(double));
	li = (struct Linear *)malloc(K_num*sizeof(struct Linear));

	fl = fopen(Linear_matter_power_spectrum, "r");
	if(fl ==NULL)printf("cao");

	for(i=0; i<K_num; i++)
	{
		fscanf(fl, "%lf%lf", &li[i].kl_r, &li[i].pkl_r);
		K[i] = li[i].kl_r;
		Pkl[i] = li[i].pkl_r;
//		printf("%14.4le\t%14.4le\t%14.4le\n", k[i], pkl[i], pk[i]);
	}
	fclose(parafile);
	fclose(fl);

	fdistance = fopen("redshift_distance","r");
	for(i=0; i<distance_number; i++)
	{
		fscanf(fdistance, "%lf%lf", &Distance_data[i].redshift, &Distance_data[i].distance);
//		printf("%lf\t%lf\n", Distance_data[i].redshift, Distance_data[i].distance);
	}
	fclose(fdistance);

	for(i=0; i<r_num; i++)
	{
		R_corr[i] = pow(10,(0.01*i -1.0));
		Corr_mm[i]= 0;
	}

	gsl_interp_accel *acc1= gsl_interp_accel_alloc ();
	gsl_spline *spline1= gsl_spline_alloc (gsl_interp_cspline, K_num);
	gsl_spline_init (spline1, K, Pkl, K_num);
	gsl_integration_glfixed_table *table = gsl_integration_glfixed_table_alloc(node);

	for(num=0; num<node; num++)
	{
		gsl_integration_glfixed_point(0,2*pi,num,&Xi[num],&Wi[num],table);
//		printf("%lf\t%lf\n", Xi[num], Wi[num]);
	}

	for(j=0; j<100; j++)
	{
		for(i=0; i<100; i++)
		{	
			for(num=0; num<node; num++)
			{
				xi_res[num] = Xi[num] + 2*pi*i;
				wi_res[num] = Wi[num];
				Corr_mm[j] = Corr_mm[j] + wi_res[num]*xi_res[num]/R_corr[j]/R_corr[j]/R_corr[j]*gsl_spline_eval(spline1, xi_res[num]/R_corr[j], acc1)*sin(xi_res[num]);
			}
		}
		Corr_mm[j] = Corr_mm[j]/2.0/pi/pi;
//		printf("%d\t%.8lf\n", j, Corr_mm[j]);
	}
	for(j=100; j<150; j++)
	{
		for(i=0; i<1000; i++)
		{	
			for(num=0; num<node; num++)
			{
				xi_res[num] = Xi[num] + 2*pi*i;
				wi_res[num] = Wi[num];
				Corr_mm[j] = Corr_mm[j] + wi_res[num]*xi_res[num]/R_corr[j]/R_corr[j]/R_corr[j]*gsl_spline_eval(spline1, xi_res[num]/R_corr[j], acc1)*sin(xi_res[num]);
			}
		}
		Corr_mm[j] = Corr_mm[j]/2.0/pi/pi;
//		printf("%d\t%.8lf\n", j, Corr_mm[j]);
	}
	for(j=150; j<200; j++)
	{
		for(i=0; i<1000; i++)
		{	
			for(num=0; num<node; num++)
			{
				xi_res[num] = Xi[num] + 2*pi*i;
				wi_res[num] = Wi[num];
				Corr_mm[j] = Corr_mm[j] + wi_res[num]*xi_res[num]/R_corr[j]/R_corr[j]/R_corr[j]*gsl_spline_eval(spline1, xi_res[num]/R_corr[j], acc1)*sin(xi_res[num]);
			}
		}
		Corr_mm[j] = Corr_mm[j]/2.0/pi/pi;
//		printf("%d\t%.8lf\n", j, Corr_mm[j]);
	}
	for(j=200; j<300; j++)
	{
		for(i=0; i<3000; i++)
		{	
			for(num=0; num<node; num++)
			{
				xi_res[num] = Xi[num] + 2*pi*i;
				wi_res[num] = Wi[num];
				Corr_mm[j] = Corr_mm[j] + wi_res[num]*xi_res[num]/R_corr[j]/R_corr[j]/R_corr[j]*gsl_spline_eval(spline1, xi_res[num]/R_corr[j], acc1)*sin(xi_res[num]);
			}
		}
		Corr_mm[j] = Corr_mm[j]/2.0/pi/pi;
//		printf("%d\t%.8lf\n", j, Corr_mm[j]);
	}
	for(j=300; j<r_num; j++)
	{
		for(i=0; i<5000; i++)
		{	
			for(num=0; num<node; num++)
			{
				xi_res[num] = Xi[num] + 2*pi*i;
				wi_res[num] = Wi[num];
				Corr_mm[j] = Corr_mm[j] + wi_res[num]*xi_res[num]/R_corr[j]/R_corr[j]/R_corr[j]*gsl_spline_eval(spline1, xi_res[num]/R_corr[j], acc1)*sin(xi_res[num]);
			}
		}
		Corr_mm[j] = Corr_mm[j]/2.0/pi/pi;
//		printf("%d\t%.8lf\n", j, Corr_mm[j]);
	}

//	for(j=0; j<r_num; j++)
//	{
//		printf("%d\t%.8lf\n", j, Corr_mm[j]);
//	}


	gsl_spline_free (spline1);
	gsl_interp_accel_free (acc1);



	for(i=0; i<Perpendicular_min; i++)
	{
		Perpendicular[i] = pow(10.0,0.5*( (27.0/140.0*i+27.0/140.0*Start_point-1.0)+(27.0/140.0*i+27.0/140.0*Start_point-113.0/140.0) ) ) ;
//		printf("Perpendicular[%d]=%lf\n", i, Perpendicular[i]);
	}

//---------------------------------------------------start MCMC----------------------------------------------------------

}


double approximation(double pa_in, double pe_in)
{
		double distance;
		int loc;
		distance = sqrt(pow(pe_in,2)+pow(pa_in,2));
		loc = (int)(log10(distance)/0.01+100.5);
		if (loc>=r_num) loc = r_num-1;
		return loc;		
}

void getwp(double *param, double *w_analysis)
{
	int i, j, num, pa, pe, m, s;
	int location;
	int high_limit;
	double *xi_s;
	double error,bias;
	double phoxi[node_pho]={0};
	double phowi[node_pho]={0};
	double *w1, *w2, *w;	
	double *corr_y;
	double temp_error_distance_high, temp_error_distance_low, error_distance_high, 
	error_distance_low, error_distance;
	int loc_error_distance_high, loc_error_distance_low;
	gsl_integration_glfixed_table *table_pho;

	table_pho = gsl_integration_glfixed_table_alloc(node_pho);

	error = *(param+0);
	bias = *(param+1);
//	printf("error = %lf\tbias = %lf\n", error, bias);

	temp_error_distance_high = Xi_redshift+error*(1+Xi_redshift)*0.5;
	temp_error_distance_low  = Xi_redshift-error*(1+Xi_redshift)*0.5;
	loc_error_distance_high  = (int)(( temp_error_distance_high )*1000000 + 0.5);
	loc_error_distance_low   = (int)(( temp_error_distance_low  )*1000000 + 0.5);
	error_distance_high      = Distance_data[ loc_error_distance_high ].distance;
	error_distance_low       = Distance_data[ loc_error_distance_low  ].distance;
	error_distance           = (error_distance_high - error_distance_low)*sqrt(2);
//	printf("j=%d\t%lf\t%lf\t%d\t%d\t\n", j, temp_error_distance_high, temp_error_distance_low, loc_error_distance_high, 
//		loc_error_distance_low);
//	printf("error_distance=%lf\n", error_distance);


	xi_s = (double *)malloc(node_pho*Perpendicular_min*sizeof(double));
	w1   = (double *)malloc(wp_number*Perpendicular_min*sizeof(double));
	w2   = (double *)malloc(wp_number*Perpendicular_min*sizeof(double));
	w    = (double *)malloc(wp_number*Perpendicular_min*sizeof(double));
    corr_y = (double *)malloc(node_pho*sizeof(double));

	for(i=0; i<wp_number*Perpendicular_min; i++)	
	{ 
		w1[i]=0;
		w2[i]=0;
		w[i]=0;
	}

	for(m=1; m<=wp_number; m++)
	{
		num = m-1;
		high_limit=50*m;


		for(i=0; i<node_pho; i++)
		{
			gsl_integration_glfixed_point(0,high_limit,i,&phoxi[i],&phowi[i],table_pho);
//			printf("%lf\t%lf\n", phoxi[i], phowi[i]);
		}

		for(pe = 0; pe<Perpendicular_min; pe++)
		{	
			for(pa = 0; pa<node_pho; pa++)		
			{	
				location=approximation(Perpendicular[pe],phoxi[pa]);
				xi_s[pe*node_pho+pa]=Corr_mm[location];
//				printf("xi_s[%d][%d]=%lf\n", pe, pa, xi_s[pe*node_pho+pa] );
			}
		}    


		for(j=0; j<Perpendicular_min; j++)			
		{

			for(s=0; s<node_pho; s++)
			{
				corr_y[s] = xi_s[j*node_pho+s];
//				printf("corry[%d]=%lf\n", s, corr_y[s]);
			}

			gsl_interp_accel *acc9 = gsl_interp_accel_alloc ();
			gsl_spline *spline9 = gsl_spline_alloc (gsl_interp_cspline, node_pho);
			gsl_spline_init (spline9, phoxi, corr_y, node_pho);

			for(i=0; i<node_pho; i++)		
			{ 	
				w1[num*Perpendicular_min+j] = w1[num*Perpendicular_min+j]+gsl_spline_eval(spline9, phoxi[i], acc9)*gsl_sf_erf( (high_limit+phoxi[i])/sqrt(2)/error_distance )*phowi[i];
//				w2[num][j] = w2[num][j]+corr_2d[i][j]*2;
//				printf("node=%d\tw1[%d][%d]=%lf\n", i, num, j, w1[num*Perpendicular_min+j]);

			}
			for(i=0; i<node_pho; i++)
			{
				w2[num*Perpendicular_min+j] = w2[num*Perpendicular_min+j]+gsl_spline_eval(spline9, phoxi[i], acc9)*gsl_sf_erf( (high_limit-phoxi[i])/sqrt(2)/error_distance )*phowi[i];
//				printf("node=%d\tw2[%d][%d]=%lf\n", i, num, j, w2[num*Perpendicular_min+j]);
			}	
			
			w[num*Perpendicular_min+j] = w1[num*Perpendicular_min+j] + w2[num*Perpendicular_min+j]; 		
//			printf("w[%d][%d]=%lf\t%lf\t%lf\n", num, j, w1[num*Perpendicular_min+j], w2[num*Perpendicular_min+j], w[num*Perpendicular_min+j]);
		

			gsl_spline_free (spline9);
			gsl_interp_accel_free (acc9);	
		}
	
	}


	for(i=0; i<wp_number*Perpendicular_min; i++)
	{
		w_analysis[i] = bias*bias*w[i];
//		printf("w[%d]=%lf\tw_analysis[%d]=%lf\n", i, w[i], i, w_analysis[i]);		
	}

	free(xi_s);
	free(corr_y);	
	free(w1);
	free(w2);
	free(w);
}
