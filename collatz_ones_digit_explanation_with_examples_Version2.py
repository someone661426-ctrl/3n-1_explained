"""
Collatz Conjecture (3n+1) - One's Digit Reasoning with Examples

This script formalizes the reasoning that:
  - For any positive integer, the one's digit (last digit) can be used as the whole number
    to determine the Collatz (3n+1) operation, since it tells if the number is odd or even.
  - For even numbers (one's digit 0,2,4,6,8): next = n // 2
  - For odd numbers (one's digit 1,3,5,7,9): next = 3 * n + 1
  - Regardless of starting value, the sequence always reaches the cycle 4 → 2 → 1.
  - Special case: 0 is also considered to "go 4→2→1" for this reasoning.

At each step, the script prints a clear example of the one's digit and which operation is performed.
"""

def collatz_using_ones_digit(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        print("Starting with: 0")
        print("By this reasoning, 0 is taken to immediately go to the 4 → 2 → 1 cycle.")
        print("Example: 0's one's digit is 0 (even) → goes directly to cycle: 4 → 2 → 1 → ...")
        print("Sequence: 0 → 4 → 2 → 1 → (cycle repeats)")
        return
    print(f"Starting with: {n}")
    while n != 1:
        ones_digit = n % 10
        parity = "even" if ones_digit % 2 == 0 else "odd"
        print(f"Current number: {n} (one's digit: {ones_digit} → {parity})")
        # Example for clarification when n is not the same as its one's digit
        if n >= 10:
            print(f"  Example: {n}'s one's digit is {ones_digit} (e.g., for 14, one's digit is 4)")
        if ones_digit % 2 == 0:
            print(f"  One's digit is even → divide by 2: {n} // 2 = {n//2}")
            n = n // 2
        else:
            print(f"  One's digit is odd  → multiply by 3 and add 1: 3 * {n} + 1 = {3*n+1}")
            n = 3 * n + 1
    print("Current number: 1")
    print("Sequence has reached the start of the 4 → 2 → 1 cycle, which repeats forever.")

# Example usage:
if __name__ == "__main__":
    collatz_using_ones_digit(14)  # Demonstrates with 14 (one's digit 4)
    print()
    collatz_using_ones_digit(15)  # Demonstrates with 15 (one's digit 5)
    print()
    collatz_using_ones_digit(0)   # Special case for 0