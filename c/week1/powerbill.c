// returns the power bill based on input conditions

#include <stdio.h>

void main() {
    char type; float r100, r200, r500, rall, bill;
    printf("enter type: ");
    scanf("%c", &type);

    float units;
    printf("enter units: ");
    scanf("%f", &units);

    if (type == 'D' || type == 'd') {
        r100 = 1;
        r200 = 2.5;
        r500 = 4;
        rall = 6;
    }

    else if (type == 'C' || type == 'c') {
        r100 = 2;
        r200 = 4.5;
        r500 = 6;
        rall = 7;
    }

    if (units > 500) {
        bill = 100*r100 + 100*r200 + 300*r500 + (units-500)*rall;
    }

    else if (units > 200 && units <= 500) {
        bill = 100*r100 + 100*r200 + (units-200)*r500 ;
    }

    else if (units > 100 && units <= 200) {
        bill = 100*r100 + (units-100)*r200;
    }

    else {
        bill = units*r100;
    }

    printf("bill is rs.%.2f\n", bill);
}