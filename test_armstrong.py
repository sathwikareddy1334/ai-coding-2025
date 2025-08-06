from armstrong_number import (
    is_armstrong_number, 
    get_armstrong_calculation_details, 
    find_armstrong_numbers_in_range
)

def test_armstrong_function():
    """
    Comprehensive test of the Armstrong number functions.
    """
    print("=== Testing Armstrong Number Functions ===\n")
    
    # Test 1: Known Armstrong numbers
    print("Test 1: Known Armstrong Numbers")
    print("-" * 30)
    armstrong_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 371, 407, 1634, 8208, 9474]
    
    for num in armstrong_numbers:
        result = is_armstrong_number(num)
        print(f"{num:4d}: {'✅ PASS' if result else '❌ FAIL'}")
    
    # Test 2: Known non-Armstrong numbers
    print("\nTest 2: Known Non-Armstrong Numbers")
    print("-" * 30)
    non_armstrong = [10, 11, 100, 123, 456, 999, 1000, 1500]
    
    for num in non_armstrong:
        result = is_armstrong_number(num)
        print(f"{num:4d}: {'❌ FAIL (should be False)' if result else '✅ PASS'}")
    
    # Test 3: Error handling
    print("\nTest 3: Error Handling")
    print("-" * 30)
    
    # Test negative number
    try:
        is_armstrong_number(-5)
        print("Negative number test: ❌ FAIL (should raise ValueError)")
    except ValueError:
        print("Negative number test: ✅ PASS")
    
    # Test non-integer input
    try:
        is_armstrong_number(153.5)
        print("Float input test: ❌ FAIL (should raise TypeError)")
    except TypeError:
        print("Float input test: ✅ PASS")
    
    try:
        is_armstrong_number("153")
        print("String input test: ❌ FAIL (should raise TypeError)")
    except TypeError:
        print("String input test: ✅ PASS")
    
    # Test 4: Detailed calculation function
    print("\nTest 4: Detailed Calculation Analysis")
    print("-" * 30)
    
    test_cases = [153, 371, 1634, 123]
    for num in test_cases:
        details = get_armstrong_calculation_details(num)
        print(f"\nNumber: {num}")
        print(f"Digits: {details['digits']}")
        print(f"Calculation: {details['detailed_calculation']}")
        print(f"Sum: {details['sum']}")
        print(f"Is Armstrong: {details['is_armstrong']}")
    
    # Test 5: Range finder function
    print("\nTest 5: Finding Armstrong Numbers in Range")
    print("-" * 30)
    
    ranges_to_test = [(0, 10), (1, 200), (1, 1000)]
    
    for start, end in ranges_to_test:
        armstrong_list = find_armstrong_numbers_in_range(start, end)
        print(f"Range {start}-{end}: {armstrong_list}")
    
    print("\n=== All Tests Completed ===")


def demonstrate_step_by_step_calculation():
    """
    Demonstrate step-by-step calculation for educational purposes.
    """
    print("\n=== Step-by-Step Armstrong Number Calculation ===\n")
    
    examples = [153, 9474, 1634, 123]
    
    for number in examples:
        print(f"Example: Checking if {number} is an Armstrong number")
        print("-" * 50)
        
        # Step 1: Break down into digits
        digits = [int(d) for d in str(number)]
        num_digits = len(digits)
        print(f"Step 1: Break {number} into digits: {digits}")
        print(f"Step 2: Count digits: {num_digits}")
        
        # Step 3: Calculate each term
        print(f"Step 3: Calculate each digit raised to power {num_digits}:")
        terms = []
        for digit in digits:
            term = digit ** num_digits
            terms.append(term)
            print(f"        {digit}^{num_digits} = {term}")
        
        # Step 4: Sum all terms
        total_sum = sum(terms)
        print(f"Step 4: Sum all terms: {' + '.join(map(str, terms))} = {total_sum}")
        
        # Step 5: Compare with original
        print(f"Step 5: Compare {total_sum} with original {number}")
        
        if total_sum == number:
            print(f"Result: ✅ {number} IS an Armstrong number!")
        else:
            print(f"Result: ❌ {number} is NOT an Armstrong number.")
        
        print()


if __name__ == "__main__":
    test_armstrong_function()
    demonstrate_step_by_step_calculation()