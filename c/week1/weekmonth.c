// return weekday and no of days in a month based on user input using a switch statement

#include <stdio.h>

void main() {
    int week, month;
    printf("enter week: ");
    scanf("%d", &week);

    printf("enter month: ");
    scanf("%d", &month);

    switch (week) {
        // following the french convention of starting a week on monday
        case 1:
            printf("monday\n");
            break;

        case 2:
            printf("tuesday\n");
            break;

        case 3:
            printf("wednesday\n");
            break;

        case 4:
            printf("thursday\n");
            break;
        
        case 5:
            printf("friday\n");
            break;

        case 6:
            printf("saturday\n");
            break;

        case 7:
            printf("sunday\n");
            break;
    }

    switch (month) {
        case 1:
            printf("31\n");
            break;

        case 2:
            printf("28 or 29\n");
            break;

        case 3:
            printf("31\n");
            break;

        case 4:
            printf("30\n");
            break;
        
        case 5:
            printf("31\n");
            break;

        case 6:
            printf("30\n");
            break;

        case 7:
            printf("31\n");
            break;

        case 8:
            printf("31\n");
            break;

        case 9:
            printf("30\n");
            break;

        case 10:
            printf("31\n");
            break;

        case 11:
            printf("30\n");
            break;
        
        case 12:
            printf("31\n");
            break;

        default:
            printf("invalid input\n");
    }

}