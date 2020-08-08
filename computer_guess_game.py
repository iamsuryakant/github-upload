from random import randint
computer_guess=randint(1,100)
chance=1
while chance<=5:
    user_input=int(input("Enter a number : "))
    if user_input>100 or user_input<1:
        continue
    elif computer_guess==user_input:
        print("you win")
        break
    elif computer_guess<user_input:
        print("take small number")
    elif computer_guess>user_input:
        print("take larger number")
    chance=chance+1
else:
    print("better luck next time")
    print("you are such a looser")
    print(f"number is : {computer_guess}")
#from random import randint
