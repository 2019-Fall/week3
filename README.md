# Week 3
Dictionaries, nested dictionaries, Functions

### Chapter 9. Dictionaries
In this chapter you’ll learn how to use Python’s dictionaries, which allow you to connect pieces of related information. You’ll learn how to access the information once it’s in a dictionary and how to modify that information. Because dictionaries can store an almost limitless amount of information, I’ll show you how to loop through the data in a dictionary. Additionally, you’ll learn to nest dictionaries inside lists, lists inside dictionaries, and even dictionaries inside other dictionaries.

#### A Simple Dictionary
```python 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

The dictionary alien_0 stores the alien’s color and point value. The two print statements access and display that information, as shown here:
```python
green
5
```

#### Looping Through All Key-Value Pairs
```python
for key, value in alien_0.items():
    print("Key: " + key)
    print("Value: " + value)
````

#### Looping Through All Keys
```python
for key in alien_0.keys():
    print("Key: " + key)
````

#### Looping Through All Values
```python
for value in alien_0.values():
    print("Value: " + value)
````

### Chapter 8. Functions
In this chapter you’ll learn to write functions, which are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you’ve defined in a function, you call the name of the function responsible for it. If you need to perform that task multiple times throughout your program, you don’t need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function. You’ll find that using functions makes your programs easier to write, read, test, and fix.

#### Defining a Function
Here’s a simple function named greet_user() that prints a greeting:
 ```python
 def greet_user():
     """Display a simple greeting."""
     print("Hello!")

greet_user()
```

## Steps to clone the project 
1. Copy the url of the repository ending with .git (https://github.com/2019-Fall/week3.git)
2. GitHub Desktop: 
    * Go to Current Repository
    * click on Add drop down
    * Clone Repository
    * click on URL tab
    * paste the copied URL (https://github.com/2019-Fall/week3.git)
    * choose the location from your local machine `C:\dev\` then click on Clone.

    Git Bash: navigate to the right directory `C:\dev\` and enter following:
  ```bash
  git clone https://github.com/2019-Fall/week3.git
  ```

  3. [optional] Create your feature branch: 
  ```bash
  git checkout -b week3_john
  ```
  4. Open the `C:\dev\week3` folder from your VS Code and start modifying the code.

// changes here 

## References
* [Python Documentation - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
* [Socratica - Dictionaries](https://youtu.be/XCcpzWs-CI4)
* [Python Crash Course](http://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/No.Starch.Python.Oct_.2015.ISBN_.1593276036.pdf)
