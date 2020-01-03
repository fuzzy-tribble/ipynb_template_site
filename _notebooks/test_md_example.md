---
layout: notebook
title: Test MD
permalink: /testmd/
topics: ['Test1', 'Test2']
---

# Python3 Fluency Workbook: Functions

**Purpose:** The purpose of this workbook is to help you get comfortable with functions in Python3.

**Recomended Usage**
* Run each of the cells (Shift+Enter) and edit them as necessary to solidify your understanding
* Do any of the exercises that are relevant to helping you understand the material

**Topics Covered**
* Basic Functions
* Generators
* Lambda Expressions
* Partial Functions
* Nested Functions
* Positional and Keyword Arguments (args and kwargs)

# Workbook Setup

## Troubleshooting Tips

If you run into issues running any of the code in this notebook, check your version of Jupyter, extensions, etc.

```bash
!jupyter --version

jupyter core     : 4.6.1
jupyter-notebook : 6.0.2
qtconsole        : not installed
ipython          : 7.9.0
ipykernel        : 5.1.3
jupyter client   : 5.3.4
jupyter lab      : 1.2.3
nbconvert        : 5.6.1
ipywidgets       : not installed
nbformat         : 4.4.0
traitlets        : 4.3.3
```

```bash
!jupyter-labextension list

JupyterLab v1.2.3
Known labextensions:
   app dir: /usr/local/share/jupyter/lab
        @aquirdturtle/collapsible_headings v0.5.0  enabled  OK
        @jupyter-widgets/jupyterlab-manager v1.1.0  enabled  OK
        @jupyterlab/git v0.8.2  enabled  OK
        @jupyterlab/github v1.0.1  enabled  OK
        jupyterlab-flake8 v0.4.0  enabled  OK

Uninstalled core extensions:
    @jupyterlab/github
    jupyterlab-flake8
```


```python
#!jupyter --version
```


```python
#!jupyter-labextension list
```

## Notebook Configs


```python
# AUTO GENERATED CELL FOR NOTEBOOK SETUP

# NOTEBOOK WIDE MAGICS

# Reload all modules before executing a new line
%load_ext autoreload
%autoreload 2

# Abide by PEP8 code style
%load_ext pycodestyle_magic
%pycodestyle_on

# LIBRARY SPECIFIC MAGICS - UNCOMMENT AS NEEDED

# Plot all matplotlib plots in output cell and save on close
# %matplotlib inline
```


```python
import functools
```

# Basic Functions

> ```python
def function_name(arg_1, arg_2):
    pass
```


```python
def my_function(arg_1):
    print("arg_1 is: {}".format(arg_1))


my_function("test")
```

    arg_1 is: test



```python
def my_function(arg_1):
    return arg_1 + 1


result = my_function(3)
print(result)
```

    4


# Generators

Generators produce values one-at-a-time as opposed to functions which give them all at once. Its particularly useful when dealing with big data because we just access values one at a time.

```python
def my_generator():
    yield "a"
```

## Generator functions


```python
# Regular function
def function_a():
    return "a"

# Generator function
def generator_a():
    yield "a"
```


```python
function_a()
```




    'a'




```python
generator_a()
```




    <generator object generator_a at 0x11410df50>




```python
next(generator_a())
```




    'a'



*Note: You can only use a generator ONCE (once you get to the end, you're done).*

## Generator Expressions


```python
# Traditional list comprehension (uses brackets)
lc_example = [n**2 for n in [1, 2, 3, 4, 5]]
lc_example
```




    [1, 4, 9, 16, 25]




```python
# Generator expression (uses parentheses)
gen_exp1 = (n**2 for n in [1, 2, 3, 4, 5])
gen_exp1
```




    <generator object <genexpr> at 0x113367350>



There are two ways to get the next item from a generator; next() and a for loop


```python
print(next(gen_exp1))
print(next(gen_exp1))
print(next(gen_exp1))
```

    1
    4
    9



```python
for item in gen_exp1:
    print(item)
```

    16
    25



```python
gen_exp2 = (n**2 for n in [1, 2, 3, 4, 5] if n >= 3)
print(next(gen_exp2))
print(next(gen_exp2))
```

    9
    16


One practical example could be to read in a very large file row by row.

```python
def rowByRowGenerator():
    file = "veryBIGFile.csv"
    for row in open(file):
        yield row
```

# Lambda Expressions

Lambda expressions (sometimes called lambda functions) are small (single expression) anonymous functions created using the lambda keyword. They are especially useful in situations when you don't want/need to use a whole function definition but rather just have a small expression.

> `lambda arguments: expression`

For example, the following are functionally equivalent:

```python
def f(x): return 2*x 
# ACTS THE SAME AS
f = lambda x: 2*x 
```

<span style="color:red;"><b>Best Practice Note:</b> Though the def and lambda expression above are equivalent, you generally want to assign a lambda expression to a name. It defeats the purpose of it, see best use cases below.</span>

### Lambda expressions as function arguments

Lambda expressions are really useful when a function takes another function as a parameter like in the `map()` function

> `map(func, *iterables) --> map object`


```python
original_list = [1, 2, 3, 4]
```


```python
doubled_list = map(lambda x: x*2, original_list)
```


```python
print('Original List: {}'.format(original_list))
print('Doubled List: {}'.format(list(doubled_list)))
```

    Original List: [1, 2, 3, 4]
    Doubled List: [2, 4, 6, 8]


You can also use it in the case of in the `sort()` function.

> `sort(*, key=None, reverse=False)`


```python
pairs = [(4, 'c'), (2, 'b'), (3, 'a'), (1, 'd')]
```


```python
# Sort the pairs by the 0th element in each pair
pairs.sort(key=lambda pair: pair[0])
print(pairs)
```

    [(1, 'd'), (2, 'b'), (3, 'a'), (4, 'c')]



```python
# Sort the pairs by the 1th element in each pair
pairs.sort(key=lambda pair: pair[1])
print(pairs)
```

    [(3, 'a'), (2, 'b'), (4, 'c'), (1, 'd')]


# Partial Functions

After importing partial from functools you can use partial functions. 

A partial function is really useful for being able to add some default arguments to a function so you don't need to repeat all the arguments all of the time.

The general syntax for a partial function is this:
> `variable = partial(function_name, function_params)`


```python
from functools import partial
```


```python
# Say we have a regular function def that multiplies two numbers
def multiply(x, y):
    print(x, y)
    return x * y
```


```python
# We can create a new function that multiplies by 2
dbl = partial(multiply, 2)
```


```python
# Then dbl(4) is called with the 2 already there
print(dbl(4))
```

    2 4
    8


In this case we start with a normal function definition called `multiply()` that multiplies to inputs. We can then create a partial function definition that uses a spin off of that function called `dble` by always setting one param as 2.

# Nested Functions

In Python, you can define nested or inner functions like in the examples below. They are most widely used in the case of decorators (see the "Decorators Workbook" for more).


```python
def parent():
    print("parent() funct")

    def first_child():
        print("first_child() funct")

    def second_child():
        print("second_child() funct")

    first_child()
    second_child()
```


```python
parent()
```

    parent() funct
    first_child() funct
    second_child() funct


We can call `parent()` and return the functions that handle each case


```python
def parent(num):
    def first_child():
        return "Hi, I am the 1st child"

    def second_child():
        return "Hi, I am the 2nd child"

    if num == 1:
        return first_child
    else:
        return second_child
```


```python
first = parent(1)
first
```




    <function __main__.parent.<locals>.first_child()>




```python
first()
```




    'Hi, I am the 1st child'




```python
second = parent(2)
second
```




    <function __main__.parent.<locals>.second_child()>




```python
second()
```




    'Hi, I am the 2nd child'



# Positional and Keyword Arguments

Functions in Python can have positional and/or keyword arguments. They can be a fixed number of arguments or variable.

In Python3.8 there is a new function parameter syntax `/` to indicate that some function parameters must be specified positionally and cannot be used as keyword arguments. Check out the [examples from the docs below](https://docs.python.org/3.8/whatsnew/3.8.html#summary-release-highlights)


```python
# Make sure you are using Python3 or you may get an error
import sys
print(sys.version)
```

    3.7.5 (default, Nov  1 2019, 13:00:01) 
    [Clang 11.0.0 (clang-1100.0.33.8)]



```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```


      File "<ipython-input-4-bd67c2300f8f>", line 1
        def f(a, b, /, c, d, *, e, f):
                    ^
    SyntaxError: invalid syntax




```python
f(10, 20, 30, d=40, e=50, f=60)
```


```python
f(10, b=20, c=30, d=40, e=50, f=60)   # b cannot be a keyword argument
f(10, 20, 30, 40, 50, f=60)           # e must be a keyword argument
```

Since the parameters to the left of / are not exposed as possible keywords, the parameters names remain available for use in **kwargs:


```python
def f(a, b, /, **kwargs):
    print(a, b, kwargs)

f(10, 20, a=1, b=2, c=3)         # a and b are used in two ways
```

### Packing and unpacking using `*`

When you see `*` or `**` in front of a variable in Python they are used to unpack iterables and dictionaries respectively.

They are frequently used to unpack a variable number of function arguments using `*args` (arguments) and `**kwargs` (keyword arguments) in function definitions.


```python
# *args is used to pass in a variable number of arguments
def sayThis1(*argv):
    for arg in argv:
        print(arg)
```

    2:1: E302 expected 2 blank lines, found 0
    2:1: E302 expected 2 blank lines, found 0
    2:1: E302 expected 2 blank lines, found 0
    2:1: E302 expected 2 blank lines, found 0
    2:1: E302 expected 2 blank lines, found 0



```python
sayThis1('Hi', 'whats', 'going', 'on') # Pass in any number of args
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-15-52fbf7181596> in <module>
    ----> 1 sayThis1('Hi', 'whats', 'going', 'on') # Pass in any number of args
    

    NameError: name 'sayThis1' is not defined


    1:39: E261 at least two spaces before inline comment



```python
# **kwargs is used to pass a variable number of keyword arguments   
def sayThis2(**kwargs):
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value))
```


```python
sayThis2(first ='Love', mid ='is', last='good') 
```

    first == Love
    mid == is
    last == good



```python
my_list = [1, 2, 3]
print(my_list)  # Packed
print(*my_list)  # Unpacked
```

    [1, 2, 3]
    1 2 3


### Extract/unpack the body of a list

The asterisk can also be used to unpack the body of something.


```python
my_list = [1, 2, 3, 4, 5, 6]
my_list
```




    [1, 2, 3, 4, 5, 6]




```python
a, *b, c = my_list
print(a)
print(b)
print(c)
```

    1
    [2, 3, 4, 5]
    6


### Merging lists and dicts by unpacking


```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]  # Unpack each list into a new list

print(merged_list)
```

    [1, 2, 3, 4, 5, 6]



```python
dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}
merged_dict = {**dict1, **dict2}

print(merged_dict)
```

    {'A': 1, 'B': 2, 'C': 3, 'D': 4}


### Unpack a string into chars


```python
a = [*"SomeStringOfChars"]
print(a)
```

    ['S', 'o', 'm', 'e', 'S', 't', 'r', 'i', 'n', 'g', 'O', 'f', 'C', 'h', 'a', 'r', 's']

