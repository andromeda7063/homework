// print if a given number is an armstrong number or not

#include <stdio.h>
# include <math.h>      // compile with -lm flag

void main() {
    int n;
    printf("enter n: ");
    scanf("%d", &n);


    int sum = 0, k, l, d = n;

    while (d > 0) {
        l = d % 10;

        k = pow(l, 3);
        sum = sum + k;

        d = d / 10;
    }

    if (sum == n) {
        printf("%d is an armstrong number\n", n);
    }

    else {
        printf("%d is not an armstrong number. sum of its digits cubed is %d\n", n, sum);
    }
}