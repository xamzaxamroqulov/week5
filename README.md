# Week 5
Python Functions, Modules, Packages, Classes

## Chapter 8. Functions
In this chapter you’ll learn to write functions, which are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you’ve defined in a function, you call the name of the function responsible for it. If you need to perform that task multiple times throughout your program, you don’t need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function. You’ll find that using functions makes your programs easier to write, read, test, and fix.

### Defining a Function
Here’s a simple function named greet_user() that prints a greeting:
 ```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

### Passing Information to a Function
The function now expects you to provide a value for username each time you call it. When you call greet_user(), you can pass it a name, such as 'jesse', inside the parentheses:

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```


### Positional Arguments
When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments.

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
# I have a hamster.
# My hamster's name is Harry.
```

### Multiple Function Calls
You can call a function as many times as needed. Describing a second, different pet requires just one more call to describe_pet():
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry') # order matter in Positional Arguments
describe_pet('dog', 'willie')
```
### Keyword Arguments
A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion (you won’t end up with a harry named Hamster). Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call. Let’s rewrite pets.py using keyword arguments to call describe_pet(): 
```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
```
### Default Values
When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.

For example, if you notice that most of the calls to describe_pet() are being used to describe dogs, you can set the default value of animal_type to 'dog'. Now anyone calling describe_pet() for a dog can omit that information: 
```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

# I have a dog.
# My dog's name is Willie.
```
### Equivalent Function Calls
Because positional arguments, keyword arguments, and default values can
all be used together, often you’ll have several equivalent ways to call a function.

All of the following calls would work for this function:
```python
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```
Each of these function calls would have the same output as the previous examples. 

*Note: It doesn’t really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.*

## Avoiding Argument Errors
When you start to use functions, don’t be surprised if you encounter errors about unmatched arguments. Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.





## Steps to clone the project 
1. Copy the url of the repository (https://github.com/2020spring/week5.git)

Open Git Bash and navigate to the right directory `C:\dev\` and enter following:
```bash
cd /c/dev/
git clone https://github.com/2020spring/week5.git
```

## References

* [Python Documentation - Modules](https://docs.python.org/3/tutorial/modules.html)
* [Socratica - Pyton Functions](https://youtu.be/NE97ylAnrz4)
* [Socratica - Python Recursion](https://youtu.be/Qk0zUZW-U_M)
* [Socratica - Python Classes and Objects](https://youtu.be/apACNr7DC_s)
* [Python Crash Course](http://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/No.Starch.Python.Oct_.2015.ISBN_.1593276036.pdf)
