// print the times table of a given number

#include <stdio.h>

void main() {
    int n;
    printf("enter n: ");
    scanf("%d",&n);

    int i;

    for (i=1; i <= 15; i++) {
        printf("%d X %d = %d\n", n, i, n * i);
    }
}