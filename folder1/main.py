from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from folder2.calculator import sum_numbers, multiply_numbers


# Test the functions
def main():
    # Test sum_numbers
    print("Sum test: 1 + 2 + 3 + 4 =", sum_numbers(1, 2, 3, 4))

    # Test multiply_numbers
    print("Multiplication test: 2 * 3 * 4 =", multiply_numbers(2, 3, 4))


if __name__ == "__main__":
    main()
