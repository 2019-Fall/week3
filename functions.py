# Functions 
# defining the function
def greet_user():
    """Function to greet the user."""
    print('Hello!')

# passing the arguments to our function
def greet_user_arg(name, lastname):
    """Function to greet the user with name."""
    return (f'Hello, {name} {lastname}!')


# calling the funcitons
# greet_user()
# print(greet_user_arg('John', 'Lee')) 
# msg = greet_user_arg('John', 'Lee')
# print(msg)

# keyword (default) arguments
def greet_user_kwd(name, lastname = ''):
    """Function to greet the user with name."""
    return (f'Hello, {name} {lastname}!')

print(greet_user_kwd('John'))
print(greet_user_kwd('John', lastname='Lee'))

def triangle_area(height=0, base=0):
    return height * base * 0.5

print(triangle_area(4, 5))

def describe_city(city, county='usa'):
    """ return the message with city and country"""
    return (f'{city.title()} is in {county.upper()}')

print(describe_city("chicago"))
print(describe_city("paris","france"))

def remove_duplicate(anylist):
    return set(anylist)

print(remove_duplicate([2,3,7,4,2, 9,7]))

#polindrome
def is_polindrome(phrase):
    return phrase == phrase[::-1]

print(is_polindrome('hello'))
print(is_polindrome('mom'))
print(is_polindrome('kayak'))
