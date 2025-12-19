#include <iostream>

void reverse(int n){
    if (n > 0) {
        std::cout << n % 10;
        reverse(n / 10);
    }
}

int main() {
    int n;
    std::cin >> n;


    reverse(n);
    return 0;
}