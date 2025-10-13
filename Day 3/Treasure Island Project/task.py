print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____ 
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____ 
/______/______/______/______/______/______/______/______/______/______/_____ / 
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction = input("You are at a cross road. Where do you want to go? Type 'left', 'right', 'forward', or 'back': ").lower()

if direction == "left":
    decision = input("\nYou've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if decision == "wait":
        doors = input("\nYou arrive at the island unharmed. There are 3 doors: one red, one yellow, and one blue.\nWhich color do you choose? ").lower()

        if doors == "yellow":
            print("🎉 You found the treasure! You win!")
        elif doors == "blue":
            print("💦 A big wave rushes in and you drown. Game over.")
        elif doors == "red":
            print("🔥 You got caught in fire. Game over.")
        else:
            print("😕 That door doesn't exist. Game over.")
    else:
        print("🐊 There were crocodiles in the lake. Game over.")

elif direction == "right":
    cave = input("\nYou walk into a dark cave. Do you want to 'light' a torch or 'walk' in darkness? ").lower()

    if cave == "light":
        print("💎 The light reveals sparkling gems! But a hidden trap closes the entrance forever. Game over.")
    elif cave == "walk":
        print("😱 You stumble and fall into a deep pit. Game over.")
    else:
        print("🦇 You stand there until bats surround you. Game over.")

elif direction == "forward":
    forest = input("\nYou move forward into a dense forest. You hear strange noises.\nDo you 'follow' the sound or 'hide'? ").lower()

    if forest == "follow":
        print("🦜 You find a talking parrot who leads you to the treasure chest. You win!")
    elif forest == "hide":
        print("🐅 A tiger finds you before you can escape. Game over.")
    else:
        print("🌲 You get lost forever in the forest. Game over.")

elif direction == "back":
    camp = input("\nYou return to your camp. Do you 'rest' or 'explore' the nearby ruins? ").lower()

    if camp == "rest":
        print("😴 You fall asleep and wake up to find your supplies stolen. Game over.")
    elif camp == "explore":
        print("🏺 Inside the ruins, you discover an ancient treasure. You win!")
    else:
        print("🌪️ You wander aimlessly and get caught in a sandstorm. Game over.")

else:
    print("💀 You took a wrong path and fell into a hole. Game over.")
