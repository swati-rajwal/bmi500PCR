# Python implementation of Merge Sort algorithm

def merge_sort(arr):
    """
    Recursive function to implement Merge Sort.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list.
    """
    
    if len(arr) <= 1: # Here i check if input array has 1 or 0 elements
        return arr  # already sorted
    mid = len(arr) // 2  # Otherwise, find middle point

    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    """
    Function to merge two sorted lists into one sorted list.
    
    Parameters:
    left (list): The first sorted list.
    right (list): The second sorted list.
    
    Returns:
    list: The merged sorted list.
    """
    sorted_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):  # Compare elements from both lists and merge them in sorted order
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):        # If there are remaining elements in the left list, add them
        sorted_list.append(left[i])
        i += 1
    while j < len(right):       # If there are remaining elements in the right list, add them
        sorted_list.append(right[j])
        j += 1
    return sorted_list

if __name__ == "__main__":
    input_list = [1000,5,39,9,45,98,600,5621] # Example
    print("Original List:", input_list)
    
    sorted_list = merge_sort(input_list)
    print("Sorted List:", sorted_list)