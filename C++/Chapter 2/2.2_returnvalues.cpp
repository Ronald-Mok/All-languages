#include <iostream>

int getIntFromUser(){                            // Function to get int from user
    std::cout << "Enter a Number: ";             // Recieves user input
    int input;                                   // Define a var for user input
    std::cin >> input;                           // Stores user input in input variable 
    
    return input;                                // Returns user input
}

int main(){

    int a{getIntFromUser()};                     // Gets input for a and b
    int b{getIntFromUser()};

    // Prints out sum of a and b
    std::cout << "The total sum of int a and b are: " << a + b << '\n';     

    return 0;

}
