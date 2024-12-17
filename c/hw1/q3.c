#include <stdio.h>

void main() {
    int a, b;

    printf("enter a: ");
    scanf("%d",&a);

    printf("enter b: ");
    scanf("%d",&b);

    if (a > b) {
        printf("%d (a) is greater than %d (b)\n", a, b);
    }

    else if (b > a) {
        printf("%d (b) is greater than %d (a)\n", b, a);
    }

    else {
        printf("both %d (a) and %d (b) are equal\n", a, b);
    }
}