from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice = int(input("What you want to choose? 0 or 1 or 2: "))

computer_choice = randint(0,2)
if user_choice == 0 and computer_choice == 2:
    print("Your choice is: ")
    print(rock)
    print("Computer choice is: ")
    print(scissors)
    print("You win!")

elif user_choice == 1 and computer_choice == 2:
    print("Your choice is: ")
    print(paper)
    print("Computer choice is: ")
    print(scissors)
    print("Oh, you loose!")

elif user_choice == 2 and computer_choice == 2:
    print("Your choice is: ")
    print(rock)
    print("Computer choice is: ")
    print(scissors)
    print("No one win.")

elif user_choice == 0 and computer_choice == 1:
    print("Your choice is: ")
    print(rock)
    print("Computer choice is: ")
    print(paper)
    print("Oh, you loose!")

elif user_choice == 1 and computer_choice == 1:
    print("Your choice is: ")
    print(paper)
    print("Computer choice is: ")
    print(paper)
    print("No one win.")

elif user_choice == 2 and computer_choice == 1:
    print("Your choice is: ")
    print(scissors)
    print("Computer choice is: ")
    print(paper)
    print("You win!.")

elif user_choice == 0 and computer_choice == 0:
    print("Your choice is: ")
    print(rock)
    print("Computer choice is: ")
    print(rock)
    print("No one win.")

elif user_choice == 1 and computer_choice == 0:
    print("Your choice is: ")
    print(paper)
    print("Computer choice is: ")
    print(rock)
    print("You win!")

elif user_choice == 2 and computer_choice == 0:
    print("Your choice is: ")
    print(scissors)
    print("Computer choice is: ")
    print(rock)
    print("Oh, you loose.")




'''
print(user_choice)
print(computer_choice)
'''
