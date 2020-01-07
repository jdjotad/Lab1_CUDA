#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>

typedef struct {
  float *R;
  float *G;
  float *B;
} RGB;

int euler_method(int t0, int y0, int delta_t);


int main(int argc, char* argv[]){
  int t0, y0;
  int delta_t[6] = {pow(10,-1), pow(10,-2), pow(10,-3), pow(10,-4),
                    pow(10,-5), pow(10,-6)};
  int* y_i;
  if(argc != 3){
    printf("Se debe ingresar t0 e y0\n", );
    return -1;
  }

  error = euler_method(t0, y0, delta_t[0]);
  return 0;
}

int euler_method(int t0, int y0, int delta_t){

}
