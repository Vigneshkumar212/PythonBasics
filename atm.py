class Atm(object):
    def __init__(self, cardNumber, password):
        self.cardNumber = cardNumber
        self.password = password
        self.balanceAmt = 10587852
    
    def withdraw(self, amount):
        choice = str(input("Do you want to withdraw Rs."+str(amount)+" from your bank account? Yes / NO"))
        if(choice=="Yes"):
            print("You have withdrawn Rs."+str(amount)+" from your bank account.")
            self.balanceAmt -= amount
            print("Your account balance is Rs."+str(self.balanceAmt))
            print()
            print("You Receved Rs."+str(amount)+" In Cash!")
        
        if(choice=="yes"):
            print("You have withdrawn Rs."+str(amount)+" from your bank account.")
            self.balanceAmt -= amount
            print("Your account balance is Rs."+str(self.balanceAmt))
            print()
            print("You Receved Rs."+str(amount)+" In Cash!")

        if(choice == "No"): 
            print("Withdrawl cancled!")

        if(choice == "no"): 
            print("Withdrawl cancled!")


    def balance(self):
        print("Your account balance is Rs."+str(self.balanceAmt))

    def deposit(self, amount):
        choice = str(input("Do you want to deposit Rs."+str(amount)+" to your bank account? Yes / NO"))

        if(choice=="Yes"):
            print("You have deposited Rs."+str(amount)+" to your bank account.")
            self.balanceAmt += amount
            print("Your account balance is Rs."+str(self.balanceAmt))
            print()
            print("Rs."+str(amount)+" Was removed from your pocket!")
        
        if(choice=="yes"):
            print("You have deposited Rs."+str(amount)+" to your bank account.")
            self.balanceAmt += amount
            print("Your account balance is Rs."+str(self.balanceAmt))
            print()
            print("Rs."+str(amount)+" Was removed from your pocket!")

        if(choice == "No"): 
            print("deposit cancled!")

        if(choice == "no"): 
            print("deposit cancled!")
    
    def getAccountInfo(self):
        print('Your Account Info: ')
        print('Account No : '+str(self.cardNumber))
        print('Password : encrypted')
        print("Balance : "+str(self.balanceAmt))

    def changePassword(self, prvPass):
        if(prvPass == self.password):
            newPass =input("Enter New Passowrd")
            newCPass = input("Confirm New Passowrd")
            if(newPass == newCPass):
                print("password changed!")
            else:
                print("Password Didn't match")
        else: 
            print("Incorrect Old Password")

myBank = Atm(2902334909, "thisIsNotMyCard")

print()
print("Getting account info:")
print()
myBank.getAccountInfo()
print()
print("withdrawing 1240")
print()
myBank.withdraw(1240)
print()
print("depositing 10234")
print()
myBank.deposit(10234)
print()
print("now using the balance funtion")
print()
myBank.balance()
print()
print("changing password")
print()
myBank.changePassword("thisIsNotMyCard")

print()
print("END!!!")
