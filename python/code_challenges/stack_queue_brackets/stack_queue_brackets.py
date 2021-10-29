
"""
function named that check the validate_brackets Multi-bracket Validation.
"""
def validate_brackets(input_data):


    list = []


    for i in input_data:

        if i in ["(", "{", "["]:

            """ if the string start from ["(", "{", "["]  this correct
            then push element in the stack  """
            """
            list can be used as a stack.
            Instead of push(), append() is used to add elements to the top of the stack
            while pop() removes the element in LIFO order.
            """
            list.append(i)
        else:
            """
            if the string not belong ["(", "{", "["] then it will be close
            brackets like this [")","}","]"]
            the stack list have element
            """

            if not list:
                """ check if the list is full"""

                return False

            current = list.pop()

            """ Round Brackets """

            if current == '(':

                if i != ")":

                    return False

            if current == '{':
                """ Curly Brackets """

                if i != "}":

                    return False

            if current == '[':
                """ Square Brackets """

                if i != "]":

                    return False

    """
     checking if the list is not contain any element

    """
    if list:

        return False

    return True



# if __name__ == "__main__":

#     input_data = "({}]"

# print(validate_brackets(input_data))
