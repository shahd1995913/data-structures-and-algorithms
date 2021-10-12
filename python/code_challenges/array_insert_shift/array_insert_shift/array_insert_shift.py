def insertShiftArray():

    array=[2,4,6,-8]

    print("The Original array :",array)

    newItemToAdd=5

    TheNewArray=[]

    TheNewArray=array[:len(array)//2] +[newItemToAdd]+array[len(array)//2:]

    print("The array after add" , int(newItemToAdd) )

    print(TheNewArray)

insertShiftArray()

