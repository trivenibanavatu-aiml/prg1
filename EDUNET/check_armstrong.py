# Python program to check if a number is Armstrong or not

def is_armstrong(number):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is equal to the sum of its digits each raised 
    to the power of the number of digits.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if the number is Armstrong, False otherwise
    
    Examples:
        153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
        371 = 3³ + 7³ + 1³ = 27 + 343 + 1 = 371 ✓
    """
    # Convert number to string to get individual digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to the power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if sum equals the original number
    return sum_of_powers == number


# Get input from user
try:
    num = int(input("Enter a number to check if it's an Armstrong number: "))
    
    # Check if the number is Armstrong
    if is_armstrong(num):
        print(f"\n✓ {num} is an Armstrong number")
        
        # Show the calculation (optional detail)
        num_str = str(num)
        num_digits = len(num_str)
        calculation = " + ".join(f"{digit}^{num_digits}" for digit in num_str)
        sum_value = sum(int(digit) ** num_digits for digit in num_str)
        print(f"   ({calculation} = {sum_value})")
    else:
        print(f"\n✗ {num} is not an Armstrong number")
    
except ValueError:
    print("Error: Please enter a valid integer number only.")


