#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<time.h>

__global__ void euler_method(float *y, float *sum, float delta_t, int N)
{
	int y0 = 4;
	int tId = threadIdx.x + blockIdx.x*blockDim.x;
	if(tId <= N){
			y[tId] = y0 + delta_t * sum[tId];
	}
}

float edo_resuelta(float t);
float edo_original(float t);
void sumatoria(float *sum, float delta_t, int N);

int main(){
	FILE *fp;
	int i, j, N, counter = 0;
  float delta_t[6] = {powf(10, -1), powf(10, -2), powf(10, -3), powf(10, -4),
                    powf(10, -5), powf(10, -6)};
  float *y, *y_dev, *sum, *sum_dev;
	int block_size, grid_size;
  fp = fopen("../1_c", "w");

	cudaEvent_t ct1, ct2;
	float dt;
	cudaEventCreate(&ct1); cudaEventCreate(&ct2);

  for(j = 0 ; j < 6 ; j++)
  {
  	fprintf(fp, "*********************************\n");
  	fprintf(fp, "Con delta = %f\n", delta_t[j]);
  	fprintf(fp, "*********************************\n");

		block_size = 256;
		N = 10 / delta_t[j];
		grid_size = (int)ceil((float)(N +1 )/ block_size);

		cudaMalloc(&y_dev, sizeof(float) * (N + 1));
		cudaMalloc(&sum_dev, sizeof(float) * (N + 1));
		sum = (float*) malloc(sizeof(float) * (N + 1));
		y = (float*) malloc(sizeof(float) * (N + 1));

		sumatoria(sum, delta_t[j], N);

		cudaEventRecord(ct1);
		cudaMemcpy(sum_dev, sum, (N + 1)*sizeof(float), cudaMemcpyHostToDevice);
  	euler_method<<<grid_size,block_size>>>(y_dev, sum_dev, delta_t[j], N);
		cudaEventRecord(ct2);
		cudaMemcpy(y, y_dev, (N + 1)*sizeof(float), cudaMemcpyDeviceToHost);
		cudaEventSynchronize(ct2);
		cudaEventElapsedTime(&dt, ct1, ct2);

  	for(i = 0 ; i <= N; i++)
    {
			fprintf(fp, "%f\n", i * delta_t[j]);
      fprintf(fp, "y[%i]=%f   ,   %f\n", i, *(y + i), edo_resuelta(i * delta_t[j]));
    }
		counter++; printf("Tiempo que demora en GPU = %f [ms] para delta numero %d\n", dt, counter);
		free(y);
		free(sum);
		cudaFree(y_dev);
  }
  return 0;
}

void sumatoria(float *sum, float delta_t, int N){
	sum[0] = edo_original(0);
	for(int i = 1; i <= N; i++){
		sum[i] = sum[i-1] + edo_original(i*delta_t);
	}
}

float edo_original(float t)
{
	return 9 * (powf(t, 2)) - 4 * t + 5;
}

float edo_resuelta(float t)
{
	return 3 * (powf(t, 3)) - 2 * (powf(t, 2)) + 5 * t + 4;
}
