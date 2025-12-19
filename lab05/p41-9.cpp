#include <iostream>

bool is_sum_eq_15(int n) {
    int sum = 0;

    while (n != 0) {
        sum += n % 10;
        n /= 10;
    }

    return sum == 15;
}

int main() {
    int count = 0;
    for (int i = 100; i <= 999; i++) {
        if (is_sum_eq_15(i)) {
        count += 1;
        std::cout << i << " ";}
    }
    return 0;
}