"""
create a function that called a Mergesort
that take array of integer and returnd a new ordered array

using 2 method 1st one called a Mergesort and the 2nd called Merge


"""

def Mergesort(arr):
    n=len(arr)
    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right= arr[mid:n]
        Mergesort(left)
        Mergesort(right)
        return Merge(left, right, arr)

def Merge(left, right, arr):
        i = 0
        j=0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        if j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        elif i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        return arr





# print(Mergesort([10,18,26,205,4,3]))
