def calculate_stats(numbers):
    """
    Calculate mean, minimum, and maximum values from a list of numbers.
    
    Args:
        numbers (list): A list of numeric values (int or float)
    
    Returns:
        dict: A dictionary containing 'mean', 'min', and 'max' values
    
    Raises:
        ValueError: If the list is empty or contains non-numeric values
        TypeError: If input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Check if all elements are numeric
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError(f"All elements must be numeric. Found: {type(num).__name__}")
    
    # Calculate statistics
    mean = sum(numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    return {
        'mean': mean,
        'min': minimum,
        'max': maximum
    }


def read_numbers_from_input():
    """
    Read numbers from user input and return as a list.
    
    Returns:
        list: A list of numbers entered by the user
    """
    print("Enter numbers separated by spaces (or commas):")
    user_input = input().strip()
    
    # Handle both space and comma separated inputs
    if ',' in user_input:
        number_strings = user_input.split(',')
    else:
        number_strings = user_input.split()
    
    numbers = []
    for num_str in number_strings:
        try:
            # Try to convert to int first, then float
            if '.' in num_str:
                numbers.append(float(num_str.strip()))
            else:
                numbers.append(int(num_str.strip()))
        except ValueError:
            raise ValueError(f"Invalid number: '{num_str.strip()}'")
    
    return numbers


def main():
    """
    Main function to demonstrate the number statistics calculator.
    """
    try:
        # Read numbers from user input
        numbers = read_numbers_from_input()
        
        # Calculate statistics
        stats = calculate_stats(numbers)
        
        # Display results
        print(f"\nStatistics for the numbers: {numbers}")
        print(f"Mean: {stats['mean']:.2f}")
        print(f"Minimum: {stats['min']}")
        print(f"Maximum: {stats['max']}")
        
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()