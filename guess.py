#start
#importing random
import random;
#the prints
print("number gzuessing game")
print("Guess a number between 1 and 9")
#making a random no bwt 1-9
randNo =(random.choice([1,2,3,4,5,6,7,8,9,5,6,7,3,4,7,2,4,5,8,9,2,3,3,2,4,5,8,6,4]))
#an infinite loop
while True:
    #inputting the guessed no
    no = input("Enter your guess :-")
    #if higher, we say it
    if int(no) > int(randNo):
        print("Your guess was too high: Guess a number lesser than "+no)
    
    #if lower, we say it
    if int(no) < int(randNo):
        print("Your guess was too low: Guess a number more than "+no)
    
    #if same, we say it. and Congragulate
    if int(no) == int(randNo):
        print("YAY!!! You found the no")
        #break the prog
        break

#END
