// imports
#include <iostream>
#include <string>
using namespace std;

class Musician {
    protected:
        string name;
        string instrument;
        int paycheck;

    public:
        Musician(string name, string instrument, int paycheck) {
            this->name = name;
            this->instrument = instrument;
            this->paycheck = paycheck;
        }
};

class Bassist : protected Musician {
    protected:
        string bassGuitarName;

    public:
        Bassist(string name, string bassGuitarName) : Musician{name, "Bass", 0}, bassGuitarName{bassGuitarName} {
            cout << "Bassist object created" << endl;
        }

        void displayBassist() {

            cout << "Name: " << name << endl;
            cout << "Instrument: " << instrument << endl;
            cout << "Paycheck: " << paycheck << endl;
            cout << "Bass Guitar name: " << bassGuitarName << endl;

        }

};

int main() {
    Bassist Ryo("Ryo", "Fender P-Bass");

    Ryo.displayBassist();
}