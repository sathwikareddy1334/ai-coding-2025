def is_armstrong_number(number):
    """
    Check whether a given number is an Armstrong number.
    
    An Armstrong number (also known as a narcissistic number) is a number that is 
    equal to the sum of its own digits each raised to the power of the number of digits.
    
    For example:
    - 153 is an Armstrong number: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
    - 9474 is an Armstrong number: 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474
    
    Args:
        number (int): The number to check (must be a positive integer)
    
    Returns:
        bool: True if the number is an Armstrong number, False otherwise
    
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    
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
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for single-digit numbers (0-9 are all Armstrong numbers)
    if number < 10:
        return True
    
    # Convert number to string to easily access individual digits
    number_str = str(number)
    num_digits = len(number_str)
    
    # Calculate the sum of each digit raised to the power of number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in number_str)
    
    # Check if the sum equals the original number
    return armstrong_sum == number


def get_armstrong_calculation_details(number):
    """
    Get detailed calculation steps for checking if a number is an Armstrong number.
    
    Args:
        number (int): The number to analyze
    
    Returns:
        dict: Dictionary containing calculation details including:
            - 'is_armstrong': Boolean result
            - 'digits': List of individual digits
            - 'num_digits': Number of digits
            - 'calculation': String showing the calculation
            - 'sum': The calculated sum
            - 'original': The original number
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    number_str = str(number)
    digits = [int(d) for d in number_str]
    num_digits = len(digits)
    
    # Calculate each term and the total sum
    terms = [digit ** num_digits for digit in digits]
    armstrong_sum = sum(terms)
    
    # Create calculation string
    calculation_parts = [f"{digit}^{num_digits}" for digit in digits]
    calculation = " + ".join(calculation_parts)
    
    # Create detailed calculation with actual values
    detailed_calculation_parts = [f"{digit}^{num_digits} = {digit**num_digits}" 
                                for digit in digits]
    detailed_calculation = " + ".join(detailed_calculation_parts)
    
    return {
        'is_armstrong': armstrong_sum == number,
        'digits': digits,
        'num_digits': num_digits,
        'calculation': calculation,
        'detailed_calculation': detailed_calculation,
        'sum': armstrong_sum,
        'original': number,
        'terms': terms
    }


def find_armstrong_numbers_in_range(start, end):
    """
    Find all Armstrong numbers within a given range.
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
    
    Returns:
        list: List of Armstrong numbers in the range
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")
    
    if start < 0 or end < 0:
        raise ValueError("Range values must be non-negative")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    
    return armstrong_numbers


def interactive_armstrong_checker():
    """
    Interactive function to check Armstrong numbers with user input.
    """
    print("=== Armstrong Number Checker ===")
    print("\nWhat is an Armstrong Number?")
    print("An Armstrong number is equal to the sum of its digits")
    print("each raised to the power of the number of digits.")
    print("\nExamples:")
    print("- 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153")
    print("- 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474")
    print()
    
    while True:
        try:
            user_input = input("Enter a non-negative integer to check (or 'quit' to exit): ").strip()
            
            if user_input.lower() in ['quit', 'q', 'exit']:
                print("Goodbye!")
                break
            
            number = int(user_input)
            
            if number < 0:
                print("Please enter a non-negative integer.")
                continue
            
            # Get detailed calculation
            details = get_armstrong_calculation_details(number)
            
            print(f"\n--- Analysis for {number} ---")
            print(f"Number of digits: {details['num_digits']}")
            print(f"Digits: {details['digits']}")
            print(f"Calculation: {details['calculation']}")
            print(f"Detailed: {details['detailed_calculation']}")
            print(f"Sum: {details['sum']}")
            
            if details['is_armstrong']:
                print(f"✅ {number} IS an Armstrong number!")
            else:
                print(f"❌ {number} is NOT an Armstrong number.")
            print()
            
        except ValueError:
            print("Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


def main():
    """
    Main function demonstrating Armstrong number checking.
    """
    print("Armstrong Number Examples and Testing")
    print("=" * 40)
    
    # Test some known Armstrong numbers
    test_numbers = [0, 1, 153, 371, 407, 1634, 8208, 9474, 123, 456, 999]
    
    print("\nTesting known numbers:")
    for num in test_numbers:
        result = is_armstrong_number(num)
        status = "✅ Armstrong" if result else "❌ Not Armstrong"
        print(f"{num:4d}: {status}")
    
    print("\nDetailed analysis of 153:")
    details = get_armstrong_calculation_details(153)
    print(f"Calculation: {details['detailed_calculation']} = {details['sum']}")
    
    print("\nDetailed analysis of 9474:")
    details = get_armstrong_calculation_details(9474)
    print(f"Calculation: {details['detailed_calculation']} = {details['sum']}")
    
    print("\nFinding Armstrong numbers from 1 to 1000:")
    armstrong_in_range = find_armstrong_numbers_in_range(1, 1000)
    print(f"Found {len(armstrong_in_range)} Armstrong numbers: {armstrong_in_range}")
    
    print("\n" + "=" * 40)
    print("Run interactive_armstrong_checker() for hands-on testing!")


if __name__ == "__main__":
    main()