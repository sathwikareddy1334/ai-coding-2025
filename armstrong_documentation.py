"""
ARMSTRONG NUMBER CHECKER - COMPLETE DOCUMENTATION
================================================

This module provides comprehensive functionality for checking Armstrong numbers,
also known as narcissistic numbers or pluperfect digital invariants.

WHAT IS AN ARMSTRONG NUMBER?
---------------------------
An Armstrong number is a number that equals the sum of its own digits each 
raised to the power of the number of digits.

Mathematical Definition:
For a number with n digits: d₁d₂d₃...dₙ
The number is Armstrong if: d₁ⁿ + d₂ⁿ + d₃ⁿ + ... + dₙⁿ = original number

EXAMPLES:
--------
1-digit numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
   - All single digits are Armstrong numbers (e.g., 5¹ = 5)

3-digit examples:
   - 153: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✅
   - 371: 3³ + 7³ + 1³ = 27 + 343 + 1 = 371 ✅
   - 407: 4³ + 0³ + 7³ = 64 + 0 + 343 = 407 ✅

4-digit examples:
   - 1634: 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1 + 1296 + 81 + 256 = 1634 ✅
   - 8208: 8⁴ + 2⁴ + 0⁴ + 8⁴ = 4096 + 16 + 0 + 4096 = 8208 ✅
   - 9474: 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474 ✅

Counter-examples:
   - 123: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123 ❌
   - 456: 4³ + 5³ + 6³ = 64 + 125 + 216 = 405 ≠ 456 ❌

ALGORITHM STEPS:
---------------
1. Input Validation:
   - Check if input is an integer
   - Check if input is non-negative
   
2. Extract Digits:
   - Convert number to string to access individual digits
   - Count the number of digits (n)
   
3. Calculate Power Sum:
   - For each digit d, calculate d^n
   - Sum all the powered digits
   
4. Compare:
   - If sum equals original number → Armstrong number
   - If sum ≠ original number → Not Armstrong number

FUNCTIONS PROVIDED:
------------------

1. is_armstrong_number(number)
   - Primary function to check if a number is Armstrong
   - Returns: Boolean (True/False)
   - Raises: TypeError for non-integers, ValueError for negative numbers

2. get_armstrong_calculation_details(number)
   - Returns detailed calculation breakdown
   - Useful for educational purposes and debugging
   - Returns: Dictionary with calculation steps

3. find_armstrong_numbers_in_range(start, end)
   - Finds all Armstrong numbers in a given range
   - Returns: List of Armstrong numbers

4. interactive_armstrong_checker()
   - Interactive command-line interface
   - Allows users to test multiple numbers with detailed output

USAGE EXAMPLES:
--------------
"""

from armstrong_number import (
    is_armstrong_number, 
    get_armstrong_calculation_details, 
    find_armstrong_numbers_in_range,
    interactive_armstrong_checker
)

def show_basic_usage():
    """Demonstrate basic usage of the Armstrong number checker."""
    print("=== BASIC USAGE EXAMPLES ===\n")
    
    # Example 1: Simple check
    print("1. Simple Armstrong number check:")
    numbers_to_check = [153, 123, 371, 456, 9474]
    
    for num in numbers_to_check:
        is_armstrong = is_armstrong_number(num)
        status = "IS" if is_armstrong else "is NOT"
        print(f"   {num} {status} an Armstrong number")
    
    print()

def show_detailed_analysis():
    """Show detailed step-by-step analysis."""
    print("=== DETAILED ANALYSIS EXAMPLES ===\n")
    
    examples = [153, 1634, 123]
    
    for num in examples:
        print(f"Analyzing {num}:")
        details = get_armstrong_calculation_details(num)
        
        print(f"  • Digits: {details['digits']}")
        print(f"  • Number of digits: {details['num_digits']}")
        print(f"  • Calculation: {details['calculation']}")
        print(f"  • Detailed: {details['detailed_calculation']}")
        print(f"  • Sum: {details['sum']}")
        print(f"  • Original: {details['original']}")
        print(f"  • Result: {'✅ Armstrong' if details['is_armstrong'] else '❌ Not Armstrong'}")
        print()

def show_range_finding():
    """Demonstrate finding Armstrong numbers in ranges."""
    print("=== FINDING ARMSTRONG NUMBERS IN RANGES ===\n")
    
    ranges = [(0, 20), (100, 500), (1000, 2000)]
    
    for start, end in ranges:
        armstrong_list = find_armstrong_numbers_in_range(start, end)
        print(f"Armstrong numbers from {start} to {end}:")
        print(f"  Found {len(armstrong_list)} numbers: {armstrong_list}")
        print()

def show_error_handling():
    """Demonstrate error handling."""
    print("=== ERROR HANDLING EXAMPLES ===\n")
    
    test_cases = [
        (-5, "negative number"),
        (3.14, "float number"),
        ("153", "string input"),
        (None, "None input")
    ]
    
    for test_input, description in test_cases:
        try:
            result = is_armstrong_number(test_input)
            print(f"  {description}: Unexpected success - {result}")
        except (TypeError, ValueError) as e:
            print(f"  {description}: Correctly caught error - {type(e).__name__}: {e}")
        except Exception as e:
            print(f"  {description}: Unexpected error - {type(e).__name__}: {e}")
    
    print()

def show_performance_considerations():
    """Show performance characteristics."""
    print("=== PERFORMANCE CONSIDERATIONS ===\n")
    
    import time
    
    # Test performance with different sized numbers
    test_numbers = [153, 1634, 54748, 1741725, 4210818]
    
    print("Performance test (time in seconds):")
    for num in test_numbers:
        start_time = time.time()
        
        # Run the check multiple times for better measurement
        for _ in range(1000):
            is_armstrong_number(num)
        
        end_time = time.time()
        avg_time = (end_time - start_time) / 1000
        
        print(f"  {num} ({len(str(num))} digits): {avg_time:.6f}s per check")
    
    print()

def complete_demonstration():
    """Run a complete demonstration of all features."""
    print("ARMSTRONG NUMBER CHECKER - COMPLETE DEMONSTRATION")
    print("=" * 55)
    print()
    
    show_basic_usage()
    show_detailed_analysis()
    show_range_finding()
    show_error_handling()
    show_performance_considerations()
    
    print("=== INTERACTIVE MODE AVAILABLE ===")
    print("To use the interactive checker, run:")
    print("  from armstrong_number import interactive_armstrong_checker")
    print("  interactive_armstrong_checker()")
    print()
    
    print("=== KNOWN ARMSTRONG NUMBERS (up to 7 digits) ===")
    known_armstrong = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 371, 407, 
                      1634, 8208, 9474, 54748, 92727, 93084, 548834, 
                      1741725, 4210818, 9800817, 9926315]
    
    print("Single digit:", [n for n in known_armstrong if n < 10])
    print("3-digit:", [n for n in known_armstrong if 100 <= n <= 999])
    print("4-digit:", [n for n in known_armstrong if 1000 <= n <= 9999])
    print("5-digit:", [n for n in known_armstrong if 10000 <= n <= 99999])
    print("6-digit:", [n for n in known_armstrong if 100000 <= n <= 999999])
    print("7-digit:", [n for n in known_armstrong if 1000000 <= n <= 9999999])

if __name__ == "__main__":
    complete_demonstration()