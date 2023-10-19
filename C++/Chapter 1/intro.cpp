#include <iostream>

int main(){

    int x, y;

    std::cout << "Enter 1st Number: ";
    std::cin >> x;
    std::cout << "Enter 2nd Number: ";
    std::cin >> y;

    std::cout << "The sum of x and y is: " << (x + y) << '\n';
    std::cout << "The subtraction of x and y is: " << (x - y) << '\n';

    return 0;
}
