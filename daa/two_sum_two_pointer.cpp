#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int arr[] = {2, 7, 5, 10, 3, 4, 6};
    int n = 7;
    int target = 9;

    sort(arr, arr+n);
    int left = 0, right = n - 1;
    bool found = false;

    while (left < right) {
        int sum = arr[left] + arr[right];

        if (sum == target) {
            cout << "Pair Found: " << arr[left] << " " << arr[right] << endl;
            found = true;
            left++;
            right--;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    if (!found)
        cout << "No pair found";

    return 0;
}
