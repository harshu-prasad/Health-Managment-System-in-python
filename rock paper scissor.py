

print("\n\n ||| Welcome to Rock Paper Scissors game |||\n")
print("| Instructions | \n")
print("|1 .You have ten chances to play|")
print("| 2. Press r for rock, p for paper and s for scissor |")
print("| 3. You will Be notified about your chances remaining with who amon gyou and computer won the game |")
print("Enjoy the game")


import random

computer_result = []
user_result = []
i = 0
while i<=9 :
    i+=1
   game_items = ['r','p','s']
   computer_choice = random.choice(game_items)
   user_choice = input("Please enter the letter corresponding to the desired action you want \n")
   if user_choice == computer_choice :
       print(f"The Game is a tie \n Computer too pointed {computer_choice} ")
       print(f"Used {i} chances out of total 10 chances total {10-i} chances remaining")

    # User did rock
    elif user_choice == 'r' and computer_choice == 'p':
        print("You lost \n Computer pointed paper")
        print(f"Used {i} chances out of total 10 chances total {10-i} chances remaining")
        computer_result.append("Won")

    elif user_choice == 'r' and computer_choice == 's':
        print("You won \n Computer pointed scissor")
        print(f"Used {i} chances out of total 10 chances total {10-i} chances remaining")
        user_result.append("Won")

    # User did paper
    elif user_choice == 'p' and computer_choice == 'r':
        print("You won \n Computer pointed rock")
        print(f"Used {i} chances out of total 10 chances total {10-i} chances remaining")
        user_result.append("Won")

    elif user_choice == 'p' and computer_choice == 's':
        print("You lost \n Computer pointed scissor")
        print(f"Used {i} chances out of total 10 chances total {10-i} chances remaining")
        computer_result.append("Won")


     # User did scissor
    elif user_choice == 's' and computer_choice == 'r':
        print("You lost \n Computer pointed rock")
        print(f"Used {i} chances out of total 10 chances total {10-i} chances remaining")
        computer_result.append("Won")

    elif user_choice == 's' and computer_choice == 'p':
        print("You won \n Computer pointed paper")
        print(f"Used {i} chances out of total 10 chances total {10-i} chances remaining")
        user_result.append("Won")
    
    if i == 10 :
        if len(user_result) > len(computer_result):
            print(f"You won the game in you won {len(user_result)} times")
        elif len(user_result) < len(computer_result):
            print(f"You lost the game in computer won {len(computer_result)} times")
        break