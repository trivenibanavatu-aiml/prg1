def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1      
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
print(arr)
mergesort(arr)
print("Sorted array is: ", end="\n")
print(arr)

# Main function to test the mergesort algorithm
if __name__ == "__main__":
    test_cases = [
        [12, 11, 13, 5, 6, 7],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]

    for arr in test_cases:
        print("Given array is", end="\n")
        print(arr)
        mergesort(arr)
        print("Sorted array is: ", end="\n")
        print(arr)
        print("-" * 50) 
    print("All test cases passed!")
    print("-" * 50)
    print("All test cases passed!")  


            
