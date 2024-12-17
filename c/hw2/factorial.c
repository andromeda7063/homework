// calculate factorial of a given number

#include <stdio.h>

void main() {
    int n;
    printf("enter n: ");
    scanf("%d",&n);

    int out = 1, i;

    for (i = 1; i <= n; i++) {
        out = out * i;
    }

    printf("factorial of %d is %d\n", n, out);
}