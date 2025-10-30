"""
Python Program to Find Inverse of a 2x2 Matrix

For a 2x2 matrix: [[a, b],
                   [c, d]]

Inverse = (1/det) * [[d, -b],
                     [-c, a]]

where det = a*d - b*c
"""

def input_matrix():
    """Get 2x2 matrix input from user"""
    print("Enter the elements of the 2x2 matrix:")
    print("Format: Matrix = [[a, b],")
    print("                  [c, d]]\n")
    
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    
    return [[a, b], [c, d]]

def calculate_determinant(matrix):
    """Calculate determinant of 2x2 matrix"""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def inverse_matrix(matrix):
    """Calculate inverse of 2x2 matrix"""
    det = calculate_determinant(matrix)
    
    if det == 0:
        return None, det  # Matrix is singular, no inverse exists
    
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    
    # Formula for 2x2 matrix inverse
    inv = [[d/det, -b/det],
           [-c/det, a/det]]
    
    return inv, det

def display_matrix(matrix, name="Matrix"):
    """Display matrix in readable format"""
    print(f"\n{name}:")
    for row in matrix:
        print(f"[{row[0]:8.3f}, {row[1]:8.3f}]")

def main():
    print("=" * 50)
    print("    2x2 Matrix Inverse Calculator")
    print("=" * 50)
    
    # Get matrix input
    matrix = input_matrix()
    
    # Display original matrix
    display_matrix(matrix, "Original Matrix")
    
    # Calculate determinant
    det = calculate_determinant(matrix)
    print(f"\nDeterminant = {det:.3f}")
    
    # Calculate and display inverse
    inv_matrix, det = inverse_matrix(matrix)
    
    if inv_matrix is None:
        print("\n❌ ERROR: The matrix is singular (determinant = 0)")
        print("The inverse does not exist for this matrix.")
    else:
        display_matrix(inv_matrix, "Inverse Matrix")
        
        # Verify the inverse by multiplying
        print("\n" + "=" * 50)
        print("Verification (Original × Inverse):")
        
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += matrix[i][k] * inv_matrix[k][j]
        
        display_matrix(result, "Result (should be Identity Matrix)")
        
        # Check if result is close to identity matrix
        is_identity = all(abs(result[i][j] - (1 if i == j else 0)) < 0.001 
                         for i in range(2) for j in range(2))
        
        if is_identity:
            print("\n✅ Verification successful!")

 ±      
if __name__ == "__main__":
    main()


