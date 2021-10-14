
"""
the function called a  BinarySearch that make a serch in array
and serch for index  and  that have start point
and end point and mid_val point  and
 there is condition that check the value that is search exisit in array
 if exisit  return value if not return -1
    """

def  Binarysearch(arr,value):
    starting = 0
    ending= len(arr)-1
    mid_val=0
    # use the while loop for checking the ending value i > or equal the start value
    while ending >=  starting :
        mid_val = (ending + starting) // 2
        if arr[mid_val] == value:
            return mid_val
        if arr[mid_val] > value:
            ending=mid_val-1
        else :
            starting=mid_val+1
    # When the value not exisit in array return -1
    return( -1)


if  __name__ == "__main__" :
     arr  =  [ 1,2,3,4,5,8,70,100,200,300,78 ]
     value  = 100
     results = Binarysearch(arr,value)
if results != -1:
         print("The Index of the value is : ", results)
else:
        print("The value not exisit in array = -1 ")












