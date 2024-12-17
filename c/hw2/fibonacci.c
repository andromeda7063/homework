// print the nth fibonacci number

#include <stdio.h>

void main() {
    int n;
    printf("enter n: ");
    scanf("%d",&n);

    if (n < 0) {
        printf("n cant be negative\n");
    }

    else {
        int a = 0, b = 1, c;

        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }

        printf("%d fibonacci number is: %d\n", n, b);
    }
}
