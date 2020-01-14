#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<time.h>

float* euler_method(int t0, int y0, float delta_t, int N);
float edo_original(float t);
float edo_resuelta(float t);
int main(){
  FILE *fp;
  int t0 = 0;
  int y0 = 4;
  int i, j;
  int N = 0;
  float delta_t[6] = {pow(10, -1), pow(10, -2), pow(10, -3), pow(10, -4),
                    pow(10, -5), pow(10, -6)};
  float* y;
  clock_t start_t, end_t, total_t;
  fp = fopen("../1_a", "w");
  int counter = 0;

  for(j = 0 ; j < 6 ; j++)
  {
  	fprintf(fp, "*********************************\n");
  	fprintf(fp, "Con delta = %f\n", delta_t[j]);
  	fprintf(fp, "*********************************\n");
    start_t = clock();
    N = 10 / delta_t[j];
  	y = euler_method(t0, y0, delta_t[j], N);
    end_t = clock();
  	for(i = 0 ; i <= N; i++)
    {
    	fprintf(fp, "%f\n", (i) * delta_t[j]);
      fprintf(fp, "y[%i]=%f   ,   %f\n", i, *(y + i), edo_resuelta(i * delta_t[j]));
      if(i == N){
        counter++;
        printf("Vez que paso termino de escribir n %d \n", counter);
      }
    }
    total_t = end_t - start_t;
    fprintf(fp, "Tiempo que demora en CPU = %f\n", (float)total_t/CLOCKS_PER_SEC );
	free(y);

  }
  return 0;
}


float* euler_method(int t0, int y0, float delta_t, int N){
  int i = 0;
  int j = 0;
  float sum = 0;
  float* y = (float*) malloc(sizeof(float) * (N + 1)); //Asignacion de memoria
  for(i = 0 ; i <= N ; i++, j++){ //Desde 1 / delta_t porque necesita empezar desde n=1, hasta n=10
      sum += edo_original(j*delta_t);
      y[i] = y0 + (delta_t * sum);
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
