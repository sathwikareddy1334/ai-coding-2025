# Armstrong Number Checker - Complete Documentation

## Overview

This document provides comprehensive documentation for the Armstrong number checker implementation, including mathematical concepts, algorithm steps, prompts, and detailed outputs.

## What is an Armstrong Number?

An **Armstrong number** (also known as a **narcissistic number** or **pluperfect digital invariant**) is a number that equals the sum of its own digits each raised to the power of the number of digits.

### Mathematical Definition

For a number with `n` digits: `d₁d₂d₃...dₙ`

The number is Armstrong if: `d₁ⁿ + d₂ⁿ + d₃ⁿ + ... + dₙⁿ = original number`

### Examples

- **153** (3 digits): `1³ + 5³ + 3³ = 1 + 125 + 27 = 153` ✓
- **9474** (4 digits): `9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474` ✓
- **123** (3 digits): `1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123` ✗

## Algorithm Steps

### Step 1: Input Validation
- Check if input is an integer
- Verify input is non-negative
- Raise appropriate exceptions for invalid inputs

### Step 2: Extract Digits
- Convert number to string representation
- Count the number of digits (`n`)
- Extract individual digits as integers

### Step 3: Calculate Powers
- For each digit `d`, calculate `d^n`
- Store results for summation

### Step 4: Sum and Compare
- Sum all the power results
- Compare sum with original number
- Return True if equal, False otherwise

## Implementation Details

### Core Function: `is_armstrong_number(number)`

```python
def is_armstrong_number(number):
    # Input validation
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number < 0:
        raise ValueError("Input must be non-negative")
    
    # Convert to string to access digits
    str_number = str(number)
    num_digits = len(str_number)
    
    # Calculate Armstrong sum
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_number)
    
    # Return comparison result
    return armstrong_sum == number
```

### Verbose Function: `is_armstrong_number_verbose(number)`

This function provides step-by-step output for educational purposes, showing:
1. Digit extraction process
2. Individual power calculations
3. Sum computation
4. Final comparison

## Sample Outputs

### Example 1: 153 (Armstrong Number)

```
--- Checking if 153 is an Armstrong number ---
Step 1: Extract digits from 153
        Digits: [1, 5, 3]
        Number of digits: 3

Step 2: Calculate each digit raised to the power of 3
        1^3 = 1
        5^3 = 125
        3^3 = 27

Step 3: Sum all the powers
        1^3 = 1 + 5^3 = 125 + 3^3 = 27
        = 153

Step 4: Compare sum with original number
        153 == 153? True

Result: 153 IS an Armstrong number!
```

### Example 2: 123 (Not Armstrong Number)

```
--- Checking if 123 is an Armstrong number ---
Step 1: Extract digits from 123
        Digits: [1, 2, 3]
        Number of digits: 3

Step 2: Calculate each digit raised to the power of 3
        1^3 = 1
        2^3 = 8
        3^3 = 27

Step 3: Sum all the powers
        1^3 = 1 + 2^3 = 8 + 3^3 = 27
        = 36

Step 4: Compare sum with original number
        36 == 123? False

Result: 123 IS NOT an Armstrong number!
```

### Example 3: 9474 (4-digit Armstrong Number)

```
--- Checking if 9474 is an Armstrong number ---
Step 1: Extract digits from 9474
        Digits: [9, 4, 7, 4]
        Number of digits: 4

Step 2: Calculate each digit raised to the power of 4
        9^4 = 6561
        4^4 = 256
        7^4 = 2401
        4^4 = 256

Step 3: Sum all the powers
        9^4 = 6561 + 4^4 = 256 + 7^4 = 2401 + 4^4 = 256
        = 9474

Step 4: Compare sum with original number
        9474 == 9474? True

Result: 9474 IS an Armstrong number!
```

## Quick Check Results

Here are quick results for various test numbers:

```
   0: ✓ Armstrong
   1: ✓ Armstrong
   2: ✓ Armstrong
   3: ✓ Armstrong
 153: ✓ Armstrong
 371: ✓ Armstrong
 407: ✓ Armstrong
1634: ✓ Armstrong
8208: ✓ Armstrong
9474: ✓ Armstrong
 123: ✗ Not Armstrong
 456: ✗ Not Armstrong
```

## Armstrong Numbers by Digit Count

### 1-digit Armstrong numbers
All single digits (0-9) are Armstrong numbers because `d¹ = d`

### 3-digit Armstrong numbers
- 153: `1³ + 5³ + 3³ = 1 + 125 + 27 = 153`
- 371: `3³ + 7³ + 1³ = 27 + 343 + 1 = 371`
- 407: `4³ + 0³ + 7³ = 64 + 0 + 343 = 407`

### 4-digit Armstrong numbers
- 1634: `1⁴ + 6⁴ + 3⁴ + 4⁴ = 1 + 1296 + 81 + 256 = 1634`
- 8208: `8⁴ + 2⁴ + 0⁴ + 8⁴ = 4096 + 16 + 0 + 4096 = 8208`
- 9474: `9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474`

## Error Handling

The implementation includes robust error handling for:

### Invalid Input Types
```
Testing String input: "153"
Error caught: Input must be an integer
```

### Negative Numbers
```
Testing Negative number: -5
Error caught: Input must be non-negative
```

### Float Numbers
```
Testing Float number: 3.14
Error caught: Input must be an integer
```

## Additional Features

### Range Finder Function

The `find_armstrong_numbers_in_range(start, end)` function can discover Armstrong numbers within specified ranges:

```
Armstrong numbers between 0-10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Armstrong numbers between 100-200: [153]
Armstrong numbers between 1000-2000: [1634]
Armstrong numbers between 8000-10000: [8208, 9474]
```

## Performance Considerations

- **Time Complexity**: O(d) where d is the number of digits
- **Space Complexity**: O(d) for storing digit strings
- **Optimization**: Uses generator expression for efficient sum calculation

## Usage Examples

### Basic Usage
```python
from armstrong_checker import is_armstrong_number

# Check if a number is Armstrong
result = is_armstrong_number(153)  # Returns True
```

### Verbose Output
```python
from armstrong_checker import is_armstrong_number_verbose

# Get detailed step-by-step explanation
is_armstrong_number_verbose(153)  # Prints detailed steps
```

### Find Armstrong Numbers
```python
from armstrong_checker import find_armstrong_numbers_in_range

# Find all Armstrong numbers in a range
armstrong_list = find_armstrong_numbers_in_range(100, 200)
```

## Mathematical Properties

1. **Single digits**: All digits 0-9 are Armstrong numbers
2. **No 2-digit Armstrong numbers exist**
3. **Finite set**: There are only a finite number of Armstrong numbers
4. **Distribution**: Armstrong numbers become increasingly rare as digit count increases

## Conclusion

This implementation provides a complete, robust, and educational approach to checking Armstrong numbers, with comprehensive error handling, detailed documentation, and step-by-step explanations suitable for learning and practical use.