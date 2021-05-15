# This is a health managment system
# Three characters are there 
# Names are Harry,Rohan and Shubham 

# Getting the current date 
def getdate():
    import datetime
    return datetime.datetime.now()

print("\n\n||| Welcome to Shree Shree Tribhuvan Baba Health Managment System ||| \n")
print("| Press The corresponding number for the name and the type of activity you have dome | \n")
print("| Press 1 if your name is Harry |")
print("| Press 2 if your name is Rohan |")
print("| Press 3 if your name is Shubham |")

print("\n | Please specify if you have to give information about excercise or food |")
print("Press 1 if you have to give information about food and 2 if you have to give information about excercise")

username_shortcut = int(input("Press The number corresponding to your name \n"))
activity_shortcut = int(input("Press The number according to your activity \n"))


# Harry food
if username_shortcut == 1 and activity_shortcut == 1 :
    filepointer1_food = open("food1.txt" , "a")
    date = getdate()
    
    activity_information_food_character1 = input("Please Enter information about what you eated \n")
    activity_information_food_character1_specified = f" [{date}] {activity_information_food_character1} "
    filepointer1_food.write(activity_information_food_character1_specified + "\n")

    filepointer1_food.close()
    # IF Else statement closes here

# Harry excercise
elif username_shortcut == 1 and activity_shortcut == 2 :
    filepointer1_excercise = open("excercise1.txt" , "a")
    date = getdate()
    
    activity_information_excercise_character1 = input("Please Enter information about what excercise you performed \n")
    activity_information_excercise_character1_specified = f" [{date}] {activity_information_excercise_character1} "
    filepointer1.write(activity_information_excercise_character1_specified + "\n")

    filepointer1_excercise.close()
    # IF Else statement closes here









# Rohan food
elif username_shortcut == 2 and activity_shortcut == 1 :
    filepointer2_food = open("food2.txt" , "a")
    date = getdate()
    
    activity_information_food_character2 = input("Please Enter information about what you eated \n")
    activity_information_food_character2_specified = f" [{date}] {activity_information_food_character2} "
    filepointer2_food.write(activity_information_food_character2_specified + "\n")

    filepointer2_food.close()
    # IF Else statement closes here

# Rohan excercise
elif username_shortcut == 2 and activity_shortcut == 2 :
    filepointer2_excercise = open("excercise2.txt" , "a")
    date = getdate()
    
    activity_information_excercise_character2 = input("Please Enter information about what excercise you performed \n")
    activity_information_excercise_character2_specified = f" [{date}] {activity_information_excercise_character2} "
    filepointer2.write(activity_information_excercise_character2_specified + "\n")

    filepointer2_excercise.close()
    # IF Else statement closes here













# Shubham food
elif username_shortcut == 3 and activity_shortcut == 1 :
    filepointer3_food = open("food3.txt" , "a")
    date = getdate()
    
    activity_information_food_character3 = input("Please Enter information about what you eated \n")
    activity_information_food_character3_specified = f" [{date}] {activity_information_food_character3} "
    filepointer3_food.write(activity_information_food_character3_specified + "\n")

    filepointer3_food.close()
    # IF Else statement closes here

# Shubham excercise
elif username_shortcut == 3 and activity_shortcut == 2 :
    filepointer3_excercise = open("excercise3.txt" , "a")
    date = getdate()
    
    activity_information_excercise_character3 = input("Please Enter information about what excercise you performed \n")
    activity_information_excercise_character3_specified = f" [{date}] {activity_information_excercise_character3} "
    filepointer3.write(activity_information_excercise_character3_specified + "\n")

    filepointer3_excercise.close()
    # IF Else statement closes here


print("/n/n ||| Thank you for giving the information |||")