#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<time.h>
__device__ float edo_original(float t)
{
	return 9 * (powf(t, 2)) - 4 * t + 5;
}

__global__ void euler_method(float *y, float delta_t, int N)
{
	int y0 = 4;
	int tId = threadIdx.x + blockIdx.x*blockDim.x;
	float sum = 0;
	if(tId < N){
		for(int i = 0, j = 0; i <= tId ; i++, j++){ //Desde 1 / delta_t porque necesita empezar desde n=1, hasta n=10
				sum += edo_original(j*delta_t);
				y[i] = y0 + (delta_t * sum);
		}
	}
}

float edo_resuelta(float t);

int main(){
	FILE *fp;
	int i, j, N, counter = 0;
  float delta_t[6] = {powf(10, -1), powf(10, -2), powf(10, -3), powf(10, -4),
                    powf(10, -5), powf(10, -6)};
  float *y, *y_dev;
	int block_size, grid_size;
  fp = fopen("../1_b", "w");

	cudaEvent_t ct1, ct2;
	float dt;
	cudaEventCreate(&ct1); cudaEventCreate(&ct2);

  for(j = 0 ; j < 6 ; j++)
  {
		block_size = 256; N = 10 / delta_t[j];
		grid_size = (int)ceil((float)N/ block_size);

		cudaMalloc(&y_dev, sizeof(float) * N);
		y = (float*) malloc(sizeof(float) * N);

		cudaEventRecord(ct1);
  	euler_method<<<grid_size,block_size>>>(y_dev, delta_t[j], N);
		cudaEventRecord(ct2);
		cudaMemcpy(y, y_dev, N *sizeof(float), cudaMemcpyDeviceToHost);
		cudaEventSynchronize(ct2);
		cudaEventElapsedTime(&dt, ct1, ct2);

		fprintf(fp, "*********************************\n");
		fprintf(fp, "Con delta = %f\n", delta_t[j]);
		fprintf(fp, "*********************************\n");
  	for(i = 0 ; i < N; i++)
    {
			fprintf(fp, "t = %f\n", i+1 * delta_t[j]);
      fprintf(fp, "y[%i]=%f , %f\n", i + 1, *(y + i), edo_resuelta((i+1) * delta_t[j]));
    }
		counter++; printf("Tiempo que demora en GPU = %f [ms] para delta numero %d\n", dt, counter);
		free(y);
		cudaFree(y_dev);
  }
  return 0;
}

float edo_resuelta(float t)
{
	return 3 * (powf(t, 3)) - 2 * (powf(t, 2)) + 5 * t + 4;
}
