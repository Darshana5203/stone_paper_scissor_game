import random

rock = '''
    ________
---'   _____)
      (______)
      (______)
      (_____)
---,__(____)
'''
paper = '''
    ________
---'   _____)_____
          ________)
          _________)
        __________)
---,____________)
'''
scissors = '''
    _______
---'   ____)_____
          _______)
       ___________)
      (______)
---,__(____)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number You Lose!.")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer Choice")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win !")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose !")
    elif computer_choice > user_choice:
        print("You Lose !")
    elif user_choice > computer_choice:
        print("You Win !")
    elif user_choice == computer_choice:
        print("It's Draw !")