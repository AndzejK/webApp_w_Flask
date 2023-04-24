# Scopes

# How python will look for a var - LEGB
#1. Local
#2. Enclosing
#3. Global
#4. Built-in

# Global level
x='This Global scope'

def change_scope():
    # Local scope/assignment 
    x='inside'
    return x

#Enclosing having more than one function in the function
def enclosing():
    z='Enclosing scope'
    # creating another fn
    def inside():
        # LEGB
        y='Local scope'
        print(x)
    # call this inside function, inside()
    inside()

enclosing()


