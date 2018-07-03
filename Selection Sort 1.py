# Python program for the implementation of Selection Sort

# Function to do Selection sort
def selectionSort(ar):

    i = 0
    while i < len(ar):
        # smallest element in the sublist
        smallest = min(ar[i:])
        # index of smallest element
        index_of_smallest = ar.index(smallest)
        # swapping
        ar[i], ar[index_of_smallest] = ar[index_of_smallest], ar[i]
        i = i + 1

    for elements in ar:
        print(elements)


# Driver code to test above
ar = [49, 25, 26, 2, 99]
print("Sorted array is:")
selectionSort(ar)
