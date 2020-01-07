#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

float* euler_method(int t0, int y0, double delta_t);


int main(){
  int t0 = 0, y0 = -1;
  double delta_t[6] = {pow(10,-1), pow(10,-2), pow(10,-3), pow(10,-4),
                    pow(10,-5), pow(10,-6)};
  float* y;
  y = euler_method(t0, y0, delta_t[0]);
  printf("%f", y[0]);
  free(y);
  return 0;
}

float* euler_method(int t0, int y0, double delta_t){
  int N = 10/delta_t;
  double sum_exp = 1;
  float* y = (float*) malloc(sizeof(float)*N); //Asignacion de memoria
  for(int i = 1; i <= N; i++){
    for(int j = 1; i<= i - 1; i++){
      sum_exp += exp(-j*delta_t);
    }
    y[i] = -1 + float(delta_t*sum_exp);
  }
  return y;
}
