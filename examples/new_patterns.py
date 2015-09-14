
"""
Using an unpythonic loop:

Instead of counting over an index and retrieving the corresponding index element within the for
loop, you should use enumerate to retrieve the index and list element simultaneously.
"""
l = [1,2,3]

#Bad
for i in range(0,len(list)):
    le = l[i]
    print(i,le)

#Good
for i,le in enumerate(l):
    print(i,le)

"""
Returning more than one variable type from function call

A function call should return only one type of variable. Example: If a function is supposed to
return a list, do not return None if an error occurs or some condition is unmet. Instead, raise
an exception.

Why this is bad:

If a function that is supposed to return a given type (e.g. list, tuple, dict) suddenly returns
something else (e.g. None) the caller of that function will always need to check the type of the
return value before proceeding. This makes for confusing and complex code. If the function is unable
to produce the supposed return value it is better to raise an exception that can be caught by the caller instead.
"""
#Bad

def filter_for_foo(l):
    r = [e for e in l if e.find("foo") != -1]
    if not check_some_critical_condition(r):
        return None
    return r

res = filter_for_foo(["bar","foo","faz"])

if res is not None:
    #continue processing
    pass

#Good

def filter_for_foo(l):
    r = [e for e in l if e.find("foo") != -1]
    if not check_some_critical_condition(r):
        raise SomeException("critical condition unmet!")
    return r

try:
    res = filter_for_foo(["bar","foo","faz"])
    #continue processing
except SomeException:
    #handle exception

"""
The loop may never terminate

The given loop does not modify anything that impacts the loop condition and does not call 'break', 'return' or 'yield' explicitly
, which may lead to an infinite loop.
"""

#example:
i = 0
while i < 10:
    do_something()
    #we forget to increment i

"""
Not using .iteritems() to iterate over a list of key/value pairs of a dictionary.
"""

#Bad

d = {'foo' : 1,'bar' : 2}

for key in d:
    value = d[key]
    print("%s = %d" % (key,value))

#Good

for key,value in d.iteritems():
    print("%s = %d" % (key,value))

"""
Not using zip() to iterate over a pair of lists
"""

#Bad

l1 = [1,2,3]
l2 = [4,5,6]

for i in range(l1):
    l1v = l1[i]
    l2v = l2[i]
    print(l1v,l2v)

#Good

for l1v,l2v in zip(l1,l2):
    print(l1v,l2v)

"""
Using "key in list" to check if a key is contained in a list.

This is not an error but inefficient, since the list search is O(n). If possible, a set or dictionary
should be used instead.

Note: Since the conversion of the list to a set is an O(n) operation, it should ideally be done only once when generating the list.
"""

#Bad:

l = [1,2,3,4]

if 3 in l:
    pass

#Good

s = set(l)

if 3 in s:
    pass

"""
Not using 'else' where appropriate in a loop.

'else' can be used in a loop context to execute code in case the loop does not get terminated by a 'break' statement.

See here for more details:
https://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
"""

#Bad

found = False

l = [1,2,3]

for i in l:
    if i == 4:
        found = True
        break

if not found:
    #not found...
    pass

#Good

for i in l:
    if i == 4:
        break
else:
    #not found...

"""
Not using .setdefault() where appropriate.

setdefault can be used to initialize a dictionary value with a default.

https://docs.python.org/2/library/stdtypes.html#dict.setdefault

For usage examples see here:

http://stackoverflow.com/questions/3483520/use-cases-for-the-setdefault-dict-method
"""

#Bad

d = {}

if not 'foo' in d:
    d['foo'] = []

d['foo'].append('bar')

#Good

d = {}

foo = d.setdefault('foo',[])
foo.append(bar)

"""
Not using .get() to return a default value from a dict

https://docs.python.org/2/library/stdtypes.html#dict.get
"""

#Bad

d = {'foo' : 'bar'}

foo = 'default'
if 'foo' in d:
    foo = d['foo']

#Good

foo = d.get('foo','default')

"""
Using map/filter where a list comprehension would be possible
"""

#Bad:

values = [1,2,3]

doubled_values = map(lambda x:x*2,values)

#Good

doubled_values = [x*2 for x in values]


#Bad

filtered_values = filter(lambda x:True if x < 2 else False,values)

#Good

filtered_values = [x for x in values if x < 2]

"""
Not using defaultdict where appropriate
"""

#Bad

d = {}

if not 'count' in d:
    d['count'] = 0

d['count']+=1

#Good

from collections import defaultdict

d = defaultdict(lambda :0)

d['count']+=1

"""
Not using a namedtuple when returning more than one value from a function

Named tuples can be used anywhere where normal tuples are acceptable, but their values can be accessed
through their name in addition to their index, which makes code more verbose and easier to read.

https://docs.python.org/2/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields


"""

#Bad

def foo():
    #....
    return -1,"not found"

status_code,message = foo()

print(status_code,message)

#Good

from collections import namedtuple

def foo():
    #...
    return_args = namedtuple('return_args',['status_code','message'])
    return return_args(-1,"not found")

ra = foo()

print(ra.status_code,ra.message)

"""
Not using explicit unpacking of sequencing

Python supports unpacking of lists, tuples and dicts.
"""

#Bad

l = [1,"foo","bar"]

l0 = l[0]
l1 = l[1]
l2 = l[2]

#Good

l0,l1,l2 = l

"""
Not using unpacking for updating multiple values at once
"""

#Bad

x = 1
y = 2

_t = x

x = y+2
y = x-4

#Good

x = 1
y = 2

x,y = y+2,x-4

"""
Not using 'with' to open files
"""

#Bad

f = open("file.txt","r")
content = f.read()
f.close()

#Good

with open("file.txt","r") as input_file:
    content = f.read()

"""
Asking for permission instead of forgiveness when working with files
"""

#Bad

import os

if os.path.exists("file.txt"):
    os.unlink("file.txt")

#Good

import os

try:
    os.unlink("file.txt")
except OSError:
    pass

"""
Not using a dict comprehension where appropriate
"""

#Bad

l = [1,2,3]

d = dict([(n,n*2) for n in l])

#Good

d = {n : n*2 for n in l}

"""
Using string concatenation instead of formatting
"""

#Bad

n_errors = 10

s = "there were "+str(n_errors)+" errors."

#Good

s = "there were %d errors." % n_errors

"""
Putting type information in the variable name (Hungarian notation)
"""

#Bad

intN = 4
strFoo = "bar"

#Good

n = 4
foo = "bar"

"""
Implementing Java-style getters and setters instead of using properties.

http://stackoverflow.com/questions/6618002/python-property-versus-getters-and-setters
"""

#Bad

class Foo(object):

    def __init__(a):
        self._a = a

    def get_a(self):
        return a

    def set_a(self,value):
        self._a = value

#Good

class Foo(object):

    def __init__(a):
        self._a = a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self,value):
        self._a = value

#Bad

def calculate_with_operator(operator, a, b):

    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '/':
        return a/b
    elif operator == '*':
        return a*b

#Good

def calculate_with_operator(operator, a, b):

    possible_operators = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b
    }

    return possible_operators[operator](a,b)

#Bad


class DateUtil:
    @staticmethod
    def from_weekday_to_string(weekday):
        nameds_weekdays = {
            0: 'Monday',
            5: 'Friday'
        }

        return nameds_weekdays[weekday]

#Good

def from_weekday_to_string(weekday):
    nameds_weekdays = {
        0: 'Monday',
        5: 'Friday'
    }

    return nameds_weekdays[weekday]
