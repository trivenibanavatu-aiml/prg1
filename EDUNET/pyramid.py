def print_pyramid(symbol, rows):
    """
    Print a pyramid shape using the given symbol.
    
    Args:
        symbol (str): The character/symbol to use for the pyramid
        rows (int): Number of rows in the pyramid
    """
    for i in range(1, rows + 1):
        # Print leading spaces (for centering)
        spaces = rows - i
        print(' ' * spaces, end='')
        
        # Print the symbol
        # Each row has (2*i - 1) symbols
        print(symbol * (2 * i - 1))


def main():
    print("=" * 50)
    print("Pyramid Pattern Generator")
    print("=" * 50)
    
    # Get input from user
    symbol = input("Enter the symbol to use for the pyramid (e.g., '*', '#', 'x'): ")
    
    try:
        rows = int(input("Enter the number of rows: "))
        
        if rows <= 0:
            print("Please enter a positive number of rows!")
            return
        
        print("\nPyramid:")
        print_pyramid(symbol, rows)
        
    except ValueError:
        print("Please enter a valid number for rows!")


if __name__ == "__main__":
    main()
