from number_stats import calculate_stats

# Example usage with predefined data
def example_usage():
    """
    Demonstrate the calculate_stats function with example data.
    """
    # Example 1: Quiz scores
    quiz_scores = [85, 92, 78, 96, 88, 91, 82]
    stats = calculate_stats(quiz_scores)
    print("Quiz Scores Analysis:")
    print(f"Scores: {quiz_scores}")
    print(f"Average Score: {stats['mean']:.2f}")
    print(f"Lowest Score: {stats['min']}")
    print(f"Highest Score: {stats['max']}")
    print()
    
    # Example 2: Temperature readings
    temperatures = [23.5, 25.1, 22.8, 26.3, 24.7, 23.9, 25.8]
    stats = calculate_stats(temperatures)
    print("Temperature Readings (°C):")
    print(f"Readings: {temperatures}")
    print(f"Average Temperature: {stats['mean']:.2f}°C")
    print(f"Minimum Temperature: {stats['min']}°C")
    print(f"Maximum Temperature: {stats['max']}°C")
    print()
    
    # Example 3: Stock prices
    stock_prices = [150.25, 148.90, 152.10, 149.75, 151.60, 153.20, 150.85]
    stats = calculate_stats(stock_prices)
    print("Stock Price Analysis:")
    print(f"Prices: {stock_prices}")
    print(f"Average Price: ${stats['mean']:.2f}")
    print(f"Lowest Price: ${stats['min']:.2f}")
    print(f"Highest Price: ${stats['max']:.2f}")

if __name__ == "__main__":
    example_usage()