class Book:

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    # reusing special buit-in methods in Python, once Book() will be called these attributes will be returned too
    def __repr__(self): # similar as __str__
        # for the string representation
        return f"Title: {self.title}, Author: {self.author}"
    # special method for len
    def __len__(self):
        return(self.pages) # we need to pass int 

myBook1=Book('Animal Farm','George Orwell',112)
print(myBook1.title)
myBook2=Book('Zero to One','Peter Thiel',243)
print(myBook2)
# instead of getting 3, since pages = 112, we get we actual numbers 
print(len(myBook1))

