
import math
"""
Create a function called insertShiftArray
take  array and a value to be added in the array .
the new value it will add in the mid of array .

"""
def insertShiftArray(array, new_val_to_add):

    print("The Original array :",array)

    divid_len = math.ceil((len(array))/2)

    newarray = array[-1]
    """
using a for loop for make a loop in array
 and then add the new value in mid of array

"""
    for value in range(divid_len, len(array)):

        arr_val = array[value]

        array[value] = new_val_to_add

        new_val_to_add = arr_val

    array += [newarray]

    print("The new array after adding a vlaue in mide of array is :",array)

insertShiftArray([1,2,7,3],4)

