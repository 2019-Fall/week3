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
