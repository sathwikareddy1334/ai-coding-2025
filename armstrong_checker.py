"""
Armstrong Number Checker
========================

An Armstrong number (also known as a narcissistic number) is a number that is 
equal to the sum of its own digits each raised to the power of the number of digits.

Mathematical Definition:
For a number with n digits: d₁d₂d₃...dₙ
The number is Armstrong if: d₁ⁿ + d₂ⁿ + d₃ⁿ + ... + dₙⁿ = original number

Examples:
- 153 is Armstrong: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
- 9474 is Armstrong: 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474
- 123 is NOT Armstrong: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123
"""

def is_armstrong_number(number):
    """
    Check if a given number is an Armstrong number.
    
    Args:
        number (int): The number to check (must be non-negative)
        
    Returns:
        bool: True if the number is an Armstrong number, False otherwise
        
    Raises:
        ValueError: If the input is negative
        TypeError: If the input is not an integer
        
    Examples:
        >>> is_armstrong_number(153)
        True
        >>> is_armstrong_number(123)
        False
        >>> is_armstrong_number(9474)
        True
    """
    # Input validation
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number < 0:
        raise ValueError("Input must be non-negative")
    
    # Convert number to string to easily access individual digits
    str_number = str(number)
    num_digits = len(str_number)
    
    # Calculate sum of each digit raised to the power of number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_number)
    
    # Check if the sum equals the original number
    return armstrong_sum == number


def is_armstrong_number_verbose(number):
    """
    Check if a given number is an Armstrong number with detailed step-by-step output.
    
    Args:
        number (int): The number to check (must be non-negative)
        
    Returns:
        bool: True if the number is an Armstrong number, False otherwise
    """
    print(f"\n--- Checking if {number} is an Armstrong number ---")
    
    # Input validation
    if not isinstance(number, int):
        print(f"Error: Input must be an integer, got {type(number).__name__}")
        return False
    if number < 0:
        print(f"Error: Input must be non-negative, got {number}")
        return False
    
    # Step 1: Get individual digits
    str_number = str(number)
    digits = [int(d) for d in str_number]
    num_digits = len(digits)
    
    print(f"Step 1: Extract digits from {number}")
    print(f"        Digits: {digits}")
    print(f"        Number of digits: {num_digits}")
    
    # Step 2: Calculate each digit raised to the power of number of digits
    print(f"\nStep 2: Calculate each digit raised to the power of {num_digits}")
    powers = []
    calculation_parts = []
    
    for digit in digits:
        power_result = digit ** num_digits
        powers.append(power_result)
        calculation_parts.append(f"{digit}^{num_digits} = {power_result}")
        print(f"        {digit}^{num_digits} = {power_result}")
    
    # Step 3: Sum all the powers
    armstrong_sum = sum(powers)
    calculation_str = " + ".join(calculation_parts)
    
    print(f"\nStep 3: Sum all the powers")
    print(f"        {calculation_str}")
    print(f"        = {armstrong_sum}")
    
    # Step 4: Compare with original number
    is_armstrong = armstrong_sum == number
    print(f"\nStep 4: Compare sum with original number")
    print(f"        {armstrong_sum} == {number}? {is_armstrong}")
    
    # Final result
    result_text = "IS" if is_armstrong else "IS NOT"
    print(f"\nResult: {number} {result_text} an Armstrong number!")
    
    return is_armstrong


def find_armstrong_numbers_in_range(start, end):
    """
    Find all Armstrong numbers within a given range.
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
        
    Returns:
        list: List of Armstrong numbers in the range
    """
    armstrong_numbers = []
    
    print(f"\nFinding Armstrong numbers between {start} and {end}:")
    print("-" * 50)
    
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
            print(f"{num} is an Armstrong number")
    
    if not armstrong_numbers:
        print("No Armstrong numbers found in this range.")
    
    return armstrong_numbers


# Example usage and demonstrations
if __name__ == "__main__":
    print("ARMSTRONG NUMBER CHECKER")
    print("=" * 50)
    
    # Test cases with detailed output
    test_numbers = [0, 1, 2, 3, 153, 371, 407, 1634, 8208, 9474, 123, 456]
    
    print("\n1. DETAILED STEP-BY-STEP CHECKS")
    print("=" * 40)
    
    for num in [153, 123, 9474]:
        is_armstrong_number_verbose(num)
        print("\n" + "="*60)
    
    print("\n2. QUICK CHECKS FOR MULTIPLE NUMBERS")
    print("=" * 40)
    
    for num in test_numbers:
        result = is_armstrong_number(num)
        status = "✓ Armstrong" if result else "✗ Not Armstrong"
        print(f"{num:4d}: {status}")
    
    print("\n3. FIND ARMSTRONG NUMBERS IN RANGES")
    print("=" * 40)
    
    # Find Armstrong numbers in different ranges
    ranges = [(0, 10), (100, 200), (1000, 2000), (8000, 10000)]
    
    for start, end in ranges:
        armstrong_list = find_armstrong_numbers_in_range(start, end)
        print(f"Armstrong numbers between {start}-{end}: {armstrong_list}")
        print()
    
    print("\n4. ERROR HANDLING EXAMPLES")
    print("=" * 40)
    
    # Test error handling
    error_cases = [
        (-5, "Negative number"),
        (3.14, "Float number"),
        ("153", "String input")
    ]
    
    for test_input, description in error_cases:
        print(f"\nTesting {description}: {test_input}")
        try:
            result = is_armstrong_number(test_input)
            print(f"Result: {result}")
        except (ValueError, TypeError) as e:
            print(f"Error caught: {e}")