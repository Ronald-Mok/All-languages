#include <iostream>

int getInput(){
    std::cout << "Enter Number: ";
    int input;
    std::cin >> input;

    return input;


}

void calculate(int x=getInput(), int y=getInput()){


    std::cout << x + y << '\n';
}

int main(){
    calculate();

    return 0;
}
