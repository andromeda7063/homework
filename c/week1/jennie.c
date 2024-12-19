// for a given integer, return its digits as words
// 1234 -> one two three four

#include <stdio.h>

const char* num2str(int num) {

    switch (num) {
        case 1:
            return "one ";
            break;

        case 2:
            return "two ";
            break;

        case 3:
            return "three ";
            break;

        case 4:
            return "four ";
            break;
        
        case 5:
            return "five ";
            break;

        case 6:
            return "six ";
            break;

        case 7:
            return "seven ";
            break;

        case 8:
            return "eight ";
            break;

        case 9:
            return "nine ";
            break;

        case 0:
            return "zero ";
            break;
    }
}

void main() {
    int input, k, d, rem, rev = 0;
    printf("enter a no: ");
    scanf("%d", &input);

    k = input;

    while (k != 0) {        // loop reverses a given number i.e, 1234 -> 4321
        rem = k % 10;
        rev = 10 * rev + rem;
        k = k / 10;
    }

    while (rev > 0) {
        d = rev % 10;

        printf("%s", num2str(d));

        rev = rev / 10;
    }

    printf("\n");
}