#include <iostream>

int getNum(int x=0){
    
    std::cout << "Enter a number: ";
    std::cin >> x;
    
    return x;
}

void calculate(int x, int y){
    
    std::cout << "The sum is: " << x + y << '\n';

}


int main(){
    calculate(getNum(), getNum());

    return 0;
}
