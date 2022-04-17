# Arihant Kuba 14th April 2022
# This is a project documenting various sorting algorithms in python along with the test benches to test them
# each sort is written out as its own function and also lists its space and time complexity


def selection_sort(unsorted_list):
    # select the lowest element from an array of size n
    # swap it with the first element of the array
    # exclude the first element and repeat for an array of size n-1 until n is 0

    # Complexity O(n^2)
    # Auxiliary Space O(1)
    # In place
    # Not stable

    # length of the list
    n = len(unsorted_list)

    # iterate over all elements
    for i in range(n):

        # find the smallest element
        min_index = i
        for j in range(i + 1, n):
            # if current value in the list is smaller than the first value, swap the index to denote minimum value
            if unsorted_list[min_index] > unsorted_list[j]:
                min_index = j

        # One the loop is finished, swap the values using the index
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

    return unsorted_list


def bubble_sort(unsorted_list):
    # checks each adjacent value from the start and compares them one at a time in a 'bubble'
    # swaps the values if they are in the wrong order
    # if no swaps were made produces the final result
    # repeats the loop until there are no swaps made in a pass though

    # Worst time complexity O(n^n)
    # best time complexity (when already solved) O(n)
    # Auxiliary Space O(1)
    # In place
    # Stable

    # length of the list
    n = len(unsorted_list)

    for i in range(n):

        # variable to check if anything was swapped
        swapped = False

        # Ignore the last i elements as those were already sorted
        for j in range(0, n - i - 1):

            # Compare each 'bubble' and swap if they are not in the right order
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        # break if there was a loop when nothing was swapped
        if swapped == False:
            break

    return unsorted_list


def recursive_bubble_sort(unsorted_list, n=None):
    # Same complexity as the normal implementation of bubble sort

    # For the first call, iterate over the whole list
    if n is None:
        n = len(unsorted_list)

    # return the sorted list when the length is 1
    if n == 1:
        return unsorted_list

    # After each loop in each recursion, the last element is bubbled out
    for i in range(n - 1):
        if unsorted_list[i] > unsorted_list[i + 1]:
            unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]

    # as the last element is fixed n-1 of the array is called. when the last call returns the value, it's passed back
    # to the first call as well
    return recursive_bubble_sort(unsorted_list, n - 1)


def insertion_sort(unsorted_list):
    # use the position of elements to evaluate their positions by keys
    # Compare each element with its predecessor, if the key element is smaller than the previous value, check the one
    # before, Move all elements after the position the element has to be inserted up one position value and place the
    # key element in the right place

    # Complexity O(n^2)
    # Auxiliary Space O(1)
    # In place
    # Stable

    n = len(unsorted_list)

    for i in range(1, n):

        # assign the current iterator as the key
        key = unsorted_list[i]

        # j is the element before the Key element i
        j = i - 1

        # go through every element before the key element to see if it needs to be moved
        # j >=0 checks to see the end of the list
        # key < unsorted_list[j] check to see if the key is smaller than the element before it
        while j >= 0 and key < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]
            # Assign J as the new key (as the value was shifted, and then reduce the value to j by 1 for the next check
            j -= 1

        unsorted_list[j+1] = key

    return unsorted_list


def recursive_insertion_sort(unsorted_list, n=None):
    # same complexity as normal insertion sort

    # checks if this is the first call and assigns n
    if n is None:
        n = len(unsorted_list)

    # return the list when the length is 1, base case
    if n == 1:
        return unsorted_list

    # key of the unsorted list is set to the last element and j is the element just before that
    key = unsorted_list[n - 1]
    j = n - 2

    # works the same way as normal insertion sort
    while j >= 0 and unsorted_list[j] > key:
        unsorted_list[j + 1] = unsorted_list[j]
        j -= 1

    unsorted_list[j + 1] = key

    # recursively call the function for a list of size n-1
    return recursive_insertion_sort(unsorted_list, n - 1)


if __name__ == '__main__':
    print("Executed Directly")
