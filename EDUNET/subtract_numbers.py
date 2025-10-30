# Python program for subtraction of two numbers

def subtract_numbers(a, b):
    """
    Subtract two numbers and return the result.
    
    Args:
        a (float): First number (minuend)
        b (float): Second number (subtrahend)
    
    Returns:
        float: Difference of a and b
    """
    return a - b


# Get input from user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate the difference
    result = subtract_numbers(num1, num2)
    
    # Display the result
    print(f"\nThe difference of {num1} and {num2} is: {result}")
    
except ValueError:
    print("Error: Please enter valid numbers only.")


