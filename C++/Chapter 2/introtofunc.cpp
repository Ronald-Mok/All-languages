#include <iostream>

void doA(){
    std::cout << "Start doA.\n";
    std::cout << "In doA.\n";
    std::cout << "End of doA.\n";
}

void doB(){
    std::cout << "Start doB.\n";
    std::cout << "In doB.\n";
    doA();
    std::cout << "End of doB.\n";
}

int main(){
    std::cout << "Start of main.\n";
    doB();
    std::cout << "End of main.\n";
    
    return 0; 
}
