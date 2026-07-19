#include <iostream>
using namespace std;

int main() {
    int arr[] = {2, 7, 5, 10, 3, 4, 6};
    int n = 7;
    int target = 9;

    bool found = false;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == target) {
                cout << "Pair found: " << arr[i] << " " << arr[j] << endl;
                found = true;
            }
        }
    }

    if (!found)
        cout << "No pair found";

    return 0;
}
