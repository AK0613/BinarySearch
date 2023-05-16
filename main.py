# Binary search
# Problem: Given an array of integers sorted in ascending order, return the starting and ending index of a given target
# value in an array, i.e. [x,y] -> [1, 3, 3, 5, 5, 5, 8, 9] for 5, starting index is 3 and ending index is 5
# IF the value is not found, return -1. All values will be positive

def binary_search(array, value, low, high):
    if high >= low:
        # Get the middle point
        mid = low + (high - low) // 2

        # If the value we are looking for is at that index, return it.
        if array[mid] == value:
            return mid
        # If the value at index mid is less than the value we are looking for, pass only the right half of the array
        elif value > array[mid]:
            return binary_search(array, value, mid + 1, high)
        # If the value is less than the midpoint, then send the left half
        elif value < array[mid]:
            return binary_search(array, value, low, mid - 1)
    else:
        return -1


def binary_search_range(array, value):
    # If the array has elements
    if len(array) > 1:
        # Find first occurrence of target #
        first_index = binary_search(array, value, 0, len(array) - 1)
        # If it exists
        if first_index >= 0:
            # Initialize pointers to look for other identical values
            start_pos = first_index
            end_pos = first_index
            # Look to the left of the first occurrence until the value can no longer be found
            while start_pos != -1:
                temp = start_pos
                start_pos = binary_search(array, value, 0, start_pos - 1)
            # use the last valid position for the numer we are looking for
            start_pos = temp
            # Look to the right of the initial number until we find the last occurrence of the target value
            while end_pos != -1:
                temp2 = end_pos
                end_pos = binary_search(array, value, end_pos + 1, len(array) - 1)
            # Use the last valid position
            end_pos = temp2

            return [start_pos, end_pos]
        else:
            return [-1, -1]
    else:
        return [-1, -1]


__name__ = "__main__"
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(array, 5, 0, len(array) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

array2 = [1, 2, 3, 3, 3, 3, 3, 3]
result2 = binary_search_range(array2, 3)
print(result2)
