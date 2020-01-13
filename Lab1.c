#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<time.h>

float* euler_method(int t0, int y0, float delta_t);
float edo_original(float t);
float edo_resuelta(float t);
int main(){
  FILE *fp;
  int t0;
  int y0;
  int i, j;
  t0 = 0;
  y0 = 4;
  float delta_t[6] = {pow(10, -1), pow(10, -2), pow(10, -3), pow(10, -4),
                    pow(10, -5), pow(10, -6)};
  float* y;
  clock_t start_t, end_t, total_t;
  fp = fopen("1_a", "w");

  for(j = 0 ; j < 6 ; j++)
  {
  	fprintf(fp, "*********************************\n");
  	fprintf(fp, "Con delta = %f\n", delta_t[j]);
  	fprintf(fp, "*********************************\n");
    start_t = clock();
  	y = euler_method(t0, y0, delta_t[j]);
    end_t = clock();
  	for(i = 0 ; i <= (10 / delta_t[j])  - (1 / delta_t[j]); i++)
    {
    	fprintf(fp, "%f\n", (i + (1/delta_t[j])) * delta_t[j]);
      fprintf(fp, "y[%i]=%f   ,   %f\n", i, *(y + i), edo_resuelta((i + 1 / delta_t[j]) * delta_t[j]));
    }
    total_t = (double)(end_t - start_t)/ CLOCKS_PER_SEC;
    fprintf(fp, "Tiempo que demora en CPU = %f\n", total_t);
	free(y);

  }
  return 0;
}


float* euler_method(int t0, int y0, float delta_t){
  int i, j;
  int N = 10 / delta_t;
  float sum;
  float* y = (float*) malloc(sizeof(float) * N - (1 / delta_t - 1) * sizeof(float)); //Asignacion de memoria
  for(i = 1 / delta_t ; i <= N ; i++){ //Desde 1 / delta_t porque necesita empezar desde n=1, hasta n=10
  	sum = 0;
    for(j = 0 ; j <= i - 1 ; j++){//Sigue en j=0 porque necesita de esos valores para calcular los siguientes
      sum += edo_original(j*delta_t);
    }
    y[i - (int) (1 / delta_t)] = y0 + (delta_t * sum);
  }
  return y;
}

float edo_original(float t)
{
	return 9 * (powf(t, 2)) - 4 * t + 5;
}

float edo_resuelta(float t)
{
	return 3 * (powf(t, 3)) - 2 * (powf(t, 2)) + 5 * t + 4;
}
