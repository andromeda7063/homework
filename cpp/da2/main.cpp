#include <iostream>
#include <string>
using namespace std;

class salesperson; // forward declaration

class salesorder {
public:
    int ordno;
    string itemname;
    string delDate;
    string address;

    salesorder() {} // default constructor

    salesorder(int ordno, string itemname, string delDate, string address) {
        this->ordno = ordno;
        this->itemname = itemname;
        this->delDate = delDate;
        this->address = address;
    }

    void displayOrder() {
        cout << "Order Number: " << ordno << "\nItem Name: " << itemname
             << "\nDelivery Date: " << delDate << "\nAddress: " << address << "\n";
    }

    friend void checkOrderMatch(salesorder orders[], int orderCount, salesperson &sp);
};

class salesperson {
public:
    string name;
    int ordersHandled[3]; // can handle only 3 orders

    salesperson() {} // default constructor

    salesperson(string name, int o1, int o2, int o3) {
        this->name = name;
        ordersHandled[0] = o1;
        ordersHandled[1] = o2;
        ordersHandled[2] = o3;
    }

    friend void checkOrderMatch(salesorder orders[], int orderCount, salesperson &sp);
};

// friend function to check if an order number is handled by the salesperson
void checkOrderMatch(salesorder orders[], int orderCount, salesperson &sp) {
    for (int i = 0; i < orderCount; i++) {
        for (int j = 0; j < 3; j++) {
            if (orders[i].ordno == sp.ordersHandled[j]) {
                cout << "Order found! Salesperson: " << sp.name << endl;
                return;
            }
        }
    }
    cout << "The order is not found." << endl;
}

// function to search and display order details by itemname
void searchByItem(salesorder orders[], int orderCount, string searchItem) {
    bool found = false;
    for (int i = 0; i < orderCount; i++) {
        if (orders[i].itemname == searchItem) {
            cout << "Order Details:\n";
            orders[i].displayOrder();
            found = true;
        }
    }
    if (!found) {
        cout << "Item not found." << endl;
    }
}

int main() {
    int M; // number of sales orders
    cout << "Enter number of sales orders: ";
    cin >> M;

    salesorder orders[M]; // array to store sales orders

    // taking input for M sales orders
    for (int i = 0; i < M; i++) {
        int ordno;
        string itemname, delDate, address;

        cout << "\nEnter details for order " << i + 1 << ":\n";
        cout << "Order Number: ";
        cin >> ordno;
        cout << "Item Name: ";
        cin >> itemname;
        cout << "Delivery Date: ";
        cin >> delDate;
        cout << "Address: ";
        cin >> address;

        orders[i] = salesorder(ordno, itemname, delDate, address);
    }

    // taking input for salesperson
    string sp_name;
    int o1, o2, o3;
    cout << "\nEnter salesperson details:\n";
    cout << "Name: ";
    cin.ignore();
    getline(cin, sp_name);
    cout << "Enter 3 order numbers handled by salesperson: ";
    cin >> o1 >> o2 >> o3;

    salesperson sp(sp_name, o1, o2, o3);

    // checking if a specific order is handled by the salesperson
    int searchOrdNo;
    cout << "\nEnter an order number to check if handled by salesperson: ";
    cin >> searchOrdNo;
    checkOrderMatch(orders, M, sp);

    // searching for order details by itemname
    string searchItem;
    cout << "\nEnter an item name to search for order details: ";
    cin.ignore();
    getline(cin, searchItem);
    searchByItem(orders, M, searchItem);

    return 0;
}