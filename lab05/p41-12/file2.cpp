#include "headf.h"
#include <iostream>

double solve_q1() {
    double a = find_factorial(5);
    double b = find_factorial(7);
    double c = find_factorial(8);

    // std::cout << a << " " << b << " " << c;
    return (a + b) / c;
}