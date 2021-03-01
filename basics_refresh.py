# Style Guide:  https://www.python.org/dev/peps/pep-0008/

#############################
##Numbers and Math Operators
#############################
#
# a = 9
# b = 4
# ## Arithmetic Operators
# a + b  # addition operator => 13
# a - b  # subtraction operator => 5
# a * b  # multiplication operator => 36
# a / b  # division operator => 2.25
# a // b  # floor division operator => 2
# 5.0 // 3.0  # => 1.0 # works on floats too
# a ** b  # exponentiation operator (a to the power of b) => 6561
# a % b  # modulus operator => 1
#
# ## Assignment Operators
# a = 5
# a += 2  # Shorthand for a = a + 2 => a = 7
# a -= 3  # Shorthand for a = a - 3 => a = 4
# a /= 2  # Shorthand for a = a / 2 => a = 2
# a *= 3  # Shorthand for a = a * 3 => a = 6
# a **= 2  # Shorthand for a = a ** 2 => a = 36
#
# ## Arithmetic Built-in Function
# divmod(9, 4)  # returns the quotient and remainder when using floor(integer) division => (2, 1)
# sum([1, 2, 4])  # returns the sum of an iterable => 7
# min(1, -2, 3)  # returns the minimum value => -2
# max(1, 2, 4)  # returns the maximum value => 4
# a = 10 / 3  # a = 3.3333333333
# round(a, 4)  # returns a number rounded with 4 decimals => 3.3333
# pow(2, 4)  # 2 ** 4 = 16
#
# mytuple = (1, 2, 4)
# print(max(mytuple))
# mymod, myrem = divmod(9, 4)
# print(f"mymod= {mymod} \t myrem = {myrem}")

#############################
## Comparison and Identity Operators
#############################
#
# # Assignment is =
# a = 2
# b = 3
#
# # Equality is == and compares the values stored by the variables
# a == b  # => False
# b == b  # => True
#
# # Inequality is !=
# a != b  # => True
#
# # More comparisons
# a > b  # => False
# 5 >= 5  # => True
# b <= a  # => False
#
# 'Python' == 'python'  # => False - case matters
#
# id(a)  # => returns the address where the value referenced by a is stored 140464475242000
#
# # is checks if two variables refer to the same object (saved at the same memory address)
# a is b  # => False = compares the address of a to the address of b

# stra = "abc"
# strb = "abc"
# strc = "abcdef"
# print("ida =", id(stra), "idb=", id(strb))
# print(f"ida = {id(stra)} idb= {id(strb)}")
# print(f"ida = {id(stra)} idb= {id(strc[0:3])} and strings match is {stra==strc[0:3]}")  # True
# print(stra is strb)  # is True

#################################
## Boolean Variables
#################################

# ## True equals 1 and False equals 0
# True == 1  # => True
# bool(True)  # => 1
#
# False == 0  # => True
# bool(False)  # => 0
#
# 1 is True  # => False
# 0 is False  # => False
#
# True > False  # => True
# a = (True + True) * 10  # => 20
#
# id(True)  # => 10714848 (you'll obtain another value)
# id(4 > 2)  # => 10714848  - the address of True and False is constant during program execution
#
# # The next 2 expressions are equivalent
# (4 > 2) == True  # => True
# (4 > 2) is True  # => True
#
# ## Truthiness of objects
# bool(0)  # => False
# bool(0.0)  # => False
# bool(0.0001)  # => True  (not zero)
# bool(10)  # => True
# bool(-1.5)  # => True  (not zero)
#
# bool('')  # => False (empty string)
# bool('py')  # => True
#
# bool([])  # => False (empty list)
# bool([1, 2])  # => True
#
# bool(())  # => False (empty tuple)
# bool((3, 4))  # => True
#
# bool({})  # => False (empty dictionary or set)
# bool({1: 'abc', 2: 55, 'a': 5})
# bool({ 1, 2, 3})  # => True

#################################
## Boolean Operators
#################################
# exp1 and exp2 -> True when both expressions are True and False otherwise
# exp1 or exp2  -> True when any expression is True

# a, b = 3, 5
#
# a < 10 and b < 10  # => True
# a < 10 and b > 10  # => False
#
# a < 10 or b < 10  # => True
# a < 10 or b > 10  # => True
#
# # The next 2 expressions are equivalent
# 2 < a < 6        # => True
# a < 2 and a < 6  # more readable
#
# a != 7 or b > 100  # => True
#
# not a == a  # => False
# a == 3 and not b == 7  # => True
#
# not a > 10 and b < 10  # => True
#
# a < 10 or b > 10  # => True
# not a < 10 or b > 10  # => False
# not (a < 10 or b > 10)  # => False
#
# # !!!!!!!!!!!
# # Python considers in fact 4 > 2 and 2 == True.
# 4 > 2 == True    # => False
# (4 > 2) == True  # => True
# 4 > 2 and True   # => True
#
# x = 2 * 2
# y = 'Python'
#
# ## This will be evaluated to False
# result1 = bool(y) and not (x >= 4)
# print(result1)
#
# print('Py' in y)   # True
# ## This will be evaluated to True
# result2 = (not x > 0) or 'Py' in y
# print(result2)

#################################
## Intro to Strings
#################################

# ## strings (str objects) are enclosed by single or double quotes (' or "). Just be consistent within your code!
# message1 = 'I love Python Programming!'
# message2 = "I love Python Programming!"
#
# ## print() function displays the content of the string variable at console
# print(message1)
#
# # hello1 = 'Hi there! I'm Andrei'   # => error, cannot use ' inside ' ' or " inside " "
# hello1 = 'Hi there! I\'m Andrei'  # => correct. ' inside ' ' must be escaped  using \
# hello2 = "Hi there! I'm Andrei"  # you can use ' inside " " or " inside ' '
#
# ## Instructions between """ or ''' are treated as comments. It's recommended to use # to comment individual lines
# """
# This is a multiline comment
# a = 5
# print(a)
# Comment ends here.
# """
#
# ## This is a multiline string
# languages = """ I learn Python,
# Java,
# Go,
# PHP.
# """
# print(languages)
# same_languages = " I learn Python,\nJava, \nGo, \nPHP.\n"
# print(f"languages content is the same: {languages == same_languages}")  # True
#
# # \n is a new line
# print('Hello \nWorld!')  # => it displays Hello World! on 2 lines
#
# ## \ is used to escape characters that have a special meaning
# info = '\\ character is used to escape characters that have a special meaning'
# print(info)  # => \ character is used to escape characters that have a special meaning
#
# info1 = "'Jonathan' is an apple variety and \"Chardonnay\" is a grape variety"
# ## Alternative solution
# # info1 = '\'Jonathan\' is an apple variety and "Chardonnay" is a grape variety'
#
# info2 = '\\n is a newline escape sequence'
# ## Alternative solution
# # info2 = "\\n is a newline escape sequence"
#
# print(info1)
# print(info2)

#################################
## User Input and Type Casting
#################################

# ## Simple way to get user input from console
# input_string_var = input("Enter some data: ")  # Returns the data as a string
# print(input_string_var * 3)   # Can int multiply strings to produce longer strings
# print(input_string_var * 0)   # return empty string
# print(input_string_var * -1)  # return empty string
# # To perform arithmetic operations we must cast to int or float
# a = input('Enter number str a: ')  # => a stores string
# b = int(input('Enter int b: '))  # => b stores an int
# c = float(a) * b  # => here I multiply a float by an int, will get runtime error if a is not numeric
# print(type(c), c)
#
# ## Type casting
# a = 3  # => type int
# b = 4.5  # => type float
# c = '1.2'  # => type str
#
# print('a is ' + str(a))  # => str(a) returns a string from an int
# print('b is ' + str(b))  # => str(b) returns a string from a float
# d = b * float(c)  # => here I multiply 2 floats. d is a float.
#
# str1 = '12 a'
# # float(str1)    # => error
# a = '1.5'
# b = '2'
# # Using Type Casting create a new variable called c that stores the result of a multiplied by b. c stores a float and will be 3.0.
# c = float(a) * float(b)
#
# my_str = 'Python is TIOBE language of the year 2018!'
# my_pos = '0123456789_123456789_123456789_123456789_'
#
# # define a variable named s1 that stores the character T from the string above. Use a positive index to get the character T
# s1 = my_str[10]
#
# # define a variable named s2 that stores the character 8 from the string above. Use a negative index the get the character 8
# s2 = my_str[-2]
#
# # concatenate s1 and s2 in a new variable called s3. s3 will store the string 'T8'
# s3 = s1 + s2
# print(s3)
#
#################################
## String Slicing
#################################
# my_str = 'eth0:192.168.122.1'
# # using string slicing, define a variable called my_interface that stores the substring 'eth0'
# my_interface = my_str[0:4]
#
# digits = '0123456789'
# x = digits[::-3]  # x is '9630'
# # digits[::-2] = '97531'
# # digits[::2] = '02468'
#
# my_str = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
#
# ## SOLUTION 1
# mac = my_str[len(my_str) - 17:]
# print(mac)  # => b4:6d:83:77:85:f3
#
# ## SOLUTION 2
# mac = my_str[-1:-18:-1]
# mac = mac[::-1]  # reverse the string
# print(mac)  # => b4:6d:83:77:85:f3
#
# ## SOLUTION 3
# ## Split the string into a list and return the last list element which is the mac
# # my_str.split() = ['wlo1', 'Link', 'encap:Ethernet', 'HWaddr', 'b4:6d:83:77:85:f3']
# mac = my_str.split()[-1]
# print(mac)  # => b4:6d:83:77:85:f3

# # Old string printing
# name = "John Doe"
# email = "johndoe@gmail.com"
# pstring = "Hello, %s." % name + " Your email address is %s." % email
# print(pstring)
# # str.format()  -- Python 2.6+
# pstring = "Hello, {}. Your email address is {}.".format(name, email)
# print(pstring)
# # f string -- Python 3.6+
# pstring = f"Hello, {name}. Your email address is {email}."
# print(pstring)
# profile = (
#     f"Hello, {name}. " f"Your email address is {email}."
# )
# print(profile)
# profile = (
#     f"Hello, {name}. \n"
#     f"Your email address is {email}.\n"
# )
# print(profile, end="...\n")

####################################
## String Indexing, Operations and Slicing
####################################

# ## A string can be treated like a list of characters. Indexing starts from 0
# language = 'Python 3'
# language[0]  # => 'P'
# language[1]  # => 'y'
# language[-1]  # => '3'
# language[-2]  # => ' '
# "This is a string"[0]  # => 'T'
#
# # language[100]          # => IndexError: string index out of range
#
# # Cannot modify a string, it's immutable
# # language[0] = 'J'      # => TypeError: 'str' object does not support item assignment
#
# # You can find the length of a string
# len("This is a string")  # => 16
#
# ## Strings can be concatenated with + and repeated with *
# print('Hello ' + 'world!')  # => 'Hello world!'
# print('Hello ' * 3)  # => 'Hello Hello Hello '
# print('PI:' + str(3.1415))  # => Can concatenate only strings
#
# ## Slicing returns a new string
# ## start index is included, end index is excluded
# movie = 'Star Wars'
# movie[0:4]  # => 'Star' -> from index 0 included to index 4 excluded
# movie[:4]  # => 'Star' -> start index defaults to zero
# movie[2:]  # => 'ar Wars' -> end index defaults to the index of the last char of the string
# movie[::]  # => 'Star Wars'
# movie[2:100]  # => 'ar Wars -> slicing doesn't return error when using index out of range
# movie[1:6:2]  # => 'trW' -> the 3rd index is the step (from index 2 included to 6 excluded in steps of 2)
# movie[6:1:-1]  # => 'aW ra' -> from index 6 included to index 1 excluded in steps of -1 (backwards)
# movie[::-1]  # => 'sraW ratS -> reverses the string
#
# #################################
# ## Formatting Strings
# #################################
# price = 1.33
# quantity = 5
#
# # f-string literals (Python 3.6+) - NEW!
# f'The price is {price}'  # => 'The price is 1.33'
# f'Total value is {price * quantity}'  # => 'Total value is 6.65'
# f'Total value is {price * quantity:.4f}'  # => 'Total value is 6.6500' -> displaying with 4 decimals
#
# # Classical method
# 'The price is {}'.format(price)  # => 'The price is 1.33'
# 'The total value is {}'.format(price * quantity)  # => 'The total value is 6.65'
# 'The total value is {:.4f}'.format(price * quantity)  # => 'The total value is 6.6500' -> displaying with 4 decimals
#
# 'The price is {} and the total value is {}'.format(price,
#                                                    price * quantity)  # => 'The price is 1.33 and the total value is 6.65'
# 'The price is {0} and the total value is {1}'.format(price,
#                                                      price * quantity)  # => 'The price is 1.33 and the total value is 6.65'
# 'The total value is {1} and the price is {0}'.format(price,
#                                                      price * quantity)  # => 'The total value is 6.65 and the price is 1.33'
#
# print('The total value is ', price * quantity)  # => 'The total value is 6.65'

########################
## String Methods
########################

# dirlist = (dir(str))  # => lists all string methods
# for lix in dirlist:
#     print(lix)
# print("#" * 50)
# help(str.find)  # => displays the help of a method
#
# ## All string methods return a new string but don't modify the original string
# my_str = 'I learn Python Programming'
# my_str.upper()  # => 'I LEARN PYTHON PROGRAMMING'
# my_str.lower()  # => 'i learn python programming'
#
# my_ip = '  10.0.0.1 '
# my_ip.strip()  # => '10.0.0.1'
#
# my_ip = '$$$10.0.0.1$$'
# my_ip.strip('$')  # => '10.0.0.1'
# print("my_ip",my_ip)
#
# # Removes all leading whitespace in string
# my_ip.lstrip()  # => '10.0.0.1 '
#
# # Removes all trailing whitespace of string
# my_ip.rstrip()  # => '  10.0.0.1'
#
# my_str = 'I learn Python'
# my_str.replace('Python', 'Go')  # => 'I learn Go'
#
# ## split() returns a list from a string having a delimiter
# my_ip = '10.0.0.1'
# my_list = my_ip.split('.')  # => ['10', '0', '0', '1']
#
# ## join() returns a string from a list
# ':'.join(my_list)  # => '10:0:0:1'
# my_rebuilt_ip = ':'.join(my_list)
# print("my_rebuilt_ip", my_rebuilt_ip)
#
# ## Be default the delimiter is a whitespace
# my_list = my_str.split()  # => my_list = ['I', 'learn', 'Python', 'Programming']
#
# ## in and not in operators test membership
# '10' in my_ip  # => returns True
# '10' not in my_ip  # => returns False
# '20' in my_ip  # => returns False
#
# # Other string methods
# my_str = 'this is a string. this is a string'
#
# ## Returns the first index in my_str where substring 'is' is found or -1 if it didn't find the substring
# my_str.find('is')  # => 2
# my_str.find('si')  # => -1
#
# # Returns a capitalized version of the string.
# my_str.capitalize()  # => 'This is a string. this is a string'
#
# ## Returns True if my_str is an uppercase string, False otherwise
# my_str.isupper()  # => False
#
# ## Returns True if my_str is a lowercase string, False otherwise
# my_str.lower().islower()  # => True
#
# # Returns the number of occurrences of substring 's' in my_str
# my_str.count('s')  # => 6
#
# '0123123'.isdigit()  # => True
# '0123123x'.isdigit()  # => False
# 'abc'.isalpha()  # => True
# '0123123x'.isalnum()  # => True
#
# my_str1 = 'Hi everyone!'
# # Inverts case for all letters in string
# my_str1.swapcase()  # => 'hI EVERYONE!'
#
# language = '$Python$$'
# message = 'I love Python!'
#
# # YOUR CODE GOES HERE:
# language1 = language.strip('$')  # remove all leading and trailing $ signs
# language2 = language1.lower()  # lowercase version of language1 variable
# message1 = message.upper()  # uppercase version of message variable
# message2 = message.replace('Python', 'Java')  # replace Python with Java
