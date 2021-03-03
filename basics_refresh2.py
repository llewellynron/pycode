## Section 11+ coding exercises

# # Functions Review
# def say_my_name(my_name):
#     """
#     Documentation string is recommended.
#     :param my_name:
#     :return:
#     """
#     print('My name is {}'.format(my_name))
#     # return value is 'None' if not specified.
#
# ## Calling the function
# say_my_name('John')
#
# help(say_my_name)

# ## Function that calculates the VAT (value-added tax)
# ## The 1st argument is the price and the second argument is the vat percentage
# ## Exemple: if price is 200 and vat percentage is 5%, then vat is 10
# def get_vat(price, vat):
#     return (price * vat) / 100
#
# ## Calling the function
# vat = get_vat(200, 5)
# print(vat)

#################################
## Intro to Functions
#################################

# ## Use "def" to create new functions
# def my_function1():
#     """
#     This is function's docstring.
#     """
#     print('This is a function!')
#     # this function returns implicitly None
#
# ## Calling the function
# my_function1()  # => This is a function!
# print("Value returned from my_function1: ", my_function1())     # returns:  None
#
# my_function1.__doc__  # => This is function's docstring.
# help(my_function1)

# ## return exits the function
# def my_function2():
#     x = 1
#     return x  # the function ends here
#     print('Never reaches this line!')  # it will never execute this line
#
# ## Calling the function
# my_function2()  # returns 1

# ## A function can return more values as a tuple
# def add_multiply_power(x, y):
#     return x + y, x * y, x ** y
#
# ## Calling the function
# a, b, c = add_multiply_power(2, 3)  # returns (2 + 3, 2 * 3, 2 ** 3)
# print(a, b, c)  # => 5 6 8

########################
## Function's Arguments
########################

# ## Function with positional arguments
# def add(x, y):
#     print(f"x is {x} and y is {y}")
#     return x + y  # Returns the result of x + y with a return statement
#
# # Calling function with positional arguments
# s = add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11, s is 11
#
# ## Calling function with keyword arguments
# s = add(y=1, x=8)  # => prints out "x is 8 and y is 1" and returns 9, s is 9

# ## Function with default arguments
# def add(x=1, y=0):
#     print(f"x is {x} and y is {y}")
#     return x + y  # Returns the result of x + y with a return statement
#
# ## Calling function with default arguments
# s = add()  # => prints out "x is 1 and y is 0" and returns 1, s is 1
# s = add(5)  # => prints out "x is 5 and y is 0" and returns 5, s is 5
# s = add(5, 3)  # => prints out "x is 5 and y is 3" and returns 8, s is 8

# Wrong way to define a function => SyntaxError: non-default argument follows default argument
# def my_function(a, b=5, c):
#     print(a, b, c)


# # Function that takes a variable number of positional arguments
# def concatenate(*args):
#     result = ''
#     for tmp in args:
#         result = result + tmp
#     return result
#
# ## Calling the function
# result = concatenate()
# print(result)  # => '' -> empty string
#
# result = concatenate('Python', '!')
# print(result)  # => Python!
#
# result = concatenate('I', 'love ', 'programming')
# print(result)  # => Ilove programming


# # Function that takes a variable number of keyword arguments
# # kwargs is a dictionary!!
# # kwargs is a dictionary!!
# def device_info(**kwargs):  # kwargs is a dictionary
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
# ## Calling the function
# # It prints out:
# # ip: 10.0.0.1
# # username: u1
# # password: secretpass
# device_info(name='Cisco Router', ip='10.0.0.1', username='u1', password='secretpass')

# #################################
# ## Scopes and Namespaces
# #################################
# x = 3  # this is a global scoped variable
# print("line 130")
#
# def my_func1():
#     print(f'x is {x}')  # this is "x" variable from the global namespace
# ## Calling the function
# my_func1()  # => x is 3
#
#
# def my_func2():
#     x = 6  # this is a local scoped variable
#     print(f'x is {x}')  # this is NOT "x" variable from the global namespace
# ## Calling the function
# my_func2()  # => x is 6
# print(x)  # => 3 -> "x" variable was not modified inside the function
#
#
# def my_func3():
#     global x  # importing x variable from the global namespace
#     x = x * 10  # this is "x" variable from the global namespace
#     print(f'x is {x}')
# ## Calling the function
# my_func3()  # => x is 30
# print(x)  # => 30 -> global "x" variable was modified inside the function
#
#
# def my_func4():
#     print(f'x is {x}')
#     x += 7  # this is an error, we used local x before assignment
#
# ## Calling the function
# my_func4()  # => UnboundLocalError: local variable 'x' referenced before assignment

# ## Global variable x
# x = 10
# def increment():
#     global x  # this is the global variable x, not a copy
#     x += 1  # incrementing the global variable x
# ## Calling the function
# increment()
# ## Printing the value of x after calling the function (x is 11)
# print(x)

#########################
## Lambda Expressions
#########################

# ## Traditional function vs lambda function
# ## def add(x, y)
# ##     return(x + y)
# # "x" and "y" are lambdas arguments.
# add = lambda x, y: x + y  # this creates a function
# type(add)  # => function
#
# ## Assigning lambda expression to a variable
# result = add(2, 3)  # => 5
#
# ## We can use default arguments
# add = lambda x=1, y=0: x + y
# result = add()  # => 1

# ## We can even use *args and **kwargs
# my_function = lambda x, *args, **kwargs: (x, *args, {**kwargs})
# # x is 2.3, args is (a, b, c) and kwargs is {arg1='abc', arg2='def', arg3='geh'}
# my_function(2.3, 'a', 'b', 'c', arg1='abc', arg2='def', arg3='geh')
#
# ## Passing as an argument to a function
# ## Lambdas are functions and can therefore be passed to any other function as an argument (or returned from another function)
# def my_func(x, fn):
#     return fn(x)
#
# result = my_func(2, lambda x: x ** 2)
# print(result)  # => 4
#
# result = my_func(2, lambda x: x ** 3)
# print(result)  # => 8
#
# result = my_func('a', lambda x: x * 3)
# print(result)  # => 'aaa'
#
# result = my_func('a:b:c', lambda x: x.split(':'))
# print(result)  # => ['a', 'b', 'c'] -> this is a list
#
# result = my_func(('p', 'y', 't', 'h', 'o', 'n'), lambda x: '-'.join(x))
# print(result)  # => p-y-t-h-o-n > this is a string

# def reverse(my_str):
#     """
#     This function returns a new string with all characters reversed.
#     """
#     return my_str[::-1]  # slicing with a step of -1
# output = reverse('Beautiful')
# print(output)  # => lufituaeB

# def vowel_count(my_str):
#     """
#     This function counts the number of vowels in a string
#     """
#     vowels = 'aeiou'
#     my_str = my_str.lower()  # ignoring the case (we consider only lower-case letters)
#
#     # Dictionary that stores the result.
#     result = dict()
#
#     for char in my_str:
#         if char in vowels:
#             if char in result.keys():
#                 result[char] += 1
#             else:
#                 result[char] = 1
#
#     return result
#
#
# # r = vowel_count('Awesome')
# # print(r)  # => {'a': 1, 'e': 2, 'o': 1}
#
# r = vowel_count('Wow! Python is great!')
# print(r)  # => {'o': 2, 'i': 1, 'e': 1, 'a': 1}
#
# # transform dictionary into sorted dictionary
# r_sorted = sorted(r.keys())
# print(r_sorted)
# d_sorted = dict()
# for item in r_sorted:
#     d_sorted[item] = r[item]
# print(d_sorted)

# def counter(my_str):
#     vowels = 'aeiou'
#     no_of_vowels = 0
#
#     for char in vowels:
#         # letter case doesn't matter
#         my_str = my_str.lower()  # make a lowercase copy of my_str
#         no_of_vowels += my_str.count(char)
#
#     no_of_consonants = len(my_str) - no_of_vowels
#
#     return (no_of_vowels, no_of_consonants)
#
# print(counter('Python'))  # => (1, 5)
# print(counter('BeautifUl'))  # => (5, 4)

## Hands-On Challenges - Functions
# 
# How to solve these coding challenges:
# 
#     Write your solution in PyCharm or in your preferred Python IDE.
# 
#     If your solution is not correct, then try to understand the error messages, watch the video again, rewrite the solution, and test it again. Repeat this step until you get the correct solution.
# 
#     Save the solution in a file for future reference or recap.
# 
# 
## Challenge #1
# Write a Python function that takes a list as an argument and returns a new list
# with unique elements of the first list in the same order.
# Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
# Unique List : [1, 2, 3, 4, 5]


## Challenge #2
# Write a Python function to check whether a number is perfect or not.
# The function should return True if the number is perfect and False otherwise.
# Perfect numbers: https://www.britannica.com/science/perfect-number
# Are you stuck? Do you want to see the solution to this exercise? Click here.


## Challenge #3
# Create a function that takes an integer as an argument and returns True if
# it’s a prime number and False otherwise.
# Are you stuck? Do you want to see the solution to this exercise? Click here.


## Challenge #4
# Using the function defined in the previous challenge find 5 prime numbers greater
# than 1,000,000
# Are you stuck? Do you want to see the solution to this exercise? Click here.


## Challenge #5
# Write a function that takes in a list as an argument and returns the Equilibrium
# Index of the list.
# If there isn't such an index it returns False.
# Equilibrium index: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
# Are you stuck? Do you want to see the solution to this exercise? Click here.


## Challenge #6
# Change the solution of the previous challenge so that the function receives a
# string of numbers separated by a comma.
# Example:
# nums = '2, 3, 10, 5'
# print(equilibrium_index(nums)) # => 2
# nums = '3, 3, 10, 5'
# print(equilibrium_index(nums)) # => False

