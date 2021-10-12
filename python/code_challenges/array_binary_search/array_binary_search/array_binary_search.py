

def BinarySearch(input,array):

    starting_Value=0


    End_val=len(array)-1

    Mid_value=0

    while starting_Value<=End_val:

        Mid_value=(End_val+starting_Value)



        if array[Mid_value] < input:

            starting_Value=Mid_value+1


        elif array[Mid_value]>input:


                End_val=Mid_value-1

        else:

          return Mid_value

    return -1



    """
the function called a  BinarySearch that make a serch in array
and serch for index  and  that have 3 parameters called start point
and end point and mid point  and there is condition that check the value id

    """

