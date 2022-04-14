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
    if n == None:
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


if __name__ == '__main__':
    print("Executed Directly")
