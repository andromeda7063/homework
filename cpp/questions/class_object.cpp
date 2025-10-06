// imports
#include <iostream>
#include <string>
#include <iomanip>      // useless import?
using namespace std;

// define a vocaloid class with name and id parameters
class vocaloid {
    private:        // private variables cant be accessed outside the class
        string name;
        int ID;

    public:
        vocaloid(string name, int ID) {
            this->name = name;      // this pointer references the variable name locally within the class object
            this->ID = ID;
        }

        void printDetails() {
            cout << "Name: " << name << endl;
            cout << "ID: ";
            cout << setprecision(2) << ID << endl;      // refer comment in main()
        }

        ~vocaloid() {
            cout << "Vocaloid object " << name << " destroyed" << endl;
        }

};

int main() {
    vocaloid miku("Hatsune Miku", 01);      // how tf to print 01 instead of 1 idk
    
    miku.printDetails();

//    cout << miku.name;      // will return an error as 'name' is a private variable of the 'miku' object
    return 0;

}