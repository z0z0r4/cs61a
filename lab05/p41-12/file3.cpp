#include "headf.h"

int solve_q2() {
    int result = 0;
    for (int i=1; i <= 10; i++) {
        result += find_factorial(i);
    }

    return result;
}