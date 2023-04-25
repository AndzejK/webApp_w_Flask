####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    # The method for depositing $$$
    def deposit(self,depos):
        self.depos=depos
        self.balance+=self.depos
        print(f"A new balance: {self.balance}")

    # The method for withdrawing $$$
    def withdrawal(self,withdraw):
        self.withdraw=withdraw
        if self.balance<self.withdraw:
            print(f"Ops... not enough funds")
        else:
            self.balance-=self.withdraw
        print(f"A new balance: {self.balance}")

    # using special method for returning attribites which were added
    def __repr__(self):
    # for the string representation
        return f"Owner: {self.owner}, Balance: {self.balance}"


# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
print(acct1.owner)




# 4. Show the account balance attribute
print(acct1.balance)




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.deposit(50)
acct1.deposit(50)




acct1.withdrawal(50)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdrawal(500)



# ## Good job!
