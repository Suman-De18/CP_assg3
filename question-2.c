#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>

#define N 1000 // Number of samples
#define PI 3.14159265358979323846

// Define the sinc function
double sinc(double x) {
    return sin(PI * x) / (PI * x);
}

int main() {
    // Generate x values for the sinc function
    double x_values[N];
    for (int i = 0; i < N; ++i) {
        x_values[i] = -10.0 + 20.0 * i / (N - 1);
    }

    // Compute the sinc function values
    double y_values[N];
    for (int i = 0; i < N; ++i) {
        y_values[i] = sinc(x_values[i]);
    }

    // Compute the Fourier transform using FFTW
    fftw_complex* in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    fftw_complex* out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);

    fftw_plan plan = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    for (int i = 0; i < N; ++i) {
        in[i][0] = y_values[i];
        in[i][1] = 0.0;
    }

    fftw_execute(plan);

    // Overlay the Fourier transform on the sinc function plot
    for (int i = 0; i < N; ++i) {
        printf("Frequency: %d, Fourier Transform: %f\n", i, out[i][0]);
    }

    // Clean up
    fftw_destroy_plan(plan);
    fftw_free(in);
    fftw_free(out);

    return 0;
}
