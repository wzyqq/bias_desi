#include<stdio.h>
#include<stdlib.h>
#include"sigma.h"
int main()
{
	int i;
	double *w_analysis;
	w_analysis = (double *)malloc(wp_number*Perpendicular_min*sizeof(double));
	double init[ndemension]={0.2, 8};
	supplement();
	getwp(&init[0], w_analysis);

	for(i=0; i<wp_number*Perpendicular_min; i++)
	{
		printf("%lf\n", w_analysis[i]);
	}
	free(w_analysis);	
}