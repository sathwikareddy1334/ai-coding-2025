#!/usr/bin/env python3
"""
Quick demonstration of Armstrong Number Checker functionality.
This script shows the key features without requiring user interaction.
"""

from armstrong_number import is_armstrong_number, get_armstrong_calculation_details

def quick_demo():
    """Quick demonstration of the Armstrong number checker."""
    
    print("🔢 ARMSTRONG NUMBER CHECKER - QUICK DEMO")
    print("=" * 45)
    
    # Demo 1: Famous Armstrong numbers with explanations
    print("\n📚 WHAT IS AN ARMSTRONG NUMBER?")
    print("An Armstrong number equals the sum of its digits raised to the power of digit count.")
    
    print("\n✨ FAMOUS EXAMPLES:")
    
    examples = [
        (153, "Classic 3-digit example"),
        (9474, "4-digit Armstrong number"),
        (1634, "Another 4-digit example"),
        (123, "Counter-example (NOT Armstrong)")
    ]
    
    for number, description in examples:
        print(f"\n🔍 Checking {number} ({description}):")
        
        # Get detailed analysis
        details = get_armstrong_calculation_details(number)
        
        print(f"   Digits: {details['digits']}")
        print(f"   Formula: {details['calculation']}")
        print(f"   Calculation: {details['detailed_calculation']}")
        print(f"   Sum: {details['sum']}")
        
        if details['is_armstrong']:
            print(f"   ✅ Result: {number} IS an Armstrong number!")
        else:
            print(f"   ❌ Result: {number} is NOT an Armstrong number.")
    
    print(f"\n🎯 ALGORITHM STEPS:")
    print("1. Extract individual digits from the number")
    print("2. Count how many digits there are (n)")
    print("3. Raise each digit to the power of n")
    print("4. Sum all the powered digits")
    print("5. Compare sum with original number")
    
    print(f"\n📊 QUICK TESTS:")
    test_numbers = [0, 1, 5, 10, 153, 371, 407, 1634, 8208, 9474, 100, 999, 1000]
    
    armstrong_count = 0
    for num in test_numbers:
        is_armstrong = is_armstrong_number(num)
        status = "✅" if is_armstrong else "❌"
        print(f"   {num:4d}: {status}")
        if is_armstrong:
            armstrong_count += 1
    
    print(f"\n📈 SUMMARY:")
    print(f"   Tested {len(test_numbers)} numbers")
    print(f"   Found {armstrong_count} Armstrong numbers")
    print(f"   Success rate: {armstrong_count/len(test_numbers)*100:.1f}%")
    
    print(f"\n🚀 READY TO USE!")
    print("   Import: from armstrong_number import is_armstrong_number")
    print("   Usage:  is_armstrong_number(153)  # Returns True")
    
    print("\n" + "=" * 45)

if __name__ == "__main__":
    quick_demo()