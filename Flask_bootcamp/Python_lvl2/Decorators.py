# Decorators allow us to tack on (add something that already exists) extra functionality to an 
# already existing funciton, @ operator is used for that and a fn is placed on the top of the org fun
import time
from datetime import datetime

# functions in functions plus returning function :)
def simple_func(name='Andrew'):
    time_now=datetime.today()
    print(time_now)
    def greet():
        return "    This is inside the greet() fn"
    def welcome():
        return "    This is inside welcome() fn"
    # here we're returning funcotions/methods!
    if name=='Andrew':
        return greet
    else:
        return welcome
    
x=simple_func()

# passing function as an argument
def hell0():
    return "hey Andrew!"
# here I'm passing a fn
def other(fn):
    print("It's a beautiful day!")
    # here I will execute the passed fn
    print(fn())
res=other(hell0)

# decorators -  are a way to group similar functions together based on their functionality, and they can make your code more efficient and organized
print('----------------------------------------')

# fn that will pass as a arg to the fn
def new_decorator(fn):
    def wrap_fn(): # this part is only run when a decorator fn is run
        print('Some code BEFORE executing the function')
        fn()
        print('Some code AFTER executing the function')
    return wrap_fn


# or I can use python syntex to call decorator
@new_decorator
def fn_needs_decorator():
    print('Please decorate me!')

# the same fn's name is assigned a new fn and passing itself and here we don't use "()" bu fn is being executed
fn_needs_decorator=new_decorator(fn_needs_decorator) # = @new_decorator

# finally calling myself
fn_needs_decorator()
print('----------------------------------------')
#new_decorator(fn_needs_decorator)