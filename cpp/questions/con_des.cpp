// imports
#include <iostream>
#include <string>
#include <iomanip>      // useless import?
using namespace std;

// constructor-destructor
// static int keeps a count of the number of myClass objects

class myClass {
    static int count;

    public:
        myClass() {
            count++;
        }

        void displayCount() {
            cout << "object count: " << count << endl;
        }

        ~myClass() {
            count--;
            cout << "myClass object destroyed. Remaining: " << count << endl;
        }
};


// parametrized constructor-destructor
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

// constructor overloading + destructor
// constructor can be defined differently based on tyoe and number of parameters

class music {
    private:
        string randArr[3] = {"september", "moonlight", "rabbit hole"};
        string vocaloidArr[3] = {"getcha", "aishite aishite aishite", "gimmexgimme"};

    public:
        music() {
            for (int i = 0; i < 3; i++) {
                cout << randArr[i] << " ";
            }

            cout << endl;
        }

        music(int n) {          // this constructor is only called when the object is created along with an argument
            for (int i = 0; i < 3; i++) {
                cout << vocaloidArr[i] << " ";
            }

            cout << endl;
        }

        ~music() {
            cout << "Music object destroyed" << endl;
        }
 };

int myClass::count = 0;     // initialze the static count int. :: is thhe scope resolution operator


int main() {
    myClass objArr[5];      // create an array of objects

    objArr[3].displayCount();       
    objArr[4].displayCount();       // same value


    vocaloid miku("Hatsune Miku", 01);      // how tf to print 01 instead of 1 idk
    
    miku.printDetails();

//    cout << miku.name;      // will return an error as 'name' is a private variable of the 'miku' object

    music m1;           // no args
    music m2(1);       // int argument 
    return 0;

}