# Python program for addition and subtraction of two numbers
# Python program for addition, subtraction, and multiplication of two numbers

def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtract two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Difference of a and b (a - b)
    """
    return a - b

def multiply_numbers(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    return a * b


# Get input from user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate results
    sum_result = add_numbers(num1, num2)
    difference_result = subtract_numbers(num1, num2)
    product_result = multiply_numbers(num1, num2)
    
    # Display the results
    print(f"\nThe sum of {num1} and {num2} is: {sum_result}")
    print(f"The difference of {num1} and {num2} is: {difference_result}")
    print(f"The product of {num1} and {num2} is: {product_result}")
    
except ValueError:
    print("Error: Please enter valid numbers only.")


