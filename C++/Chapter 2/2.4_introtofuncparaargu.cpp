#include <iostream>

int getNum(int x=2){

    return x;
}

void calculate(int x, int y){

    std::cout << "The sum is: " << x + y << '\n';

}


int main(){
    calculate(getNum(), getNum(7));

    return 0;
}
