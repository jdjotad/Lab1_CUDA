#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<time.h>

__device__ float edo_original(float t)
{
	return 9 * (powf(t, 2)) - 4 * t + 5;
}

__global__ void euler_method_gpu(float t, float *y, float delta_t, float m)
{
	int tId = threadIdx.x + blockIdx.x*blockDim.x;
	if(tId < (int) m){
  	y[tId] = y[tId] + delta_t*(4*t - y[tId] + 3 + tId);
	}
}
void euler_method(float t, float *y, int m, float delta_t);
float edo_resuelta(float t, int j);

int main(){
  FILE *fp_time;
  float *y, *y_dev;
  clock_t start_t, end_t, total_t;
  cudaEvent_t ct1, ct2;
  int j, k, counter = 0;
  int block_size, grid_size;
  float m[5] = {powf(10, 4), powf(10, 5), powf(10, 6), powf(10, 7), powf(10, 8)};
  int N = (int) powf(10,3);
  float delta_t = powf(10,-3);
  float time[15];
	float t = 0;
  float dt;

  cudaEventCreate(&ct1); cudaEventCreate(&ct2);
  fp_time = fopen("2_time", "w");

  for(k = 0 ; k < 5 ; k++)
  {
    // Calcular valores iniciales
    y = (float*) malloc(sizeof(float)*m[k]);
    cudaMalloc(&y_dev, sizeof(float)*m[k]);
    for(j = 0; j < m[k]; j++){
      y[j] = j;
    }
    // Copiarlos a GPU
    cudaMemcpy(y_dev, y, m[k]*sizeof(float), cudaMemcpyHostToDevice);

    // CPU CODE
    start_t = clock();
		for(int i = 0; i < N ; i++){
			t = i*delta_t;
			euler_method(t, y, m[k], delta_t);
		}
    end_t = clock();
    total_t = end_t - start_t;
		counter++;
    // GPU CODE
    block_size = 256;
		grid_size = (int)ceil((float) m[k] / block_size);
    cudaEventRecord(ct1);
		for(int i = 0; i < N ; i++){
			t = i*delta_t;
			euler_method_gpu<<<grid_size,block_size>>>(t, y_dev, delta_t, m[k]);
		}
		cudaEventRecord(ct2);
		cudaMemcpy(y, y_dev, m[k]*sizeof(float), cudaMemcpyDeviceToHost);
		cudaEventSynchronize(ct2);
		cudaEventElapsedTime(&dt, ct1, ct2);
    /*
    for(j = 0; j < m[k]; j++){
      fprintf(fp, "Valor obtenido = %f , Valor real = %f j = %d\n", y[j], edo_resuelta(1,j), j+1);
    }
    */
    time[k] = (float) 1000*total_t/CLOCKS_PER_SEC;
    time[5 + k] = dt;
    //time[10 + k] = ;
    printf("Tiempo que demora en CPU = %f [ms] para m numero %d\n", ((float) 1000*total_t/CLOCKS_PER_SEC), counter);
    printf("Tiempo que demora en GPU = %f [ms] para m numero %d\n", dt, counter);
	  free(y);
    cudaFree(y_dev);
  }
  for(int i = 0; i < 15; i++){
    if((i%5 == 0) && (i != 0)){
      fprintf(fp_time, "\n");
    }
    fprintf(fp_time, "%f %f ",m[i%5], time[i]);
  }
  fclose(fp_time);
  return 0;
}


void euler_method(float t, float *y, int m, float delta_t){
  for(int j = 0; j < m ; j++){
      y[j] = y[j] + delta_t*(4*t - y[j] + 3 + j);
  }
}

float edo_resuelta(float t, int j)
{
	return expf(-t) + 4*t - 1 + j;
}
