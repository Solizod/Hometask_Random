# import random

# number=random.random() # значение от 0.0 до 1.0
# print(number)


# _________________________________________________

# import random 

# lst=[]

# for i in range (100):
#     num= random.randint(1000000000, 9999999999)
#     lst.append(num)
# print(random.sample(lst, k=2))
#____________________________________________
# import random

# name = ["Salom", "Halk", "Suhrob"]
# last_name= ["Oev", "Boev", "Salomov"]
# mails=["gmail.com", "mail.ru", "icloud.com"]

# nm=random.choice(name)
# ln=random.choice(last_name)
# ms=random.choice(mails)

# print(f"{nm}{ln}@ {ms}")


# ___________________________

# import random

# pre_num=992

# num=random.randrange(100000000, 999999999)
# print(f"+{pre_num}{num}")

# import random

# __________________________________________________________________________________________
#  Home tasks

# Guess the number 
# Numbers from 1 to 100
# lives=5
# Guessed number =27
# my input 88 - > too high
# my input 11 -> too law
# my input 28 -> too closer
# my input 29 -> too closer
# my input 27 -> You win!!!

# if my lifes equal to 0 > Game Over!!! 


# import random 

# goal=27
# turn=5
# guessed_time=0

# while turn > 0: 
#     find = int(input("Give your thought number ---> "))
#     guessed_time+=1

#     if find==goal:
#         print("You win!")
        
#     elif find > goal:
#         print("Too high ")
#     else:
#         print("Too low")


# turn-=1

# if turn==0:
#     print(f"Game over - Total guesses: {guessed_time}")

# ________________________________________________________________

# Comparing two arrays if they are equel or not

# import random

# given_number1 = [1, 0, 1, 0, 1, 1]
# given_number2 = [0, 0, 1, 1, 1, 0]

# for _ in range(6):
#     given_number1.append(random.randint(0, 1))
#     given_number2.append(random.randint(0, 1))

# if given_number1==given_number2:
#     print("Both given numbers are equal ---> ", True)
# else:
#     print("Both given numbers are not equal ---> ", False)


# ________________________________________________________________________________

# Random PASSWORD GENERATOR


# import random

# characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*[]()1234567890"

# length = 12

# password = ""
# for i in range(length):
#     password += random.choice(characters)

# print("Random password ---> ", password)

# ____________________________________________________________________________________

# import random

# player_choice = input("Enter rock, paper, or scissors: ").lower()
# computer_choice = random.choice(['rock', 'paper', 'scissors'])

# print(f"Computer chose: {computer_choice}")

# if player_choice == computer_choice:
#     print("It's a tie!")
# elif (player_choice == 'rock' and computer_choice == 'scissors') or \
#      (player_choice == 'scissors' and computer_choice == 'paper') or \
#      (player_choice == 'paper' and computer_choice == 'rock'):
#     print("You win!")
# else:
#     print("You lose!")

