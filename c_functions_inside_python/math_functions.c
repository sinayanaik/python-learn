#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int square(int a) {
    return a * a;
}

int factorial(int a) {
    int result = 1;
    for (int i = 1; i <= a; i++) {
        result *= i;
    }
    return result;
}
