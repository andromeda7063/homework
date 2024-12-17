// calculate area with radius input
// compile with gcc -lm flag to link math library
// -lm flag links libm.a (?)

#include <stdio.h>
#include <math.h>

void main() {
    float pi, rad, area;

    pi = 3.1415926535897;

    printf("enter radius: ");
    scanf("%f",&rad);

    area = pi*pow(rad, 2);

    printf("area is %f \n", area);
}