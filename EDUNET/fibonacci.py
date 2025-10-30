# Python program to generate Fibonacci series

def fibonacci(n):
    """
    Generate Fibonacci series up to n terms.
    In Fibonacci series, each number is the sum of the two preceding ones.
    Series starts with: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    
    Args:
        n (int): Number of terms to generate
    
    Returns:
        list: List containing the Fibonacci series
    
    Examples:
        fibonacci(5) returns [0, 1, 1, 2, 3]
        fibonacci(10) returns [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    # Handle special cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the series with first two terms
    fib_series = [0, 1]
    
    # Generate remaining terms
    for i in range(2, n):
        next_term = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_term)
    
    return fib_series


# Get input from user
try:
    terms = int(input("Enter the number of terms for Fibonacci series: "))
    
    if terms < 0:
        print("Error: Number of terms cannot be negative.")
    else:
        # Generate the Fibonacci series
        result = fibonacci(terms)
        
        # Display the result
        if result:
            print(f"\nFibonacci series with {terms} terms:")
            print(result)
            print("\nSequence:", ", ".join(map(str, result)))
        else:
            print("\nEmpty series. Please enter a positive number.")
    
except ValueError:
    print("Error: Please enter a valid integer number only.")

