// header snippet

#include <iostream>
#include <vector>
using namespace std;

// code snippet 

void printSnakePattern(const vector<vector<int>>& matrix) {
    // Enter your code here
    int rows = matrix.size();
    int cols = matrix[0].size();

    for (int i = 0; i < rows; i++) {
        if (i % 2 == 0) {
            for (int j = 0; j < cols; j++) {
                cout << matrix[i][j] << " " << endl;
            }
        }

        else {
            for (int j = cols - 1; j >= 0; j--) {
                cout << matrix[i][j] << " " << endl;
            }
        }
    }
}
// footer snippet

int main() {
    int rows, cols;
    cout << "enter number of rows and columns: ";
    cin >> rows >> cols;

    vector<vector<int>> matrix(rows, vector<int>(cols));

    cout << "enter the matrix elements:\n";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> matrix[i][j];
        }
    }

    cout << "snake Pattern:\n";
    printSnakePattern(matrix);

    return 0;
}
