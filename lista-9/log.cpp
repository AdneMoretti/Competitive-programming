#include <iostream>
#include <cmath>

int main() {
    int T;
    std::cin >> T; // Read the number of test cases

    while (T--) {
        int n, k;
        std::cin >> n >> k; // Read n and k

        // Calculate the first three digits using logarithmic operations
        double log_val = k * log10(n);
        int first_three_digits = pow(10, log_val - floor(log_val) + 2);

        // Calculate the last three digits using modular arithmetic
        int last_three_digits = 1;
        for (int i = 0; i < k; i++) {
            last_three_digits = (last_three_digits * (n % 1000)) % 1000;
        }

        // Output the result
        std::cout << first_three_digits << "..." << last_three_digits << "\n";
    }

    return 0;
}
