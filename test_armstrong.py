#!/usr/bin/env python3
"""
Simple test script to demonstrate individual Armstrong number checks
"""

from armstrong_checker import is_armstrong_number, is_armstrong_number_verbose

def main():
    print("=== Simple Armstrong Number Tests ===\n")
    
    # Test individual numbers with basic function
    test_numbers = [153, 123, 9474, 371, 1634, 456]
    
    print("1. Basic Function Tests:")
    print("-" * 30)
    for num in test_numbers:
        result = is_armstrong_number(num)
        print(f"is_armstrong_number({num}) = {result}")
    
    print("\n" + "="*50 + "\n")
    
    # Demonstrate verbose output for one example
    print("2. Verbose Output Example:")
    print("-" * 30)
    print("Let's check 153 step by step:")
    is_armstrong_number_verbose(153)
    
    print("\n" + "="*50 + "\n")
    
    # Show error handling
    print("3. Error Handling Examples:")
    print("-" * 30)
    
    error_tests = [
        ("String input", "153"),
        ("Negative number", -5),
        ("Float input", 3.14)
    ]
    
    for description, test_input in error_tests:
        print(f"\nTesting {description}: {test_input}")
        try:
            result = is_armstrong_number(test_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()