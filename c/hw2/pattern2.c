// print some other pattern

#include <stdio.h>

void main() {
    int n;
    printf("enter n: ");
    scanf("%d", &n);

    int i, j;

    for (i = 1; i <= n; i++) {
        
        for (j = 1; j <= i; j++) {

            printf("%d ", j);
        }

        printf("\n");
    }

}