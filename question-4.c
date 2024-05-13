#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>

#define N 1024  // Number of points
#define L 8.0   // Length of interval [-L, L]

int main() {
    double *x, *f, *f_hat;
    fftw_complex *f_hat_fft;
    fftw_plan plan_forward;

    // Allocate memory for arrays
    x = (double *)malloc(N * sizeof(double));
    f = (double *)malloc(N * sizeof(double));
    f_hat = (double *)malloc(N * sizeof(double));
    f_hat_fft = (fftw_complex *)fftw_malloc(N * sizeof(fftw_complex));

    // Define the Gaussian function
    for (int i = 0; i < N; i++) {
        x[i] = -L + i * (2 * L / N);
        f[i] = exp(-x[i]*x[i]);
    }

    // Create FFTW plan
    plan_forward = fftw_plan_dft_r2c_1d(N, f, f_hat_fft, FFTW_ESTIMATE);

    // Perform FFT
    fftw_execute(plan_forward);

    // Compute the Fourier transform magnitude
    for (int i = 0; i < N; i++) {
        f_hat[i] = sqrt(f_hat_fft[i][0]*f_hat_fft[i][0] + f_hat_fft[i][1]*f_hat_fft[i][1]) / N;
    }

    // Plot the results
    FILE *fp = fopen("fft_gaussian.dat", "w");
    for (int i = 0; i < N; i++) {
        fprintf(fp, "%f %f %f\n", x[i], f_hat[i], sqrt(M_PI) * exp(-M_PI * x[i] * x[i]));
    }
    fclose(fp);

    // Free allocated memory
    fftw_destroy_plan(plan_forward);
    fftw_free(f_hat_fft);
    free(x);
    free(f);
    free(f_hat);

    return 0;
}
