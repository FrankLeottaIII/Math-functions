#Math funtions

#Author: Frank Robert Leotta III
#Date started: 2/9/2024

#Discription: This is a repository of math functions that I have written for various projects.  

#left off at add_string_ascii_word, the ones tabed out
            

# Please use word wrap to see the code properly.

#Imports
import math

#table of contents:
#add
#subtract
#multiply
#divide
#is_even
#is_odd
#add_string_ascii_word # this adds 2 strings together based on their ascii values.  Its technically correct, and good for a laugh.
#add_string_ascii_number






####################################################################################################

def add(a,b):
    """Summery: This function adds two varibles together and returns the result.  The varibles must be the same type (int, float, or string).  If the varibles are strings, they will be concatinated together.  If the varibles are floats, they will be added together and the result will be a float.  If the varibles are ints, they will be added together and the result will be an int.

    Note: you will need to convert the varibles to the same type before using this function if you want to add a string to a number.
    
    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        int: The sum of the two numbers.
    
    """
    return a+b



################### Creating more functions ####################

def add_string_ascii_number(a,b):
    """Summery: This function adds two strings together and returns the result.  The strings are first converted to their ascii values and then added together.  The result is then converted back to a string and returned.  This is just for fun, and is tecnically correct, and good for a laugh.
    It give you a number, not a letter.


    Args:
        a (string): The first string to be added.
        b (string): The second string to be added.

    Returns:
        string: The sum of the two strings.
    
    """
    a = str(a)
    b = str(b)
    a = ord(a)
    b = ord(b)
    return str(a+b)

a = 'a'
b = 'b'

C= add_string_ascii_number(a,b)
print(C)





# def add_and_wrap_around(lst, index, amount):
#     """
#     Adds the specified amount to the given index in the list,
#     wrapping around if the index exceeds the list length.
#     """
#     new_index = (index + amount) % len(lst)
#     lst[new_index] += amount

# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# index_to_modify = 2  # Choose an index within the list
# amount_to_add = 7

# add_and_wrap_around(my_list, index_to_modify, amount_to_add)
# print(my_list)  # Output: [1, 2, 10, 4, 5]






#issue if = if b is greater than a, then it will be negative

#now if handled the opposite... need a fork in the road


def add_string_ascii_word(a,b):
    """Summery: This function adds two words that are string together and returns the result.  It preserves the number of original number of letters in the word.  The strings are first converted to their ascii values and then added together.  The result is then converted back to a string and returned.  This is just for fun, and is tecnically correct, and good for a laugh.
    This will only print upper case and lower case letters, as well as underscore spaces.  It will not print any other characters.

    Args:
        a (string): The first string to be added.
        b (string): The second string to be added.

    Returns:
        string: The sum of the two strings.
    
    """
    # print ("this is a")
    # print(a)
    # print ("this is b")
    # print(b)

    a_count = len(a)
    b_count = len(b)
    a = list(a)
    b = list(b)
    c= []
    #reverse order of a
    a.reverse()
    # print ("this is a")
    # print(a)
    numberleftover = len(a) - len(b)
    # if numberleftover <= 0:
    #     numberleftover = 
    # print("this is numberleftover")
    # print(numberleftover)



    #if numberleftover is less than or equal to 0, pass

    # NEW PART OF CODE WORKING ON
    if numberleftover < 0:
        a.reverse()
        b.reverse()
        for i in range(abs(numberleftover)):
            c.append(b[i])
        # print("this is c")
        # print(c)
        c.reverse()
        # print("this is c after reverse")
        # print(c)
        b.reverse() 
        a = list(a)  #copied from
        b = list(b)
        #for every element in a, convert to ascii 
        for i in range(len(a)):
            a[i] = ord(a[i])
        #for every element in b, convert to ascii
        for i in range(len(b)):
            b[i] = ord(b[i])
            # print(i)
        new_a = []
        #add elements together and place in new_a
        for a, b in zip(a, b):
            new_a.append(a + b)


        
            # new_a.append(a[i] + b[i]) 
        # print("this is new_a after adding a and b together")
        # print(new_a)
        #for each element
        #  if  i <= 65 subtract 122 from i
        # i >=122 subtract 122 until i =< eless than 122
        for i in range(len(new_a)):
            if new_a[i] <= 65:
                new_a[i] = new_a[i] - 122
            else:
                while new_a[i] > 122:
                    new_a[i] = new_a[i] - 122
        
        # print("this is new_a")
        # print(new_a)
        #now to loop around so that all elements are between 65 and 122
        for i in range(len(new_a)):
            if new_a[i] <= 65:
                new_a[i] = new_a[i] - 122
        # print("this is new_a")
        # print(new_a)

        #absolute value to get rid of negatives
        for i in range(len(new_a)):
            new_a[i] = abs(new_a[i])


        # if element is 91, add 1 to it
        for i in range(len(new_a)):
            if new_a[i] == 91: #if element is 91, add 1 to it
                new_a[i] = new_a[i] + 1
        for i in range(len(new_a)):
            if new_a[i] == 92:
                new_a[i] = new_a[i] + 2
        for i in range(len(new_a)):
            if new_a[i] == 93:
                new_a[i] = new_a[i] + 3
        for i in range(len(new_a)):
            if new_a[i] == 94:
                new_a[i] = new_a[i] + 4
        for i in range(len(new_a)):
            if new_a[i] == 96:
                new_a[i] = new_a[i] + 5

        # print("this is new_a")
        # print(new_a)
        #this will ensure each element is between 65 and 122, a letter of the alphabet
        #convert each element back to a letter
        for i in range(len(new_a)):
            new_a[i] = chr(new_a[i])
        
        # print("this is new_a")
        # print(new_a)
        #convert new_a to a string
        new_a = ''.join(new_a)
        # print("this is c")
        # print(c)
        c = ''.join(c)
        new_a = new_a + c
        test ="test"
        new_a = new_a + test

        #return new_a
        return new_a







    elif numberleftover >= 0:
        #transfer every element  in a up to the lens(numberleftover) to c
        for i in range(abs(numberleftover)):
            c.append(a[i])
        # print("this is c")
        # print(c)
        c.reverse()
        # print("this is c after reverse")
        # print(c)
        a.reverse() 
        # print ("this is a")
        # print(a)
        a = list(a)
        b = list(b)
        #for every element in a, convert to ascii 
        for i in range(len(a)):
            a[i] = ord(a[i])
        #for every element in b, convert to ascii
        for i in range(len(b)):
            b[i] = ord(b[i])
            # print(i)
        new_a = []
        #add elements together and place in new_a
        for a, b in zip(a, b):
            new_a.append(a + b)


        
            # new_a.append(a[i] + b[i]) 
        # print("this is new_a after adding a and b together")
        # print(new_a)
        #for each element
        #  if  i <= 65 subtract 122 from i
        # i >=122 subtract 122 until i =< eless than 122
        for i in range(len(new_a)):
            if new_a[i] <= 65:
                new_a[i] = new_a[i] - 122
            else:
                while new_a[i] > 122:
                    new_a[i] = new_a[i] - 122
        
        # print("this is new_a")
        # print(new_a)
        #now to loop around so that all elements are between 65 and 122
        for i in range(len(new_a)):
            if new_a[i] <= 65:
                new_a[i] = new_a[i] - 122
        # print("this is new_a")
        # print(new_a)

        #absolute value to get rid of negatives
        for i in range(len(new_a)):
            new_a[i] = abs(new_a[i])


        # if element is 91, add 1 to it
        for i in range(len(new_a)):
            if new_a[i] == 91: #if element is 91, add 1 to it
                new_a[i] = new_a[i] + 1
        for i in range(len(new_a)):
            if new_a[i] == 92:
                new_a[i] = new_a[i] + 2
        for i in range(len(new_a)):
            if new_a[i] == 93:
                new_a[i] = new_a[i] + 3
        for i in range(len(new_a)):
            if new_a[i] == 94:
                new_a[i] = new_a[i] + 4
        for i in range(len(new_a)):
            if new_a[i] == 96:
                new_a[i] = new_a[i] + 5

        # print("this is new_a")
        # print(new_a)
        #this will ensure each element is between 65 and 122, a letter of the alphabet
        #convert each element back to a letter
        for i in range(len(new_a)):
            new_a[i] = chr(new_a[i])
        
        # print("this is new_a")
        # print(new_a)
        #convert new_a to a string
        new_a = ''.join(new_a)
        #add c to new_a
        # print("this is c")
        # print(c)
        c = ''.join(c)
        new_a = new_a + c
        test ="test"
        new_a = new_a + test

        #return new_a
        return new_a



A = "hello how are you doing today"
print(A)
b = "I am doing well thank you for asking.  Who are you again? "
print(b)
print(" this is the result of adding two sentences together based on their ascii values.")

print(add_string_ascii_word(A,b)) 

#ok, now I would like to see if I can put back the spaces and punctuation

def Get_memory_of_spaces(list1: list)->list:
    """ Summery: 
        This funtion keeps a memory of spaces in a sentence converted into a list.  
        It uses an if statment to analyze list1 and make a list called list 2 comprised of 0 and _ in which the 0 represents a letter and the _ represents a space.  This is useful for the add_string_ascii_word function.  The list is then returned.

        
    Args:
        list1 (list): The list to be analyzed.

    Returns:
        list2: The list that is returned.
    """
    list2 = []
    for i in range(len(list1)):
        if list1[i] == " ":
            list2.append("_")
        else:
            list2.append(0)
    return list2



def add_string_ascii_sentences(a,b):
    """Summery:
    This function adds two sentences together based on their ascii values.  The result is then converted back to a string and returned.  This funtion also keeps the spaces and punctuation of the original sentence.  

    Args:
        a (string): The first string to be added.
        b (string): The second string to be added.

    Returns:
        string: The sum of the two strings.
    
    """
    # print ("this is a")
    # print(a)
    # print ("this is b")
    # print(b)

    a_count = len(a)
    b_count = len(b)
    a = list(a)
    a_spaces = Get_memory_of_spaces(a)
    print("this is a_spaces")
    print(a_spaces)
    b = list(b)
    c= []
    #reverse order of a
    a.reverse()
    # print ("this is a")
    # print(a)
    numberleftover = len(a) - len(b)
    # if numberleftover <= 0:
    #     numberleftover = 
    # print("this is numberleftover")
    # print(numberleftover)



    #if numberleftover is less than or equal to 0, pass

    # NEW PART OF CODE WORKING ON
    if numberleftover < 0:
        a.reverse()
        b.reverse()
        for i in range(abs(numberleftover)):
            c.append(b[i])
        # print("this is c")
        # print(c)
        c.reverse()
        # print("this is c after reverse")
        # print(c)
        b.reverse() 
        a = list(a)  #copied from
        b = list(b)
        #for every element in a, convert to ascii 
        for i in range(len(a)):
            a[i] = ord(a[i])
        #for every element in b, convert to ascii
        for i in range(len(b)):
            b[i] = ord(b[i])
            # print(i)
        new_a = []
        #add elements together and place in new_a
        for a, b in zip(a, b):
            new_a.append(a + b)


        
            # new_a.append(a[i] + b[i]) 
        # print("this is new_a after adding a and b together")
        # print(new_a)
        #for each element
        #  if  i <= 65 subtract 122 from i
        # i >=122 subtract 122 until i =< eless than 122
        for i in range(len(new_a)):
            if new_a[i] <= 65:
                new_a[i] = new_a[i] - 122
            else:
                while new_a[i] > 122:
                    new_a[i] = new_a[i] - 122
        
        # print("this is new_a")
        # print(new_a)
        #now to loop around so that all elements are between 65 and 122
        for i in range(len(new_a)):
            if new_a[i] <= 65:
                new_a[i] = new_a[i] - 122
        # print("this is new_a")
        # print(new_a)

        #absolute value to get rid of negatives
        for i in range(len(new_a)):
            new_a[i] = abs(new_a[i])


        # if element is 91, add 1 to it
        for i in range(len(new_a)):
            if new_a[i] == 91: #if element is 91, add 1 to it
                new_a[i] = new_a[i] + 1
        for i in range(len(new_a)):
            if new_a[i] == 92:
                new_a[i] = new_a[i] + 2
        for i in range(len(new_a)):
            if new_a[i] == 93:
                new_a[i] = new_a[i] + 3
        for i in range(len(new_a)):
            if new_a[i] == 94:
                new_a[i] = new_a[i] + 4
        for i in range(len(new_a)):
            if new_a[i] == 96:
                new_a[i] = new_a[i] + 5

        # print("this is new_a")
        # print(new_a)
        #this will ensure each element is between 65 and 122, a letter of the alphabet
        #convert each element back to a letter
        for i in range(len(new_a)):
            new_a[i] = chr(new_a[i])
        print("this is new_a")
        print(new_a)

                                                        # for i in range(len(new_a)):
                                                        #     for a in a_spaces:
                                                        #         if a == "_":
                                                        #             a[i] = "_"
        #convert new_a to a string
        new_a = ''.join(new_a)
        # print("this is c")
        # print(c)
        c = ''.join(c)
        new_a = new_a + c
        test ="test"
        new_a = new_a + test

        #return new_a
        return new_a







    elif numberleftover >= 0:
        #transfer every element  in a up to the lens(numberleftover) to c
        for i in range(abs(numberleftover)):
            c.append(a[i])
        # print("this is c")
        # print(c)
        c.reverse()
        # print("this is c after reverse")
        # print(c)
        a.reverse() 
        # print ("this is a")
        # print(a)
        a = list(a)
        b = list(b)
        #for every element in a, convert to ascii 
        for i in range(len(a)):
            a[i] = ord(a[i])
        #for every element in b, convert to ascii
        for i in range(len(b)):
            b[i] = ord(b[i])
            # print(i)
        new_a = []
        #add elements together and place in new_a
        for a, b in zip(a, b):
            new_a.append(a + b)


        
            # new_a.append(a[i] + b[i]) 
        # print("this is new_a after adding a and b together")
        # print(new_a)
        #for each element
        #  if  i <= 65 subtract 122 from i
        # i >=122 subtract 122 until i =< eless than 122
        for i in range(len(new_a)):
            if new_a[i] <= 65:
                new_a[i] = new_a[i] - 122
            else:
                while new_a[i] > 122:
                    new_a[i] = new_a[i] - 122
        
        # print("this is new_a")
        # print(new_a)
        #now to loop around so that all elements are between 65 and 122
        for i in range(len(new_a)):
            if new_a[i] <= 65:
                new_a[i] = new_a[i] - 122
        # print("this is new_a")
        # print(new_a)

        #absolute value to get rid of negatives
        for i in range(len(new_a)):
            new_a[i] = abs(new_a[i])


        # if element is 91, add 1 to it
        for i in range(len(new_a)):
            if new_a[i] == 91: #if element is 91, add 1 to it
                new_a[i] = new_a[i] + 1
        for i in range(len(new_a)):
            if new_a[i] == 92:
                new_a[i] = new_a[i] + 2
        for i in range(len(new_a)):
            if new_a[i] == 93:
                new_a[i] = new_a[i] + 3
        for i in range(len(new_a)):
            if new_a[i] == 94:
                new_a[i] = new_a[i] + 4
        for i in range(len(new_a)):
            if new_a[i] == 96:
                new_a[i] = new_a[i] + 5

        # print("this is new_a")
        # print(new_a)
        #this will ensure each element is between 65 and 122, a letter of the alphabet
        #convert each element back to a letter
        for i in range(len(new_a)):
            new_a[i] = chr(new_a[i])
        

                                                        # for i in range(len(new_a)):
                                                        #     for a in a_spaces:
                                                        #         if a == "_":
                                                        #             a[i] = "_"
                                                        #     if i == "_":
                                                        #         a[i] = "_"


        # print("this is new_a")
        # print(new_a)
        #convert new_a to a string
        new_a = ''.join(new_a)
        #add c to new_a
        # print("this is c")
        # print(c)
        c = ''.join(c)
        new_a = new_a + c
        test ="test"
        new_a = new_a + test

        #return new_a
        return new_a
    
A = "hello how are you doing today"
print(A)
b = "I am doing well thank you for asking.  Who are you again? "
print(b)
print(" this is the result of adding two sentences together based on their ascii values.")
print(add_string_ascii_sentences(A,b))