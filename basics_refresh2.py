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
#     If your solution is not correct, then try to understand the error
#     messages, watch the video again, rewrite the solution, and test it again.
#     Repeat this step until you get the correct solution.
#     Save the solution in a file for future reference or recap.

## Challenge #1
# Write a Python function that takes a list as an argument and returns a new list
# with unique elements of the first list in the same order.
# Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
# Unique List : [1, 2, 3, 4, 5]
# def unique_set(l1):
#     return(list(set(l1)))     # Set may not return same order
# l1 = [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
# print(unique_set(l1))
#
# def unique_list(my_list):
#     tmp_list = list()
#     for x in my_list:
#         if x not in tmp_list:
#             tmp_list.append(x)
#     return tmp_list
# friends = ['Dan', 'Maria', 'Dan', 'Dan', 'John', 'Dan']
# print(unique_list(friends))

## Challenge #2
# Write a Python function to check whether a number is perfect or not.
# The function should return True if the number is perfect and False otherwise.
# Perfect numbers: https://www.britannica.com/science/perfect-number
# def check_if_perfect(num1):
#     l1=list()
#     for i in range(1, int(num1/2)+1):
#         if num1 % i == 0:
#             l1.append(i)
#     sum1 = sum(l1)
#     # print(sum1, l1)       # for debug
#     if sum1 == num1:
#         print(f"{num1} is perfect")
#     else:
#         print(f"{num1} is not perfect")
# check_if_perfect(6)
# check_if_perfect(9)
# check_if_perfect(28)
# check_if_perfect(333)
# check_if_perfect(496)

# def all_divisors(n):
#     """
#      This function returns all divisors of a number
#     """
#     divisors = []
#     for x in range(1, int(n/2)+1):
#         if n % x == 0:
#             divisors.append(x)
#     return divisors
# def perfect_number(n):
#     divs = all_divisors(n)
#     if sum(divs) == n:
#         return True
#     else:
#         return False
# # calling the function
# n = 496
# if perfect_number(n):
#     print(f'{n} is one rare of a kind number, it\'s a perfect number')
# else:
#     print(f'Nothing special about {n}, it\'s no perfect number')

## Challenge #3
# Create a function that takes an integer as an argument and returns True if
# it’s a prime number and False otherwise.

# def all_divisors(n):
#     """
#      This function returns all divisors of a number
#     """
#     divisors = []
#     for x in range(1, int(n/2)+1):
#         if n % x == 0:
#             divisors.append(x)
#     return divisors
# def check_if_prime(num1):
#     my_divisors = all_divisors(num1)
#     if len(my_divisors) == 1:
#         print(f"{num1} is prime number.")
#     else:
#         print(f"{num1} is not prime number.")
# check_if_prime(3)
# check_if_prime(6)
# check_if_prime(7)

# def is_prime(n):
#     prime = True
#     if n == 1: # 1 is not a prime number, the first prime numnber is 2
#         return False
#     i = 1
#     while i < n // 2:
#         i = i + 1
#         if n % i == 0:
#             prime = False
#             break
#     return prime # returns True or False

## Challenge #4
# Using the function defined in the previous challenge find 5 prime numbers greater
# than 1,000,000
# Solution 1:
# check_num = 1000000
# count_num = 0
# while count_num < 5:
#     check_num += 1
#     if is_prime(check_num):
#         count_num += 1
#         print(check_num)
# Solution 2:
# primes = []
# for n in range(1_000_000, 100_000_000):
#    if is_prime(n):
#        primes.append(n)
#        if len(primes) == 5:
#            break
#
# print(primes)


## Challenge #5
# Write a function that takes in a list as an argument and returns the Equilibrium
# Index of the list.
# If there isn't such an index it returns False.
# Equilibrium index: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

# def equilibrium_index(my_list):
#     for x in range(0,len(my_list)):
#         if sum(my_list[:x]) == sum(my_list[x+1:]):
#             return x
#     return False
#
# nums = [2, 3, 10, 5]
# print(equilibrium_index(nums))  # => 2
#
# nums = [3, 3, 10, 5]
# print(equilibrium_index(nums))  # => False

## Challenge #6
# Change the solution of the previous challenge so that the function receives a
# string of numbers separated by a comma.
# Example:
# nums = '2, 3, 10, 5'
# print(equilibrium_index(nums)) # => 2
# nums = '3, 3, 10, 5'
# print(equilibrium_index(nums)) # => False

# def equilibrium_index(my_str):
#     my_list = my_str.split(',')   # => string to list
#     my_list = [int(n) for n in my_list]  # => converting the list of strings to a list of ints
#
#     for x in range(0,len(my_list)):
#         if sum(my_list[:x]) == sum(my_list[x+1:]):
#             return x
#
#     return False
#
# nums = '2, 3, 10, 5'
# print(equilibrium_index(nums))  # => 2
#
# nums = '3, 3, 10, 5'
# print(equilibrium_index(nums))  # => False

## Files
# open( <file>, <chars>)
# Character Meaning  # from help(open)
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)  -- use r+
#     'U'       universal newline mode (deprecated)

# fpath = "D:\\My_Recordings\\Python_Master\\Downloads\\"
# f = open(fpath + 'configuration.txt', 'r')
# content = f.read()
# print(content)
#
# print(f.closed)
# f.close()
# print(f.closed)

# head -1 configuration.txt  => 012345678790
# f = open(fpath + 'configuration.txt', 'r')
# content = f.read(3)     # => 012
# print(content)
# content = f.read(3)     # => 345
# print(content)
# print(f.tell())         # cursor position = 6
# content = f.seek(2)
# print(f.read(2))        # => 23
# content = f.seek(0)     # cursor position = 0
# print(f.read(2))        # => 01
# print(f.tell())         # cursor position = 2
# f.close()
# print(content)

#with ... as ... :  will close the file after reading contents.
# with open(fpath + 'configuration.txt', 'r') as f:
#     content = f.read()
#     print(content)
# print(f.closed)

# with open(fpath + 'configuration.txt') as f:    # 'rt' is default
#     my_list = f.read().splitlines()       # will remove \n from lines
#     print(my_list[0:2])     # ['#12345678790', 'hostname Router1']
# with open(fpath + 'configuration.txt') as f:    # 'rt' is default
#     my_list = f.readlines()
#     print(my_list[0:2])     # ['#12345678790\n', 'hostname Router1\n']

# with open(fpath + 'configuration.txt') as f:    # 'rt' is default
#     print(f.readline(), end="")
#     print(f.readline(), end="")

# with open(fpath + 'configuration.txt') as f:    # 'rt' is default
#     for line in f:              # Does readline (which retains \n)
#         print(line, end="")     # Use end="" to not add additional \n

# with open(fpath + 'configuration.txt') as f:    # 'rt' is default
#     for line in f:
#         print(line, end="")

# with open(fpath + 'myfile.txt', 'w') as f:    # 'rt' is default
#     f.write("mytext\n")
#     f.write("moretext\n")

# with open(fpath + 'myfile.txt', 'r+') as f:    # read + write
#     print(f.readline())
#     f.write("mytext\n")
#     f.write("moretext\n")

###############################
##Working with Files in Python
##############################
#
# ## Opens a file named a.txt and returns a file object called f
# ## a.txt it's in the same directory with the python script
# ## use a correct relative or absolute path
# f = open('a.txt', 'r')  # it will be opened in read-only mode
#
# content = f.read()  # reads the entire file as a string
# print(content)
#
# f.closed  # => False, file is not closed
#
# ## Closes the file
# f.close()
#
# ## Opens the file in read-only mode and reads its contents in a list
# ## the file object will be automatically closed
# with open('a.txt', 'r') as my_file:
#     content = my_file.readlines()  # content is a list
#
# my_file.closed  # => True, my_file has been closed automatically
#
# ## file object is an iterable object
# with open('a.txt', 'r') as my_file:
#     for line in my_file:  # iterating over the lines within the file
#         print(line, end='')
#
# ## Opens the file in write-mode.
# ## Creates the file if it doesn't exist or overwrites the file if it already exists
# with open('my_file.txt', 'w') as file:
#     file.write('This file will be overwritten!')
#
# ## Opens the file in append-mode.
# ## Creates the file if it doesn't exist or appends to its end if it exists
# with open('another_file.txt', 'a') as file:
#     file.write('Appending to the end!')
#
# ## Opens the file for both read and write
# ## Doesn't create the file if it doesn't exist
# with open('my_file.txt', 'r+') as file:
#     file.seek(0)  # the cursor is positioned at the beginning of the file
#     file.write('Writing and the beginning')  # writing and the beginning
#
#     file.seek(5)  # moving the cursor at position 5
#     content = file.read(10)  # reading 10 characters starting from position 5
#     print(content)

# Challenge #1
#
# Create a Python script that reads a text file into a list and then converts the list back into a string
# which is the entire file content.

fpath = "D:\\My_Recordings\\Python_Master\\Downloads\\"
# with open(fpath + "sample_file.txt", 'r') as f:
#     content = f.read().splitlines()
#     my_str = '\n'.join(content)
#     print(my_str)


# Challenge #2
#
# Create a Python function called tail that reads the last n lines of a text file. The function has two
# arguments: the file name and n (the number of lines to read). This is similar to the Linux `tail` command.

# import time
# def tail(file, n):
#     if type(n) == int:
#         print("int")
#     with open(file, 'r') as f:
#         content = f.read().splitlines()
#         last = content[len(content)-n:]
#         # return(last)
#         my_str = '\n'.join(last)
#         return(my_str)

# t = tail(fpath + 'sample_file.txt', 3)
# print(t)


# Challenge #3
#
# Change the solution from the previous challenge so that the script that prints out the last n lines of
# the file refreshes the output every 3 seconds (as the file changes or updates). This is similar to the
# tail -f Linux command.

# while True:
#     t = tail(fpath + 'sample_file.txt', 3)
#     print(t)
#     time.sleep(3)
#     print('')

# import time
# def tail(file, n):
#     while True:
#         with open(file, 'r') as f:
#             content = f.read().splitlines()
#             if type(n) == int:
#                 last = content[len(content)-n:]
#             else:
#                 last = content[len(content)-3:]
#             # return(last)
#             my_str = '\n'.join(last)
#         print(my_str)
#         if type(n) == int:
#             break
#         time.sleep(3)
#
#     return(my_str)
#
# # t = tail(fpath + 'sample_file.txt', 3)
# # print(t)
# t = tail(fpath + 'sample_file.txt', '-f')

# Challenge #4
#
# Write a Python program to count the number of lines, words, and characters in a text file. This is similar
# to the Linux `wc` command. Create a function if possible.

def wc(file):
    with open(file) as f:
        content = f.read().splitlines()
        lines = len(content)
        words = 0
        for line in content:
            words += len(line.split())
        chars = 0
        for line in content:
            chars += len(list(line))
        return lines, words, chars

print(wc(fpath + 'sample_file.txt'))


# Challenge #5
#
# Write a Python program that calculates the net amount of a bank account based on the transactions saved in a text file.
# The file format is as follows:
# D:50
# W:100
# D means deposit while W means withdrawal.
# Suppose that the following file is supplied to the program:
# D:300
# D:300
# W:500
# D:200
# Then, the output should be: 300

# with open('banking.txt', 'r') as f:
#     content = f.read().splitlines()
#     # print(content)
#
#     deposit, withdrawal = 0, 0
#
#     for item in content:
#         tmp = item.split(':')
#         # print(tmp) # -> ['D', '300']
#         if  tmp[0] == 'D':
#             deposit += int(tmp[1])
#         elif tmp[0] == 'W':
#             withdrawal += int(tmp[1])
#         else:
#             print('File format error')
#
#     balance = deposit - withdrawal
#     print(balance)

# Challenge #6
#
# Write a Python script that compares two text files line by line and displays the lines that differ.

# with open('a.txt') as f:
#     file1 = f.read().splitlines()
#
# with open('b.txt') as f:
#     file2 = f.read().splitlines()
#
# file = list(zip(file1, file2))
#
# i = 0
# for item in file:
#     i += 1
#     if item[0] != item[1]:
#         print(f'file1 ({i}): {item[0]}, file2 ({i}): {item[1]}')


# Challenge #7
#
# Consider this dictionary file.
# Write a Python script that reads the file in a dictionary. The words in the file will be the
# dictionary keys and the length of each word the corresponding values.

# with open('american-english.txt') as f:
#     words = f.read().splitlines()
#
#     words_and_length = dict()
#     for w in words:
#         words_and_length[w] = len(w)
#
#     for k, v in words_and_length.items():
#         print(f'{k} -> {v}')

# Challenge #8
#
# Consider the dictionary file from the previous challenge.
# Write a Python script that finds the first 100 longest words in the file.

# with open('american-english.txt') as f:
#     words = f.read().splitlines()
#
#     words_and_length = dict()
#     for w in words:
#         words_and_length[w] = len(w)
#
#     # print(words_and_length)
#     words_list = sorted(words_and_length.items(), key=lambda x:x[1], reverse=True)
#     print(words_list[:100])

# Challenge #9
#
# Consider this dictionary file.
# Write a Python script that finds the number of occurrences of each letter of the alphabet in all the
# words in the dictionary.
# You want to see how many times do ‘a’, ‘b’, ‘c’ and so on appear in all the words in the dictionary.
# Which is the most frequently used letter in English words?

# import string
#
# letters = dict()
# # initializing the dictionary with all letters as keys and zero as values
# for c in string.ascii_lowercase:
#     letters[c] = 0
#
# # print(letters)
# with open('american-english.txt', 'r') as words:
#     for w in words:
#         for char in string.ascii_lowercase:
#             letters[char] += w.count(char)
#
# print(letters)

# Challenge #10
#
# Continue the previous challenge and find the 3 most frequently used letters in all English Words.
# You should get: ('e', 67681), ('s', 50872), ('i', 50818)

# import string
#
# letters = dict()
# # initializing the dictionary with all letters as keys and zero as values
# for c in string.ascii_lowercase:
#     letters[c] = 0
#
# # print(letters)
# with open('american-english.txt', 'r') as words:
#     for w in words:
#         for char in string.ascii_lowercase:
#             letters[char] += w.count(char)
#
# print(sorted(letters.items(), key=lambda x:x[1], reverse=True))

#################################
## Exceptions Handling
## Exceptions are run-time Errors
#################################

# a = 2
# # for ZeroDivisionError
# # b = 0
#
# # for TypeError
# b = '0'
# # for another Exception
# # del b
#
# try:
#     ## try to execute this block of code!
#     c = a / b
# except ZeroDivisionError as e:
#     ## This block of code is executed when a ZeroDivisionError occurs
#     print(f'There was Division by zero: {e}')
# except TypeError as e:
#     ## This block of code is executed when a TypeError occurs
#     print(f'There was a Type Error: {e}')
# except Exception as e:
#     ## This block of code is executed when other exception occurs
#     print(f'Other exception accured: {e}')
# else:
#     ## This block of code is executed when no exception occurs
#     print(f'No exception raised. c is {c}')
# finally:
#     print('This block of code is always executed!')
#
# print('Continue script execution..')
# x = 2

import pandas
