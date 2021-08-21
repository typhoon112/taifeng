#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "geodesic.h"

struct tfPoint {
    double lon, lat, pressure, power, movespeed;
};

double min(double a, double b) {
    return a < b ? a : b;
}

double sqr(double x) {
    return x * x;
}

double geodis(struct geod_geodesic *g, double lat1, double lon1, double lat2, double lon2) {
    double azi1, azi2, s12;
    geod_inverse(g, lat1, lon1, lat2, lon2, &s12, &azi1, &azi2);
    // printf("%lf %lf %lf %lf %lf\n", lat1, lon1, lat2, lon2, s12);
    return s12;
}

__declspec(dllexport) double dtwdis(int n, struct tfPoint a[], int m, struct tfPoint b[], double cofficients[5], int* cutoff) {
    double **dis = (double **)malloc(sizeof(double *) * n);
    if (*cutoff) {
        struct geod_geodesic g;
        geod_init(&g, 6378137.0, 1.0 / 298.257223563); // WGS84
        double alat = a[n - 1].lat, alon = a[n - 1].lon;
        double mins = geodis(&g, alat, alon, b[m - 1].lat, b[m - 1].lon), minj = m - 1, tdis;
        for (int j = m - 1; j >= 0; --j) {
            tdis = geodis(&g, alat, alon, b[j].lat, b[j].lon);
            if (tdis < mins) {
                mins = tdis;
                minj = j;
            }
        }
        m = minj;
        *cutoff = minj;
    }
    for (int i = 0; i < n; ++i)
        dis[i] = (double *)malloc(sizeof(double) * m);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            dis[i][j] = sqr(a[i].lon - b[j].lon) * cofficients[0]
                      + sqr(a[i].lat - b[j].lat) * cofficients[1]
                      + sqr(a[i].pressure - b[j].pressure) * cofficients[2]
                      + sqr(a[i].power - b[j].power) * cofficients[3]
                      + sqr(a[i].movespeed - b[j].movespeed) * cofficients[4];
    double **acc = (double **)malloc(sizeof(double *) * n);
    for (int i = 0; i < n; ++i)
        acc[i] = (double *)malloc(sizeof(double) * m);
    acc[0][0] = dis[0][0];
    for (int i = 1; i < n; ++i)
        acc[i][0] = dis[i][0] + acc[i - 1][0];
    for (int i = 1; i < m; ++i)
        acc[0][i] = dis[0][i] + acc[0][i - 1];
    for (int i = 1; i < n; ++i)
        for (int j = 1; j < m; ++j)
            acc[i][j] = min(acc[i - 1][j - 1], min(acc[i - 1][j], acc[i][j - 1])) + dis[i][j];
    double res = sqrt(acc[n - 1][m - 1]);
    for (int i = 0; i < n; ++i) {
        free(dis[i]);
        free(acc[i]);
    }
    free(dis);
    free(acc);
    if (m)
        return res;
    return 999999.0;
}