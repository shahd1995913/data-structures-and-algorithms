"""

create a function called a InsertionSort that take array of integer and return orderded
array of integers

args : array of integers

return : orderded array

"""



def InsertionSort(arr=[]):
  len1=len(arr)
  for i in range(1,len1):
    j=i-1
    temp=arr[i]

    while j>=0 and temp < arr[j]:
      arr[j+1]=arr[j]
      j=j-1
    arr[j+1]=temp

  return(arr)
