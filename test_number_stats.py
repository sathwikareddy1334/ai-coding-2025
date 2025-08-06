from number_stats import calculate_stats

def test_calculate_stats():
    """
    Test the calculate_stats function with various examples.
    """
    # Test case 1: Integer numbers
    numbers1 = [1, 2, 3, 4, 5]
    result1 = calculate_stats(numbers1)
    print("Test 1 - Integer numbers:", numbers1)
    print(f"Mean: {result1['mean']:.2f}, Min: {result1['min']}, Max: {result1['max']}")
    print()
    
    # Test case 2: Float numbers
    numbers2 = [1.5, 2.7, 3.9, 4.1, 5.8]
    result2 = calculate_stats(numbers2)
    print("Test 2 - Float numbers:", numbers2)
    print(f"Mean: {result2['mean']:.2f}, Min: {result2['min']}, Max: {result2['max']}")
    print()
    
    # Test case 3: Mixed integers and floats
    numbers3 = [10, 15.5, 20, 25.3, 30]
    result3 = calculate_stats(numbers3)
    print("Test 3 - Mixed numbers:", numbers3)
    print(f"Mean: {result3['mean']:.2f}, Min: {result3['min']}, Max: {result3['max']}")
    print()
    
    # Test case 4: Negative numbers
    numbers4 = [-5, -2, 0, 3, 8]
    result4 = calculate_stats(numbers4)
    print("Test 4 - Including negative numbers:", numbers4)
    print(f"Mean: {result4['mean']:.2f}, Min: {result4['min']}, Max: {result4['max']}")
    print()
    
    # Test case 5: Single number
    numbers5 = [42]
    result5 = calculate_stats(numbers5)
    print("Test 5 - Single number:", numbers5)
    print(f"Mean: {result5['mean']:.2f}, Min: {result5['min']}, Max: {result5['max']}")
    print()
    
    # Test error cases
    print("Testing error cases:")
    
    try:
        calculate_stats([])
        print("Empty list test: FAILED (should raise ValueError)")
    except ValueError as e:
        print(f"Empty list test: PASSED - {e}")
    
    try:
        calculate_stats("not a list")
        print("Non-list input test: FAILED (should raise TypeError)")
    except TypeError as e:
        print(f"Non-list input test: PASSED - {e}")
    
    try:
        calculate_stats([1, 2, "three", 4])
        print("Non-numeric element test: FAILED (should raise ValueError)")
    except ValueError as e:
        print(f"Non-numeric element test: PASSED - {e}")

if __name__ == "__main__":
    test_calculate_stats()