#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int value, weight, index;
};

bool compare(Item a, Item b) {
    return (double)a.value / a.weight > (double)b.value / b.weight;
}

double fractionalKnapsack(int capacity, vector<Item> &items) {
    sort(items.begin(), items.end(), compare);

    double totalValue = 0;

    cout << "Items Selected:\n";

    for (auto item : items) {
        if (capacity >= item.weight) {
            capacity -= item.weight;
            totalValue += item.value;

            cout << "Item " << item.index
                 << " (Value = " << item.value
                 << ", Weight = " << item.weight
                 << ") -> 100%\n";
        } else if (capacity > 0) {
            double fraction = (double)capacity / item.weight;
            totalValue += item.value * fraction;

            cout << "Item " << item.index
                 << " (Value = " << item.value
                 << ", Weight = " << item.weight
                 << ") -> " << fraction * 100 << "%\n";
            break;
        }
    }

    return totalValue;
}

int main() {
    vector<Item> items = {
        {6, 3, 1},
        {8, 2, 2},
        {1, 3, 3}
    };

    int capacity = 6;

    double maxValue = fractionalKnapsack(capacity, items);

    cout << "\nMaximum Value = " << maxValue << endl;

    return 0;
}
