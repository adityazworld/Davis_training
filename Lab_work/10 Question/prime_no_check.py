## Question 9) Prime Number Checker

    """Returns True if n is a prime number, False otherwise."""

    # Numbers less than 2 are not prime
    if n < 2:
        return False

    # Check divisibility from 2 up to √n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False   # Divisible → not prime

    return True            # No divisor found → prime


def display_result(n):
    """Displays whether a number is prime or not using if-else."""
    if is_prime(n):
        print(f"  {n:>4}  →  ✅ Prime")
    else:
        print(f"  {n:>4}  →  ❌ Not Prime")


# ── Process a list of numbers
numbers = [1, 2, 3, 4, 5, 16, 17, 19, 20, 23, 25, 29, 33, 37, 49, 97]

print("=" * 28)
print("     PRIME NUMBER CHECKER")
print("=" * 28)

for num in numbers:
    display_result(num)

print("=" * 28)

# ── Bonus: Print all primes up to 50
primes_upto_50 = [n for n in range(2, 51) if is_prime(n)]
print(f"\n📋 All primes up to 50:\n   {primes_upto_50}")