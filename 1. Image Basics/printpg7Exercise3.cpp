// This program writes data to a file.
#include <iostream>
#include <fstream>
using namespace std;
 
int main()
{
    for (int g = 0; g < 5; g++){
        for (int i = 0; i < 50; i++){
            cout << "0 0 255 0 0 255 0 0 255 0 0 255 0 0 255\n";
            cout << "0 0 255 0 0 255 0 0 255 0 0 255 0 0 255\n";
            cout << "255 0 0 255 0 0 255 0 0 255 0 0 255 0 0\n";
            cout << "255 0 0 255 0 0 255 0 0 255 0 0 255 0 0\n";
        }

        for (int i = 0; i < 50; i++){
            cout << "255 0 0 255 0 0 255 0 0 255 0 0 255 0 0\n";
            cout << "255 0 0 255 0 0 255 0 0 255 0 0 255 0 0\n";
            cout << "0 0 255 0 0 255 0 0 255 0 0 255 0 0 255\n";
            cout << "0 0 255 0 0 255 0 0 255 0 0 255 0 0 255\n";
        }
    }
 
    // Close the file
    cout << "Done.\n";
    return 0;
}