#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

float* euler_method(int t0, int y0, double delta_t);


int main(){
  int t0;
  int y0;
  int i;
  t0 = 0;
  y0 = 4;
  double delta_t[6] = {pow(10,-1), pow(10,-2), pow(10,-3), pow(10,-4),
                    pow(10,-5), pow(10,-6)};
  float* y;
  y = euler_method(t0, y0, delta_t[0]);
  for(i = 0 ; i < 10/delta_t[0]  ; i++)
  {
  	printf("y[%i]=%f\n", i, *(y+i));
  }
  printf("\n");
  free(y);
  return 0;
}


float* euler_method(int t0, int y0, double delta_t){
  int i, j;
  int N = 10/delta_t;
  float sum_exp = 1;
  float* y = (float*) malloc(sizeof(float)*N); //Asignacion de memoria
  for(i = 0 ; i < N ; i++){
    for(j = 0 ; j <= i - 1 ; j++){
      sum_exp += exp(-j*delta_t);
    }
    y[i] = -y0 + (delta_t*sum_exp);
  }
  return y;
}