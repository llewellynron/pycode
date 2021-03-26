## Note:  You may want to use IDLE for prototyping new function usage
## Use help(object<.function>) for help
## Use dir(object) for list of methods and attributes
## Use dir() for list of names in local scope
# Style Guide:  https://www.python.org/dev/peps/pep-0008/

#############################
##Types of Variables
#############################
# • Numbers: Integers (ints) or whole numbers and Floating point numbers of simply floats
# • Booleans: Logical values indicating False or True
# • Strings: Ordered sequence of characters
# • Lists: Ordered mutable sequence of objects
# • Tuples: Ordered immutable sequence of objects
# • Sets: Mutable collection of unordered unique objects
# • FrozenSets: Mutable collection of unordered unique objects
# • Dictionaries: Collection unordered key:value pairs

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
# print (0.1 + 0.1 + 0.1)     # 0.30000000000000004
# print (0.1 * 3)             # 0.30000000000000004

#################################
## if ... elif ... else Statements
## Execute a specific block of code if a condition is evaluated to True
#################################

# a, b = 3, 5
# if a < b:  # if a is less that b execute the indented block of code under the if clause, otherwise go and test the elif condition
#     print('a is less than b')
# elif a == b:  # if a is equal to b execute the indented block of code that fallows, otherwise execute the block of code under the else clause
#     print('a is equal to b')
# else:
#     print('a is greater than b')
#
# ## or / and operators
# your_age = 14
# if your_age < 0 or your_age > 99:  # if ANY of the expression is True execute the indented block of code under the if clause
#     print('Invalid age!')
# elif your_age <= 2:
#     print('You are an Infant')
# elif your_age < 18:
#     print('You are a child')
# else:
#     print('You are an adult')
#
# a = 3
# if 1 < a <= 9:
#     print('a is greater than 1 and less than of equal to 9')
#
# # equivalent to
# if a > 1 and a <= 9:
#     print('a is greater than 1 and less than of equal to 9')
#
# a = 12
# ## The fallowing 3 exemples test if a number a is divisible by 6
# ## 1st Example - nested if
# if a % 2 == 0:
#     if a % 3 == 0:
#         print('Example 1: a is divisible by 2 and 3 (or by 6)')
#
# ## 2nd Example: and operator -> it returns True if both expressions are True, False otherwise
# if a % 2 == 0 and a % 3 == 0:
#     print('Example 2: a is divisible by 2 and 3 (or by 6)')
#
# ## 3rd Example
# if not (a % 2 and a % 3):  # the truthniness of an expression: a % 2 is equal to bool(a %2)
#     print('Example 2: a is divisible by 2 and 3 (or by 6)')
#
# ## The truthiness of a variable
# b = 0       # Zero is false; non-Zero is true
# if b:  # it test the truthiness of b or bool(b)
#     print('The truthiness of b: True')
# else:
#     print('The truthiness of b: False')
#
# my_str = 'some string'
# if my_str:  # it test the truthiness of my_str or bool(my_str)
#     print('The truthiness of my_str: True')
# else:
#     print('The truthiness of my_str: False')
#
# my_str = ''     # Same as Zero, so is false
# if my_str:  # it test the truthiness of my_str or bool(my_str)
#     print('The truthiness of my_str \'\': True')
# else:
#     print('The truthiness of my_str \'\': False')
#
# name = 'Andrei'
# ## Pythonic version
# print('Hello Andrei') if name == 'Andrei' else print('You are not Andrei!')
# print('Hello Andrei' if name == 'Ron' else 'You are not Ron!')
#
# # Inline if-else EXPRESSION must always contain else clause
# # See also:  https://stackoverflow.com/questions/11880430/how-to-write-inline-if-statement-for-print
# mytest = "100"
# mytest = 88 if name == 'Andrei' else 99
# print('mytest = ', mytest)
#
# # equivalent to:
# if name == 'Andrei':
#     print('Hello Andrei')
# else:
#     print('You are not Andrei')
#
# ids=["B3","B4","\nB5","\nB6"]
# with open("D:\\Dev\\testing.txt",'w') as file:
#     for item in ids:
#         file.write(item)
# # From Coffee Break
# x = 'silent'
# print(x[2] + x[1] + x[0]
#       + x[5] + x[3] + x[4])
#
# import random
# animals = ['cat', 'mouse', 'fish']
# choice = random.choice(animals)
# print(choice)
# ## YOUR CODE STARTS HERE:
# if choice == 'cat':
#     print('Tom')
# elif choice == 'mouse':
#     print('Jerry')
# else:
#     print('Neo')
#
# animal_names = ['Tom','Jerry','Neo']
# myindx = animals.index(choice)
# print(animal_names[myindx])
#
# myinput = input("Choose one of these: 'cat', 'mouse', 'fish': ")
# if myinput in animals:
#     myindx = animals.index(myinput)
#     print(animal_names[myindx])
# else:
#     print("Invalid selection.")
#
# # starting variables
# my_sum = 0
# my_product = 1
# my_validation_list = []
# for no in range(1, 26):     # Note, 1 - 25 is no processed.  25 + 1 = 26
#     my_sum = my_sum + no  # add each no. in the range to my_sum
#     my_product = my_product * no  # multiply each no. in the range by my_product
#     my_validation_list.append(no)
#
# ## Printing the variables
# print(my_sum)
# print(my_product)
# print(my_validation_list)
# lencount = len(my_validation_list)
# print(my_validation_list[lencount-1])   # Shift -1 since index starts at 0
#
# list1 = list(range(-10,99,3))     # To include 98, have to include one more than desired range as the endpoint
# print(list1)
# list2 = list(range(99,-4,-2))    # To include -3, have to include one more than desired range as the endpoint
# print(list2)

#################################
## For Loops
#################################
#
# movies = ['Star Wars', 'The Godfather', 'Harry Potter ', 'Lord of the Rings']
#
# for m in movies:  # it iterates over a sequence and executes the code indented under the "for" clause for each element in the sequence
#     print(f'One of my favorites movie is {m}')
# else:  # the indented code below "else" will be executed when "for" has finished looping over the entire list (no "break" statement executed)
#     print('This is the end of the list')
#
# for i in range(100):
#     pass  # => empty instruction or "no nothing"
#
# for i in range(10):  # => from 0 (default, included) to 10 excluded
#     print(i, end=' ')
# # it prints out:  0 1 2 3 4 5 6 7 8 9
# print("")       # Will print nothing and go to new line
#
# for i in range(3, 9):  # => from 3 included to 9 excluded
#     print(i, end=' ')
# # it prints out: 3 4 5 6 7 8
# print("\n", end="")
#
# for i in range(3, 20, 3):  # => from 3 included to 20 excluded in steps of 3
#     print(i, end=' ')
# # it prints out: 3 6 9 12 15 18
# print("")       # Will print nothing and go to new line
#
#
# ## for ... continue -> it prints out all letters of the string without 'o'
# for letter in 'Python Go and Java Cobol':
#     if letter == 'o':
#         continue  # go to the beginning of the for loop and do the next iteration
#     print(letter, end='')
# print("")       # Will print nothing and go to new line
#
# ## for ... break
# sequence = [1, 5, 19, 3, 31, 100, 55, 34]
# for item in sequence:
#     if item % 17 == 0:
#         print('A number divisible by 17 has been found! Breaking the loop...')
#         break  # breaks out of the loop (executes the first instruction (if any) after the else block of code)
# else:
#     print('There is no number divisible by 17 in the sequence')
#
# my_str = 'I Love Python!'
# str1 = ''
# for letter in my_str:
#     if letter == 'Y'.lower():
#         break
#     str1 = str1 + letter
#
# ## After running the code above str1 is 'I Love P'
# print(str1)  # => I Love P

#################################
## While Loops
#################################
#
# a = 10
# ## Infinite Loop, it prints out 10 indefinitely
#
# # while a:  #it tests the truthiness of a or bool(a) which is always True
# #    print(a)
#
# ## Prints out numbers from 10 to 1
# while a:  # => "while a:" is equivalent to "while a > 0:"
#     print(a)
#     a -= 1
# else:  # => executes the below block of code after finishing the while looop (and if no "break" statement has been executed)
#     print('Finishing printing numbers. a is now 0')
#
# ## it prints out only odd numbers between 1 and 20
# a = 0
# while a < 20:
#     a += 1
#     if a % 2 == 0:
#         continue  # go the the beginning of the while loop
#     print(f'Odd number {a}')  # it reaches this line only if the continue statement hasn't been executed
#
# ## it prints out numbers greater than 2
# a = 7  #################################
# ## While Loops
# #################################
#
# a = 10
# ## Infinite Loop, it prints out 10 indefinitely
#
# # while a:  #it tests the truthiness of a or bool(a) which is always True
# #    print(a)
#
# ## Prints out numbers from 10 to 1
# while a:  # => "while a:" is equivalent to "while a > 0:"
#     print(a)
#     a -= 1
# else:  # => executes the below block of code after finishing the while looop (and if no "break" statement has been executed)
#     print('Finishing printing numbers. a is now 0')
#
# ## it prints out only odd numbers between 1 and 20
# a = 0
# while a < 20:
#     a += 1
#     if a % 2 == 0:
#         continue  # go the the beginning of the while loop
#     print(f'Odd number {a}')  # it reaches this line only if the continue statement hasn't been executed
#
# ## it prints out numbers greater than 2
# a = 7
# while a > 0:
#     a -= 1
#     if a == 2:
#         break  # => it breaks out of the while loop and executes the next instruction after the while block of code
#     print(a)
#
# print('Loop ended.')
# while a > 0:
#     a -= 1
#     if a == 2:
#         break  # => it breaks out of the while loop and executes the next instruction after the while block of code
#     print(a)
#
# print('Loop ended.')
#
# ## Solution 1
# my_sum = 0
# x = 100
# while x:
#     if x % 2 != 0:
#         my_sum += x
#     x -= 1
# else:
#     print(my_sum)
#     print("I'm done..")
#
# #######################
#
# ## Solution 2
# my_sum = 0
# x = 100
#
# while x:
#     x -= 1
#     if x % 2 == 0:
#         continue
#     my_sum += x
#
# print(my_sum)
# #######################
#################################
## Python Collections:
#################################
# List = [ ] ordered and changeable; allows duplicate members
# tuple = ( ) ordered and unchangeable; allows duplicate members
# set  = { } unordered and unindexed; No duplicate members
# dictionary = { } unordered and changeable; No duplicate members

tuple1 = ('disco',1,2.3)
print(tuple1[1])
list1 = ['disco',1,2.3]
print(list1[1])
set1 = {'disco',1,2.3}
#print(set1[1])                         # Not allowed, not indexed
print(set1)                             # => {1, 2.3, 'disco'}
for i in set1:                          # Is iterable
    print(i)
dict1 = {'disco':1,"1":1,"key3":2.3}
print(dict1['disco'])
exit()

#################################
## Intro to Lists
## A list is an ordered sequence of objects of different types
#################################
#
# ## Creating lists
# list1 = []  # empty list
# list2 = list()  # empty list
# list3 = list('Python')  # => ['P', 'y', 't', 'h', 'o', 'n'] -> creates a list from a string
# list4 = ['Python', 'Go', 2018, 4.5, [1, 2.3, 'abc']]  # a list stores any type of object
#
# ## Lists are indexed like strings
# list4[0]  # => 'Python'
# list4[-1]  # => [1, 2.3, 'abc']
# list4[4][1]  # => 2.3
# # list4[10]  # Raises an IndexError (out of bounds index)
#
# ## A list is a mutable object, it can be modified
# list4[0] = 'Rust'  # =>['Rust', 'Go', 2018, 4.5, [1, 2.3, 'abc']]
#
# ## Lists are sliced like strings. Slicing returns a new list
# ## The start is included and the stop is excluded
# numbers = [1, 2, 3, 4, 5]
# numbers[1:4]  # => [2, 3, 4]
# numbers[1:40]  # => [2, 3, 4, 5]   -> out of bound slicing doesn't return error
# numbers[:3]  # => [1, 2, 3]  -> by default start is zero
# numbers[2:]  # => [3, 4, 5]  -> by default stop is the end of the list
# numbers[::]  # => [1, 2, 3, 4, 5]    -> returns the entire list
# numbers[1:5:3]  # => [2, 5]     -> from 2 included to 5 excluded in steps of 3
# numbers[4:1:-2]  # => [5, 3]
# numbers[0:2] = ['a', 'b']  # => ['a', 'b', 3, 4, 5]    -> slicing modifies a list
# print(numbers)
# numbers[0:2] = ['x', 'y', 'z']  # => ['x', 'y', 'z', 3, 4, 5]   -> no error
# print(numbers)
# numbers[0:2] = ['was_xy']        # => ['was_xy', 'z', 3, 4, 5]
# print(numbers)
#
# l1 = [1, 2, 3]
# l2 = l1  # l1 and l2 reference the same object, l2 is not a copy of l1
# l1 is l2  # => True
# l1 == l2  # => True
# l1.append(4)  # here I've modified both l1 and l2, they are still the same list
# l1 is l2  # => True
# l1 == l2  # => True
#
# l3 = l1.copy()  # l2 is a copy of l1, they don't reference the same object
# l1 == l2  # => True
# l1 is l2  # => False
# l3.remove(1)
# l1 == l3  # => False
# l1 is l3  # => False
#
# l1 = [1, 2]
# id(l1)  # => 139875652516360 (you get another value here)
# l1 += [3, 4]  # => [1, 2, 3, 4]  -> concatenating a new list to l1 - equivalent to using the extend method()
# id(l1)  # => 139875652516360  -> it's the same list
#
# l1 = [1, 2]
# l1.extend([3, 4])  # => [1, 2, 3, 4]  -> concatenating a new list to l1 - equivalent to using +=
# print(l1)
#
# l1 = l1 + [5, 6]  # => [1, 2, 3, 4, 5, 6] -> concatenating a new list to l1
# id(l1)  # => 139875654318792    -> l1 is a new list
#
# ## Iterating over a list
# ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
# for ip in ip_list:
#     print(f'Connecting to {ip} ...')
#
# ## in and not in operators test list membership
# print('10.0.0.1' in ip_list)  # => returns True
# print('192' not in ip_list)  # => returns True
# print('192' in ip_list)  # => returns False
# print('192' in ip_list[0])  # => returns True
#
# # list with 4 elements: a float, an integer, a string and another list
# my_list1 = [2.3, 5, 'Python', ['a', 2]]
#
# # the 2nd element of my_list
# print(my_list1[1])  # 5
#
# # the second element of the list which is the 4th element of my_list
# print(my_list1[3][1])  # 2
#
# # list slicing that returns a new list with the first 2 elements of my_list
# print(my_list1[0:2])   # [2.3, 5]

#################################
## List Methods
#################################
#
# dir(list)  # returns a list will all list methods
#
# list1 = [1, 2.2, 'abc']
# len(list1)  # => 3
#
# ## Adds a single element to the end of the list
# list1.append(5)  # => [1, 2.2, 'abc', 5]
# # list1.append(6, 7)    # TypeError: append() takes exactly one argument (2 given)
# list1.append([6, 7])  # => [1, 2.2, 'abc', 5, [6, 7]]
#
# ## Extends the list with elements of an iterable object
# # list1.extend(5.2)          # TypeError: 'float' object is not iterable
# list1.extend([5.2])  # => [1, 2.2, 'abc', 5, [6, 7], 5.2]
# list1.extend(['x', 'y'])  # => [1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']
#
# ## Inserts an item at a given index
# list1.insert(2, 'T')  # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y']
# # Inserts on the last position
# list1.insert(len(list1), 'Q')  # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y', 'Q']
#
# ## Removes and returns an element of the list
# print(list1)  # => [1, 2.2, 'T', 'abc', 5, [6, 7], 5.2, 'x', 'y', 'Q']
# list1.pop()  # => 'Q'
# list1.pop(2)  # => 'T'
# print(list1)  # => [1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']
# # list1.pop(50)    # IndexError: pop index out of range
#
#
# ## Removes and doesn't return an item of the list
# print(list1)  # [1, 2.2, 'abc', 5, [6, 7], 5.2, 'x', 'y']
# list1.remove('abc')  # => [1, 2.2, 5, [6, 7], 5.2, 'x', 'y']
# # list1.remove('a')  # ValueError: list.remove(x): x not in list
# print(list1)
# my_pop0 = list1.pop(0)  # => '1'
# print(my_pop0)
#
# ## Returns the index of an item
# letters = list('abcabcabc')
# letters.index('b')  # => 1
# letters.index('b', 3)  # => 4 -> it starts from index 3
# letters.index('b', 3, 6)  # => 4 -> it searches from index 3 to index 6
# letters.index('x')  # => returns error, should check if in list first
#
# ## Returns the no. of occurrences of an item in a list
# letters.count('a')  # => 3
#
# nums = [6, -1, 55, 2.3]
# sorted(nums)  # => [-1, 2.3, 6, 55] -> returns a new sorted list
#
# print(nums)  # => [6, -1, 55, 2.3]
# nums.sort()  # sorts the list in-place
# print(nums)  # => [-1, 2.3, 6, 55]
# max(nums)  # => 55
# min(nums)  # => -1
# sum(nums)  # => 62.3
#
# ## These methods return an error if the list is not sortable
# nums.append('5.5')
# # nums.sort()    TypeError: '<' not supported between instances of 'str' and 'int'
# # nums.max()     AttributeError: 'list' object has no attribute 'max'
#
#
# ## Converts a list into a string and a string into a list
# ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
# ## join() returns a string from a list
# ip_str = ':'.join(ip_list)  # => ip_str is equal to '192.168.0.1:192.168.0.2:10.0.0.1'
#
# ## split() returns a list from a string
# ip_list = ip_str.split(':')  # => ip_list is equal to ['192.168.0.1', '192.168.0.2', '10.0.0.1']
#
# names_list = ['Alice', 'Bob', 'Eve']
# ## Converting list to string
# names_str = ','.join(names_list)    #  Alice,Bob,Eve
# print(names_str)
# names_str = ''.join(names_list)     # AliceBobEve
# print(names_str)
#
# url = 'www.python.org'
# ## Converting string to list
# url_list = url.split('.')           # ['www', 'python', 'org']
# print(url_list)
#
# animals = ['Cat', 'Dog']
#
# ## Add an element at the end of the list. The new element stores the string 'Donkey'
# ## animals will be ['Cat', 'Dog', 'Donkey']
# animals.append('Donkey')
#
# ## Add an element at position 2. This will be the 2nd element and will store the string 'Horse'
# ## animals will be ['Cat', 'Horse', 'Dog', 'Donkey']
# animals.insert(1, 'Horse')
#
# ## Return the index of the element with value 'Cat'  => 0
# cat_index = animals.index('Cat')
#
# ## Make a string variable named str_animals from the list by joining the elements of the list using '-' as a delimiter
# ## str_animals will be 'Cat-Horse-Dog-Donkey'
# str_animals = '-'.join(animals)

#################################
## List Comprehension
## list = [expression for item in itarable if condition]
#################################
# s = [x for x in range(10)]
# print(s)  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# evens = [x for x in s if x % 2 == 0]
# print(evens)  # => [0, 2, 4, 6, 8]
#
# word_list = 'I learn Python programming!'.split()
# info = [[w.upper(), w.lower(), len(w)] for w in word_list]
# print(info)  # => [['I', 'i', 1], ['LEARN', 'learn', 5], ['PYTHON', 'python', 6], ['PROGRAMMING!', 'programming!', 12]]
#
# ## Celsius to Fahrenheit
# celsius = [7.12, 10.1, 14.15, 22.5, 29.4, 32.9]
# fahrenheit = [1.8 * x + 32 for x in celsius]
# print(fahrenheit)  # => [44.816, 50.18, 57.47, 72.5, 84.92, 91.22]
#
# miles = [12, 10, 26, 80]
# ## 1 mile = 1.609 km
# km = [m * 1.609 for m in miles]
# print(km)   # => [19.308, 16.09, 41.834, 128.72]

#################################
## Python Tuples
## A tuple is a immutable ordered sequence of objects of different types
#################################
#
#
# ## Creating tuples
# t0 = ()  # empty tuple
# t1 = tuple()  # empty tuple
# t = (1.2)  # this isn't a tuple!
# type(t)  # => float
# t2 = (1.2,)  # a tuple with a single element
# t3 = tuple('abc')  # creating a tuple from a iterable (string)
# t4 = tuple([1, 3.2, 'abc'])  # creating a tuple from a iterable (list)
# t5 = (1, 3.2, 'abc')
#
# ## Tuples are indexed like strings and lists
# t5[0]  # => 1
# t5[2]  # => 'abc'
# t5[-1]  # => 'abc'
# # t5[10]     # => IndexError: tuple index out of range
#
# ## A tuple is an immutable object. Can't be changed.
# # t5[0] = 4   # => TypeError: 'tuple' object does not support item assignment
#
#
# ## Tuple are sliced like strings and lists.
# ## The start is included and the stop is excluded
# print(t5)  # => (1, 3.2, 'abc')
# t5[0:2]  # => (1, 3.2)
# t5[:2]  # => (1, 3.2)
# t5[::]  # => (1, 3.2, 'abc')
# t5[::2]  # => (1, 'abc') -> in steps of 2
# t5[-1:0:-1]  # => ('abc', 3.2)
#
# ## Iterating over a tuple
# movies = ('The Wizard of Oz', 'The Legend', 'Casablanca')
# for movie in movies:
#     print(f'We are watching {movie}')
#
# ## in and not in operators test tuple membership
# 'The Legend' in movies  # => True
# 'The Legend' not in movies  # => False

#################################
## Tuple Methods
#################################
#
# dir(tuple)  # returns a list will all tuple methods
#
# my_tuple = (1, 2.2, 'abc', 1)
# len(my_tuple)  # => 4
#
# ## Returns the index of an item
# my_tuple.index(1)  # => 0 -> the index of the first element with value 1
# my_tuple.index(10)  # => ValueError: tuple.index(x): x not in tuple
#
# ## Returns the no. of occurrences of the item in tuple
# my_tuple.count(1)  # => 2
#
# nums = (6, -1, 55, 2.3)
# sorted(nums)  # => (-1, 2.3, 6, 55) -> returns a new sorted tuple
# max(nums)  # => 55
# min(nums)  # => -1
# sum(nums)  # => 62.3
#
# languages = ('Python', 'Java', 'Go', 'C++', 'PHP', 'Scala', 'Solidity')
#
# ## Extracting the last element of the tuple
# x = languages[-1]
#
# ## Returning a new tuple called y using slicing and a step of 5
# ##  y will be ('Python', 'Scala')
# y = languages[::5]
#
# ##1. Create a list called nums_list with the values: 'a', 3, 5.5, 'a', 4 inside
# nums_list = ['a', 3, 5.5, 'a', 4]
#
# ##2. Create a tuple called nums_tuple from the nums_list using the tuple() constructor
# nums_tuple = tuple(nums_list)
#
# ##3. Create a set called nums_set from the nums_list using the set() constructor. Print the set
# nums_set = set(nums_list)
# print(nums_set)     # => {4, 3, 'a', 5.5}
# # print(sorted(nums_set))     # => Errors, not supported between instances of 'int' and 'str'
#
# ##4. Given the following list, create a new list called unique_ip that contains only unique values in the ip list
# ## Print the unique_ip list
# ip = ['10.0.0.1', '10.0.0.2', '10.0.0.1', '10.0.0.3', '10.0.0.1', '10.0.0.2']
# unique_ip = list(set(ip))
# print(unique_ip)

#################################
## Sets in Python
## A set is a unordered sequence of immutable unique objects.
#################################
#
# ## Creating sets
# set1 = set()  # empty set
# # x = {}             # x is a dictionary, not a set
# set2 = {'a', 1, 2, 1, 'a', 2.3, 'a'}  # => {1, 2, 2.3, 'a'} -> unique unordered collection
# set3 = set('hellooo python')  # =>{'n', 'e', 'p', 't', 'o', 'h', 'l', ' ', 'y'}
# set4 = set([1, 2.3, 1, 'a', 'a', 2.3, 'b', 5])  # => {1, 2.3, 5, 'a', 'b'}
# # set4[0]    # TypeError: 'set' object does not support indexing
# set5 = {(1, 2), 'a'}  # a set can contain immutable objects like tuples
# # set6 = {[1, 2], 'a'}    # TypeError: unhashable type: 'list' -> list is mutable, not allowed in set
#
#
# ## Iterating over a set
# some_letters = set('abcabc')
# for letter in some_letters:  # prints: c a b
#     print(letter, end=' ')
#
# ## in and not in operators test list membership
# 'a' in some_letters  # => True
# 'aa' in some_letters  # => False
# 'bb' not in some_letters  # => True
#
# s1 = {1, 2, 3}
# s2 = {3, 1, 2}
# s1 == s2  # => True
# s1 is s2  # => False
#
# ## The assignment operator (=) create a reference to the same object
# s3 = s1
# s3 is s1  # => True
# s3 == s1  # => True
# s3.add('x')  # adds to the set
# print(s1)  # => {1, 2, 3, 'x'}
# s3 == s1  # => True
# s3 is s1  # => True
#
# # copy() method creates a copy of a set (not a reference to the same object)
# s4 = s1.copy()
# s4 is s1  # => False
# s4 == s1  # => True
# s4.add('z')
# s4 == s1  # => False
#
# print(s1)  # => {1, 2, 3, 'x'}
# ## pop() method removes and returns an arbitrary set element
# item = s1.pop()
# print(f'item:{item}, s1:{s1}')  # => item:1, s1:{2, 3, 'x'}
#
# s1.discard(2)  # discards element from the set, s1 is {3, 'x'}
# s1.discard(22)  # no error if the element doesn't exist
# # s1.remove(1)   # KeyError if element doesn't exist
# s1.clear()  # Removes all elements from this set
#
# set1 = {'a', 'b', 'c'}
# set2 = {'c', 'd', 'e'}
#
# ## union() or | returns the set of all unique elements present in all the sets.
# # set3 = set1 | set2
# set3 = set1.union(set2)
#
# ## intersection() or &  returns the set that contains the elements that exist in both sets
# # set4 = set1 & set2
# set4 = set1.intersection(set2)
#
# ## difference() or - returns the set of elements that  exist only in set1, but not in set2.
# # set5 = set1 - set2
# set5 = set1.difference(set2)
#
# ## Removing 'c' from set1
# set1.discard('c')

#################################
## Set Operations and Frozensets
#################################
#
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# ## difference() returns the set of elements that  exist only in set1, but not in set2.
# set1.difference(set2)  # => {1, 2}
# set1 - set2  # => {1, 2}
#
# ## symetric_difference() returns the set of elements which are in either of the sets but not in both.
# set1.symmetric_difference(set2)  # => {1, 2, 4, 5}
# set1 ^ set2  # => {1, 2, 4, 5}
#
# ## union() returns the set of all unique elements present in all the sets.
# set1.union(set2)  # => {1, 2, 3, 4, 5}
# set1 | set2  # => {1, 2, 3, 4, 5}
#
# ## intersection() returns the set that contains the elements that exist in both sets
# set1.intersection(set2)  # => {3}
# set1 & set2  # => {3}
#
# set1.isdisjoint(set2)  # => False
# set1.issubset(set2)  # => False
# set1 > set2  # => False
# set1 <= set2  # => False
#
# ## A frozenset is an immutable set
# fs1 = frozenset(set1)
# print(fs1)  # => frozenset({1, 2, 3})
#
# ## All set methods that don't modify the set are available to frozensets
# fs1 & set2  # => frozenset({3})

#################################
## Dictionaries in Python
## A dictionary is an unordered collection of key: value pairs
#################################
#
# dict1 = {}  # empty dictionary
# dict2 = dict()  # empty dictionary
#
# ## Keys for dictionaries have to be immutable types. This is to ensure that
# ## the key can be converted to a constant hash value for quick look-ups.
# # invalid_dict = {[1,2,3]: "123"}  # => Raises a TypeError: unhashable type: 'list'
# # a key of type tuple is permitted (immutable). Values can be of any type, however.
# valid_dict = {(1, 2, 3): [1, 2, 3], 3: 'abc', 'abc': {14, 'a'}, 4.5: True}
#
# product = {'id': 1234, 'name': 'Laptop'}
# product['seller'] = 'Amazon'  # adds a new key:value pair
# product.update({'price': 888.99})  # another way to add to a dictionary
#
# p = product['price']  # getting the value of a key,  p is 888.00
#
# del product['seller']  # removing a key:value pair
# print(product)  # => {'id': 1234, 'name': 'Laptop', 'price': 888.99}
# # seller = product['seller']  # Looking up a non-existing key is a KeyError
#
# # Use get() method to retrieve the value of a key
# product.get("id")  # => 1234
# product.get("review")  # => None -> it doesn't return KeyError
# # The get method supports a default argument when the value is missing
# product.get("id", 4)  # => 1234
# product.get("review", 'N/A')  # => 'N/A'
#
# ## pop() removes specified key and return the corresponding value.
# ## If key is not found, a default value is given, otherwise KeyError is raised
# name = product.pop('name')  # name is 'Laptop'
# print(product)  # => {'id': 1234, 'price': 888.99}
#
# # name = product.pop('name')                 # => KeyError: 'name', key 'name' doesn't exist anymore
# name = product.pop('name', 'No such key')  # => name is 'No such key'
#
# user = {'name': 'Andrei', 'age': 35, 'location': 'Bucharest', 'email': 'just_an_email@domain.com'}
#
# song = {
#     'artist': 'John Lennon',
#     'name': 'Imagine'
# }
#
# song['year'] = 1971
# song['artist'] = 'John Winston Ono Lennon'
# print(song)     # => {'artist': 'John Winston Ono Lennon', 'name': 'Imagine', 'year': 1971}

#################################
## Dictionary Operations and Methods
#################################
#
# product = {'id': 1234, 'price': 888.99}
#
# ## in and not in operators test dictionary key membership
# 'price' in product  # => True
# 5 in product  # => False
#
# ## Dictionary views
# keys = product.keys()  # getting all keys as an iterable
# keys = list(keys)  # it can be converted to a list
# print(keys)  # => ['id', 'price']
#
# values = product.values()  # getting all values as an iterable
# values = list(values)  # it can be converted to a list
# print(values)  # => [1234, 888.99]
#
# key_values = product.items()  # getting all key:value pairs as tuples
# key_values = list(key_values)  # it can be converted to a list of tuples
# print(key_values)  # => [('id', 1234), ('price', 888.99)]
#
# ## Iterating over a dictionary
#
# ## Iterating over the keys
# for k in product:
#     print(f'key:{k}')
# # equivalent to:
# for k in product.keys():
#     print(f'key:{k}')
#
# ## Iterating over the values
# for v in product.values():
#     print(f'value:{v}')
#
# # Iterating over both the keys and the values
# for k, v in product.items():
#     print(f'key:{k}, value:{v}')
#
# ## Creates a copy of a dictionary
# prod = product.copy()
# ## Returns the no. of key:value pairs in the dictionary
# len(prod)
# # Removes all items from dictionary
# product.clear()
#
# money = {
#     'bank': 8564.61,
#     'paypal': 1998.21,
#     'cash': 480,
#     'payoneer': 250.5
# }
#
# ## First solution using a for loop
# total_amount = 0
# for value in money.values():
#     total_amount += value
#
# print(total_amount)
#
# ## Second solution using sum() function and dictionary.values() method
# total_amount = sum(money.values())
# print(total_amount)

#################################
## Set Comprehension
## set = {expression for item in itarable if condition}
#################################
#
# set1 = {item for item in [1, 2, 1, 2, 1, 2, 3, 4, 3]}
# print(set1)  # => {1, 2, 3, 4}
#
# set2 = {item ** 2 for item in set1 if item % 2 == 0}
# print(set2)  # => {16, 4}
#
# ## Lists with duplicates
# cities = ['Paris', 'NYC', 'BERLIN', 'Liverpool', 'Osaka', 'Barcelona']
# capitals = ['Paris', 'BERLIN', 'Madrid', 'Paris', 'BERLIN']
#
# ## Set comprehension returning a set only with capitalized cities in both lists.
# capitals_unique = {word.capitalize() for word in set(cities) & set(capitals)}
# print(capitals_unique)  # => {'Paris', 'Berlin'}
#
# #################################
# ## zip() built-in function
# ## Returns an iterator of tuples, where the i-th tuple contains the i-th element
# ## from each of the argument sequences or iterables.
# ## The iterator stops when the shortest input iterable is exhausted.
# #################################
#
# years = [2015, 2016, 2017, 2018]
# sales = [20000, 30000, 40000, 45000]
#
# ## Zipping in a list of tuples
# sales_list = list(zip(years, sales))
# print(sales_list)  # => [(2015, 20000), (2016, 30000), (2017, 40000), (2018, 45000)]
#
# ## Zipping in a dictionary
# sales_dict = dict(zip(years, sales))
# print(sales_dict)  # => {2015: 20000, 2016: 30000, 2017: 40000, 2018: 45000}
#
# #################################
# ## Dictionary Comprehension
# #################################
# d1 = {'a': 1, 'b': 2, 'c': 3}
#
# ## Double values
# d2 = {k: v * 2 for k, v in d1.items()}
# print(d2)  # => {'a': 2, 'b': 4, 'c': 6}
#
# ## Double keys, squared values
# d3 = {k * 2: v * 3 for k, v in d1.items()}
# print(d3)  # => {'aa': 3, 'bb': 6, 'cc': 9}
#
# sales = {2015: 20000, 2016: 30000, 2017: 40000, 2018: 45000}
#
# ## Creating a dictionary called vat if value added tax is 20%
# vat = {k: v * 0.2 for k, v in sales.items()}
# print(vat)  # => {2015: 4000.0, 2016: 6000.0, 2017: 8000.0, 2018: 9000.0}
#
# visits = {'Monday': 5000,
#           'Tuesday': 3000,
#           'Wednesday': 4000,
#           'Thursday': 4500,
#           'Friday': 5000,
#           'Saturday': 2000,
#           'Sunday': 1500
#           }
#
# total_visits = sum(visits.values())
# print(total_visits)  # => 25000
#
# percentage = {k: (v / total_visits) * 100 for k, v in visits.items()}
# print(percentage)
# # {'Monday': 20.0, 'Tuesday': 12.0, 'Wednesday': 16.0,
# # 'Thursday': 18.0, 'Friday': 20.0, 'Saturday': 8.0, 'Sunday': 6.0}

# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number
# less than the asked number.

# #################################
# ## Concepts Review
# #################################

# ## Challenge #1
# # Create a Python script that asks the user for a number and then prints out a list
# # of all the divisors of each number less than the asked number.
# # ---- Solution: ----
# x = int(input("Enter a number: "))
# all_divisors = list()
# for i in range(2, x//2+1):
#     if x % i == 0:
#         all_divisors.append(i)
#
# print(all_divisors)
#
# ## Challenge #2
# Consider the following string: nums = '10,20,30,40,50'
# Create a Python script that creates a list of integers from the string.
# The resulting list will be: [10, 20, 30, 40, 50]
# # ---- Solution 1: ----
# nums = '10,20,30,40,50'
# num_split = nums.split(',')
# print(num_split)
# num_list = list()
# for item in num_split:
#     num_list.append(int(item))
# print(num_list)     # => [10, 20, 30, 40, 50]

# # ---- Solution 2: ----
# nums = '10,20,30,40,50'
# nums_list = nums.split(',')
# print(nums_list)  # => ['10', '20', '30', '40', '50']
# nums1 = [int(n) for n in nums_list]
# print(nums1)    # => [10, 20, 30, 40, 50]

# ## Challenge #3
# Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5,
# between 1500 and 3200 (both included). The numbers obtained should be printed in a comma-separated
# sequence (CSV) on a single line.
# # ---- Solution: ----
# result_list=list()
# for i in range(1500,3201):
#     if (i % 7 == 0) & (i % 5 == 0):
#         result_list.append(str(i))
# print(result_list)
# print(len(result_list))
# print(','.join(result_list))
# # ---- Solution: ----
# result_list=list()
# for i in range(1500,3201):
#     if (i % 7 == 0) & (i % 5 == 0):
#         result_list.append(i)   # If stored as numbers in list, then later have to convert to str in order to join ","
# print(result_list)
# result_str = [str(x) for x in result_list]
# print(len(result_str))
# print(','.join(result_str))

# ## Challenge #4
# Write a program that asks the user for a long string containing multiple words separated by whitespaces.
# Make it to print back the same string with the words in backward order.
# For example, say I type the string: My name is Andrei
# Then the script should print out: Andrei is name My
# # ---- Solution 1: ----
# str_input = input("Enter a multiple word string: ")   # input: My name is Andrei
# word_list = str_input.split(" ")
# rev_list = word_list[::-1]
# print(rev_list)
# # ---- Solution 2: ----
# words = input('Enter some words: ')       # input: My name is Andrei
# words_list =  words.split(' ')
# # print(words_list)
# words_reversed = ' '.join(reversed(words_list))
# print(words_reversed)

# Challenge #5
# Write a Python program that accepts a hyphen-separated sequence of words as input and
# prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample input string : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
# # ---- Solution: ----
# words = input('Enter some words separated by hyphens: ')
# words_list = words.split('-')
# words_list.sort()
# words_result = '-'.join(words_list)
# print(words_result)

# ## Challenge #6
# Write a Python program that accepts as input a sequence of words separated by one or more
# whitespaces and prints out the same words with the letters in reversed order. Do not use list comprehension.
# Sample input string: I love cat and dogs
# Expected Result : I evol tac dna sgod
# # ---- Solution 1: ----
# words = input('Enter some words: ')       # input: I love cat and dogs
# words_list =  words.split(' ')
# words_reversed = list()
# for item in words_list:
#     words_reversed.append(item[::-1])
# print(' '.join(words_reversed))
# # ---- Solution 2: ----
# string = input("Enter a few words separated by whitespaces: ")
# words = string.split()
# # reverse the letters in each word
# i = 0
# for w in words:
#     words[i] = w[::-1]
#     i += 1
# new_str = ' '.join(words)
# print(new_str)

# ## Challenge #7
# Create an alternative solution for the previous challenge that uses list comprehension.
# # ---- Solution: ----
# string = input("Enter a few words separated by whitespaces: ") # input: I love cat and dogs
# words = string.split()
# # reverse the letters in each word
# i = 0
# words_reversed = [w[::-1] for w in words]
# new_str = ' '.join(words_reversed)
# print(new_str)

# ## Challenge #8
# Consider a list of words(strings). Write a Python script that generates a list of tuples where
# the first element of the tuple is the word in the list and the second element is its length.
# Use list comprehension if possible.
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# Expected Result: [('Python', 6), ('Java', 4), ('C++', 3), ('Golang', 6), ('Solidity', 8), ('Bash', 4)]
# # ---- Solution 1: ----
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# my_list = list()
# for item in words:
#     my_list.append((item,len(item)))
# print(my_list)
#
# # # ---- Solution 2: ----
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# words_and_length = [(w, len(w)) for w in words]
# print(words_and_length)

# ## Challenge #9
# Consider a list of words(strings). Write a Python script that generates a dictionary where the
# key is the word in the list and the value is its length.
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}
# # ---- Solution: ----
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# words_and_length = dict()
# for w in words:
#     words_and_length[w] = len(w)
# print(words_and_length)

# ## Challenge #10
# Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].
# Create a Set that contains the elements of the 2 lists in pairs.
# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}
# # ---- Solution: ----
# names = ["Dan", "John", "Diana"]
# phones = [11111, 2222, 3333]
# print(list(zip(names, phones)))   # [('Dan', 11111), ('John', 2222), ('Diana', 3333)]
# print(tuple(zip(names, phones)))  # (('Dan', 11111), ('John', 2222), ('Diana', 3333))
# print(dict(zip(names, phones)))   # {'Dan': 11111, 'John': 2222, 'Diana': 3333}
# names_and_phones = set(zip(names, phones))
# print(names_and_phones)           # {('Diana', 3333), ('John', 2222), ('Dan', 11111)}

# ## Challenge #11
# Consider the two Python lists. Write a Python Script to make a new list whose elements
# are the intersection of the two given lists. This means all elements of L1 that also
# belong to L2, but no other elements.
# # ---- Solution: ----
# L1 = [1, 2, 5, 10, 11, -10, 9, 88]
# L2 = [88, 5, 10, 6, 7]
# L3 = list(set(L1).intersection(set(L2)))
# print(L3)

# ## Challenge #1  (from L110)
# Considering the following dict, get a dict representation sorted by key.
# A dict representation means viewing or printing the dict.
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# print(d1.keys())
# for k in sorted(d1.keys()):
#     print(f'{k} -> {d1[k]}')

# ## Challenge #2
# Considering the following dict, get a dict representation sorted by value.
# A dict representation means viewing or printing the dict.
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# view = sorted(d1.items(), key = lambda x: x[1])
# print(view)

# ## Challenge #3
# Let's generalize the last challenge and sort a dictionary by any field of its values if the value ' \
#    'is a composite type (list, tuple, etc).
# Example: Consider the dictionary in the image below and print a sorted view of the dictionary by
# the second field of its values.
# The output should be: [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]
# P.S. Do it with a single line of code. 🙂
# employees = {'John': ('London', 4000, 28), 'Maria':('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# view = sorted(employees.items(), key=lambda x: x[1][1])
# print(view)  # => [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]

# ## Challenge #4
# Consider the dictionary in the image below and print a sorted view of the dictionary by the third field
# of its values in reverse order.
# The output should be: [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]
# P.S. Do it with a single line of code. 🙂
# employees = {'John': ('London', 4000, 28), 'Maria':('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# view = sorted(employees.items(), key=lambda x: x[1][2], reverse=True)
# print(view)  # [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]

# ## Challenge #5
# Consider the dictionary called COUNTRY declared in this Python script.
# The keys are the country codes and the values are the countries’ names.
# Print a sorted view of the dictionary by the key (country code).
# COUNTRY = {
# "MX":"MEXICO",
# "US":"UNITED STATES",
# "HN":"HONDURAS",
# "NG":"NIGERIA",
# "JM":"JAMAICA"
# }
# keys = sorted(COUNTRY.keys())
# # print(keys)
# for k in keys:
#     print(f'{k} --> {COUNTRY[k]}')

# ## Challenge #6
# Consider the dictionary called COUNTRY declared in this Python script.
# Find the country which has the longest name.
# Use list comprehension if possible.
# list with the lengths of each countries
# COUNTRY = {
# "MX":"MEXICO",
# "US":"UNITED STATES",
# "HN":"HONDURAS",
# "NG":"NIGERIA",
# "JM":"JAMAICA"
# }
# lengths = [len(value) for value in COUNTRY.values()]
# m = max(lengths)  # the longest country name
# cc = [c for c in COUNTRY.values() if len(c) == m]
# print(cc)   # -> ['UNITED STATES']

# ## Challenge #7
# Consider the following two Python Lists that save information about company sales for the last 6 years:
# years = [2015, 2016, 2017, 2018, 2019, 2020]
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# Create a new list that connects the year to the corresponding sales.
# The resulting list should be: [(2015, 350000), (2016, 400000), (2017, 410000), (2018, 439000),
#                                (2019, 500000), (2020, 290000)]
# years = [2015, 2016, 2017, 2018, 2019, 2020]
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# company_sales = list(zip(years,sales))
# print(company_sales)

# ## Challenge #8
# Consider the following two Python Lists that save information about company sales for the last 6 years:
# years = [2015, 2016, 2017, 2018, 2019, 2020]
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# Create a new dictionary that has the keys, the years, and the values, the sales.
# The resulting dict should be: {2015: 350000, 2016: 400000, 2017: 410000, 2018: 439000, 2019: 500000, 2020: 290000}
# years = [2015, 2016, 2017, 2018, 2019, 2020]
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# company_sales = dict(zip(years,sales))
# print(company_sales)

# ## Challenge #9
# Consider the dictionary from the previous challenge.
# Create a new dictionary called profit that stores the profit of the company if the profit margin is 25%
# Use dictionary comprehension if possible.
# years = [2015, 2016, 2017, 2018, 2019, 2020]
# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# company_sales = dict(zip(years,sales))
# # profit margin is 25%
# profit = {k: v*0.25 for k, v in company_sales.items()}
# print(profit)

# ## Challenge #10
# Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user
# to input both integers.
# Input: 16, 2
# Output: 4 ** 2 = 16
# x = int(input("Enter a number x: "))
# y = int(input(f"Enter a number y to test if x which is {x} is a power of y: "))
# found = False
# for k in range(2, (x//2)+1):
#     if y ** k == x:
#         print(f"{y} ** {k} = {x}")
#         found = True
#         break
# else:
#     print(f'{x} is not the power of {y}')

