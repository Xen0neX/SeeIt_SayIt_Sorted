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

    # iterate over all elements
    for i in range(len(unsorted_list)):

        # find the smallest element
        min_index = i
        for j in range(i+1, len(unsorted_list)):
            # if current value in the list is smaller than the first value, swap the index to denote minimum value
            if unsorted_list[min_index] > unsorted_list[j]:
                min_index = j

        # One the loop is finished, swap the values using the index
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

    return unsorted_list


if __name__ == '__main__':
    print("Executed Directly")
