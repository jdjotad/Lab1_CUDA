#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

float* euler_method(int t0, int y0, float delta_t);
float edo_original(float t);
float edo_resuelta(float t);
int main(){
  int t0;
  int y0;
  int i;
  t0 = 0;
  y0 = 4;
  float delta_t[6] = {pow(10,-1), pow(10,-2), pow(10,-3), pow(10,-4),
                    pow(10,-5), pow(10,-6)};
  float* y;
  y = euler_method(t0, y0, delta_t[0]);
  for(i = 0 ; i <= 10/delta_t[0] - 10  ; i++)
  {
  	printf("%f\n", (i + 10)*delta_t[0]);
  	printf("y[%i]=%f   ,   %f\n", i, *(y+i), edo_resuelta((i + 10)*delta_t[0]));
  }
  printf("\n");
  free(y);
  return 0;
}

float* euler_method(int t0, int y0, float delta_t){
  int i, j;
  int N = 10 / delta_t;
  float sum;
  float* y = (float*) malloc(sizeof(float) * N - sizeof(float) * 9); //Asignacion de memoria
  for(i = 10 ; i <= N ; i++){ //Desde 10 porque necesita empezar desde n=1, hasta n=10
  	sum = 0;
    for(j = 0 ; j <= i - 1 ; j++){//Sigue en j=0 porque necesita de esos valores para calcular los siguientes
      sum += edo_original(j*delta_t);
    }
    y[i-10] = y0 + (delta_t * sum);
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