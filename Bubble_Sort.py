# Python program for the implementation of Bubble Sort

def bubbleSort(ar):
    n = len(ar)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j]


# Driver code to test above
ar = [110, 34, 25, 32, 28, 10, 90]

bubbleSort(ar)

print("Sorted array is:")
for i in range(len(ar)):
    print("%d" % ar[i]),
