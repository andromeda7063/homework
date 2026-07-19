#include <iostream>
#include <algorithm>
using namespace std;

struct Task {
    int id;
    int start;
    int finish;
};

bool helpSort(Task t1, Task t2) {
    return t1.finish < t2.finish;
}

int main() {
    Task tasks[] = {
        {1, 5, 9},
        {2, 1, 2},
        {3, 3, 4},
        {4, 0, 6},
        {5, 5, 7},
        {6, 8, 9}
    };

    int size = sizeof(tasks) / sizeof(tasks[0]);

    cout << "unsorted" << "\n";
    cout << "| " << "i" << " | " << "s" << " | " << "f" << " |\n";

    for (int i = 0; i < size; i++) {
        cout << "| " << tasks[i].id << " | " << tasks[i].start << " | " << tasks[i].finish << " |\n";
    }

    std::sort(tasks, tasks + size, helpSort);

    cout << "sorted" << "\n";
    cout << "| " << "i" << " | " << "s" << " | " << "f" << " |\n";

    for (int i = 0; i < size; i++) {
        cout << "| " << tasks[i].id << " | " << tasks[i].start << " | " << tasks[i].finish << " |\n";
    }

    Task current = tasks[0];

    cout << "greedy selection" << "\n";

    cout << current.id << " ";

    for (int i = 1; i < size; i++) {
        if (tasks[i].start >= current.finish) {
            cout << tasks[i].id << " ";
            current = tasks[i];
        }
    }

    return 0;
}
