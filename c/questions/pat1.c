// You are using GCC
#include <stdio.h>

int det(int matrix[3][3]) {
    int deter = 0;
    
    int a = matrix[0][0];
    int b = matrix[0][1];
    int c = matrix[0][2];
    int d = matrix[1][0];
    int e = matrix[1][1];
    int f = matrix[1][2];
    int g = matrix[2][0];
    int h = matrix[2][1];
    int i = matrix[2][2];
    
    deter = (a*(e*i-f*h)) - (b*(d*i-f*g)) + (c*(d*h-e*g));
    
    return deter;
}

int main() {
    int matrix[3][3];
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            scanf("%d", &matrix[i][j]);
        } 
    }
    printf("The matrix is:\n");
    for (int i = 0; i < 3; i++) {
        printf(" ");
        for (int j = 0; j < 3; j++) {
            printf("%d ", matrix[i][j]);
        } 
        printf("\n");
    }
    
    int d = det(matrix);
    printf("\n");
    
    printf("Determinant of the matrix is : %d\n", d);
    
    if (d <= 0) {
        printf("The system is unstable");
    }
    else {
        printf("The system is stable");
    }
    
    return 0;
}
