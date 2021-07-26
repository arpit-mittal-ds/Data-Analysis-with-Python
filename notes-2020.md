Data Structures:

Mutability and Order
Mutability is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (like a list can), then it is called mutable. However, if an object cannot be changed with creating a completely new object (like strings), then the object is considered immutable.

>>> my_lst = [1, 2, 3, 4, 5]
>>> my_lst[0] = 'one'
>>> print(my_lst)
['one', 2, 3, 4, 5]
As shown above, you are able to replace 1 with 'one' in the above list. This is because lists are mutable.

However, the following does not work:

>>> greeting = "Hello there"
>>> greeting[0] = 'M'
This is because strings are immutable. This means to change this string, you will need to create a completely new string.

There are two things to keep in mind for each of the data types you are using:

Are they mutable?
Are they ordered?
Order is about whether the position of an element in the object can be used to access the element. Both strings and lists are ordered. We can use the order to access parts of a list and string.

However, you will see some data types in the next sections that will be unordered. For each of the upcoming data structures you see, it is useful to understand how you index, are they mutable, and are they ordered. Knowing this about the data structure is really useful!

Additionally, you will see how these each have different methods, so why you would use one data structure vs. another is largely dependent on these properties, and what you can easily do with it!

-----
Slicing Lists
Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
eclipse_dates= eclipse_dates[-3:]
print(eclipse_dates)


-------------------
Suppose we have the following two expressions, sentence1 and sentence2:

sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

sentence2[6]="!"

sentence1[30]="!" results in an “Error”.


sentence1 is a string, and is therefore an immutable object. That means that while you can refer to individual characters in sentence1 (e.g., you can write things like sentence1[5]) you cannot assign value to them (you cannot write things like sentence1[5] = 'a'). Therefore the third expression will result in an error.

---------------------------
Useful Functions for Lists 
len() returns how many elements are in a list.
max() returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.
min() returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged.

list1 = [1,2,3,'a','b','c']
list2 = list1
print(list1)
print(list2)

[1, 2, 3, 'a', 'b', 'c']
[1, 2, 3, 'a', 'b', 'c']

list1[0] = 'changed'
print(list1)
print(list2)

['changed', 2, 3, 'a', 'b', 'c']
['changed', 2, 3, 'a', 'b', 'c']

Both lists get changed. list1 and list2 are variables pointing to the same list.

However it is not the same case with strings:
str1 = "arpit"
str2 = str1

print(str1)
print(str2)

str1[0] = 'changed'
print(str1)
print(str2)

Can't change string because it is immutable

------
Useful Functions for Lists II
join method
Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
Output:

fore
aft
starboard
port

In this example we use the string "\n" as the separator so that there is a newline between each element. We can also use other strings as separators with .join. Here we use a hyphen.

name = "-".join(["García", "O'Kelly"])
print(name)
Output:

García-O'Kelly

append method
A helpful method called append adds an element to the end of a list.

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
Output:

['a', 'b', 'c', 'd', 'z']

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
--------------------------

You can even use the list (say VINIX) to see if a particular stock is in the index fund VINIX or not.
Like this:

'GE' in VINIX
>>> False

'GOOGL' in VINIX
>>> True

---------------------------

A data type is just a type that classifies data. This can include primitive (basic) data types like integers, booleans, and strings, as well as data structures, such as lists.

Data structures are containers that organize and group data types together in different ways. For example, some of the elements that a list can contain are integers, strings, and even other lists!

Lists are mutable, ordered data structures. The indices of a list always start with 0, not 1. Although, when going backwards, the last element starts with -1.

-----------------------

TUPLES:
It's a data type for immutable ordered sequences of elements. They are often used to store related pieces of information. 
Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices. Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.

Tuples can also be used to assign multiple variables in a compact way.

dimensions = 52, 40, 100 
length, width, height = dimensions // tuple unpacking - variables are assigned from the content of the tuple
print("The dimensions are {} x {} x {}".format(length, width, height))
The parentheses are optional when defining tuples, and programmers frequently omit them if parentheses don't clarify the code.

If we won't need to use dimensions directly, we could shorten those two lines of code into a single line that assigns three variables in one go!
length, width, height = 52, 40, 100

tuple_a = 1, 2
tuple_b = (1, 2)
print(tuple_a == tuple_b)

A tuple is an immutable, ordered data structure that can be indexed and sliced like a list. Tuples are defined by listing a sequence of elements separated by commas, optionally contained within parentheses: ().

SETS
A set is a data type for mutable unordered collections of unique elements. One application of a set is to quickly remove duplicates from a list. 

A set is a mutable data structure - you can modify the elements in a set with methods like add and pop. 
A set is an unordered data structure, so you can't index and slice elements like a list; there is no sequence of positions to index with!
One of the key properties of a set is that it only contains unique elements. So even if you create a new set with a list of elements that contains duplicates, Python will remove the duplicates when creating the set automatically.

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

Sets support the in operator the same as lists do. You can add elements to sets using the add method, and remove elements using the pop method, similar to lists. Although, when you pop an element from a set, a random element is removed. Remember that sets, unlike lists, are unordered so there is no "last element".

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)


Sets are not ordered, so the order in which items appear can be inconsistent and you add items to sets with .add. Like dictionaries and lists, sets are mutable.

You cannot have the same item twice and you cannot sort sets. For these two properties a list would be more appropriate.

=========
DICTIONARIES

A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
Dictionaries can have keys of any immutable type, like integers or tuples, not just strings. It's not even necessary for every key to have the same type! We can look up values or insert new values in the dictionary using square brackets that enclose the key.

print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
We can check whether a value is in a dictionary the same way we check whether a value is in a list or set with the in keyword. Dicts have a related method that's also useful, get. get looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.

print("carbon" in elements)
print(elements.get("dilithium"))
This would output:

True
None
Carbon is in the dictionary, so True is printed. Dilithium isn’t in our dictionary so None is returned by get and then printed. If you expect lookups to sometimes fail, get might be a better tool than normal square bracket lookups because errors can crash your program.

Identity Operators
Keyword	Operator
is	evaluates if both sides have the same identity
is not	evaluates if both sides have different identities
You can check if a key returned None with the is operator. You can check for the opposite using is not.

n = elements.get("dilithium")
print(n is None)
print(n is not None)
This would output:

True
False

get with a Default Value
Dictionaries have a related method that's also useful, get(). get() looks up values in a dictionary, but unlike looking up values with square brackets, get() returns None (or a default value of your choice) if the key isn't found. If you expect lookups to sometimes fail, get() might be a better tool than normal square bracket lookups.

>>> elements.get('dilithium')
None
>>> elements['dilithium']
KeyError: 'dilithium'
>>> elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"
we specified a default value (the string 'There's no such element!') to be returned instead of None when the key is not found.

Dictionary keys must be immutable, that is, they must be of a type that is not modifiable.
Which of these could be used as the key for a dictionary? 
string, list, int, float
Each of these types except for list can be used as a key. Since lists can be changed by adding and removing elements, they are mutable.

A dictionary is a mutable, unordered data structure that contains mappings of keys to values. Because these keys are used to index values, they must be unique and immutable. For example, a string or tuple can be used as the key of a dictionary, but if you try to use a list as a key of a dictionary, you will get an error - TypeError: unhashable type: 'list'. 
In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable, meaning its value does not change during its lifetime. This allows Python to create a unique hash value to identify it, which can be used by dictionaries to track unique keys and sets to track unique values. This is why Python requires us to use immutable datatypes for the keys in a dictionary.

The lists used in the code above are NOT immutable, and thus cannot be hashed and used as dictionary keys. Can you try modifying the datatype of the keys in the dictionary above to make the code run without errors? Hint: What other data structure can you use to store a sequence of values and is immutable?



----
What will the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

List a and list b are equal and identical. List c is equal to a (and b for that matter) since they have the same contents. But a and c (and b for that matter, again) point to two different objects, i.e., they aren't identical objects. That is the difference between checking for equality vs. identity.

A set is defined with curly braces, {}, but it isn't the only data structure that does; dictionaries do as well! However, the difference is that a set is defined as a sequence of elements separated by commas:
set_example = {element1, element2, element3}
while a dictionary is defined as a sequence of key, value pairs marked with colons, separated by commas:
dict_example = {key1: value1, key2: value2, key3: value3}.

Note: if you define a variable with an empty set of curly braces like this: a = {}, Python will assign an empty dictionary to that variable. You can always use set() and dict() to define empty sets and dictionaries as well.


=================

Compound Data Structures
We can include containers in other containers to create compound data structures. For example, this dictionary maps keys to values that are also dictionaries!

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
We can access elements in this nested dictionary like this.

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
You can also add a new key to the element dictionary.

oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)


Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. 
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas']= True

print(elements)

In this lesson, we covered four important data structures in Python:

Data Structure	Ordered	Mutable	Constructor	Example
List	Yes	Yes	[ ] or list()	[5.7, 4, 'yes', 5.7]
Tuple	Yes	No	( ) or tuple()	(5.7, 4, 'yes', 5.7)
Set	No	Yes	{}* or set()	{5.7, 4, 'yes'}
Dictionary	No	No**	{ } or dict()	{'Jun': 75, 'Jul': 89}
* You can use curly braces to define a set like this: {1, 2, 3}. However, if you leave the curly braces empty like this: {} Python will instead create an empty dictionary. So to create an empty set, use set().
** A dictionary itself is mutable, but each of its individual keys must be immutable.

=================================================================================================

Control Flow:

running code only when a particular condiion holds good...

if: An if statement must always start with an if clause, which contains the first condition that is checked. If this evaluates to True, Python runs the code indented in this if block and then skips to the rest of the code after the if statement.

elif: elif is short for "else if." An elif clause is used to check for an additional condition if the conditions in the previous clauses in the if statement evaluate to False. You can have multiple elif blocks to handle different situations.

else: Last is the else clause, which must come at the end of an if statement if used. This clause doesn't require a condition. The code in an else block is run if all conditions above that in the if statement evaluate to False.



Indentation
Some other languages use braces to show where blocks of code begin and end. In Python we use indentation to enclose blocks of code. For example, if statements use indentation to tell Python what code is inside and outside of different clauses.

In Python, indents conventionally come in multiples of four spaces. Be strict about following this convention, because changing the indentation can completely change the meaning of the code. If you are working on a team of Python programmers, it's important that everyone follows the same indentation convention!

Spaces or Tabs?
The Python Style Guide recommends using 4 spaces to indent, rather than using a tab. Whichever you use, be aware that "Python 3 disallows mixing the use of tabs and spaces for indentation."

Complex Boolean Expressions
If statements sometimes use more complicated boolean expressions for their conditions. They may contain multiple comparisons operators, logical operators, and even calculations. 
if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")




