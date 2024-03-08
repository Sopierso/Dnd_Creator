import random 
import library_dnd
import os
import traceback



# welcome/intro
def welcome():
    while True:
        print("Welcome to Sophie's DnD Character creator and dice bot")
        playerinput = input("""To start, please select 'D' to access the dice bot or 'C' to access the character creator: """).upper()
        if playerinput == "D":
            dicebot()
        elif playerinput == "C":
            charactercreation()
        elif playerinput == "Q":
            break
        else:
            print("Wrong. Do it again.")

# yeah, roll that dice
def dicebot():
    while True:
        print("You have selected the dice bot. Enter 'Q' to quit at any time")
        dicetype = input("Please select one of the dice types to roll: d20, d12, d10, d8, d6, d4, d2: ")
        if dicetype == "d20":
            roll = random.randint(1, 20)
            print(f"Roll result: {roll}")
        elif dicetype == "d12":
            roll = random.randint(1, 12)
            print(f"Roll result: {roll}")
        elif dicetype == "d10":
            roll = random.randint(1, 10)
            print(f"Roll result: {roll}")
        elif dicetype == "d8":
            roll = random.randint(1, 8)
            print(f"Roll result: {roll}")
        elif dicetype == "d6":
            roll = random.randint(1, 6)
            print(f"Roll result: {roll}")
        elif dicetype == "d4":
            roll = random.randint(1, 4)
            print(f"Roll result: {roll}")
        elif dicetype == "d2":
            roll = random.randint(1, 2)
            print(f"Roll result: {roll}")
        elif dicetype.lower() == "q":
            break
        else:
            print("That dice type does not exist, please try again.")

def charactercreation():
    
    #Strength-0 Charisma-1 Wisdom-2 Intelligence-3 Dexterity-4 Constitution-5
    abilityscore_list = [0, 0, 0, 0, 0, 0]
    abilitymod_list = [0, 0, 0, 0, 0, 0]

    while True:
        
        print("Welcome to the Character Creator!")
        print("---------------------------------")
        print("To start we are going to figure out our ability scores and modifiers")
        ability_score(abilityscore_list, abilitymod_list)
        print("\t\tPlease Choose Race")
        print("------------------------")
        print("\tHuman")
        print("\tTiefling")

        race = input("").capitalize()

        if race == "Human":
            print("\tYou have selected Human")
            for i in range(len(abilitymod_list)):
                abilitymod_list[i] += 1
        elif race == "Tiefling":
            print("\tYou have selected Tiefling")
            abilitymod_list[1] += 2
        else:
            print("Be better, stupid")

        class_dnd = choice_class(abilitymod_list)
        health = healthcalc(class_dnd, abilitymod_list)
        weapon_list = weaponselection(class_dnd)
        printsheet(abilitymod_list, abilityscore_list, health, class_dnd, weapon_list)

def choice_class(abilitymod_list):
    
    print("\tPlease Choose Class")
    print("\t\tPaladin")
    print("\t\tFighter")

    class_dnd = input("").capitalize()

    if class_dnd == "Paladin":
        abilitymod_list[5] += 1
        print("Would you like the Paladin description? (y/n) ")
        palinfo = input("").lower()
        if palinfo == "y":
            print("Display Paladin info")
        
    elif class_dnd =="Fighter":
        print("Would you like the Fighter description? (y/n)")
        fightinfo = input("").lower()
        if fightinfo == "y":
            print("Display Fighter info")
    else:
        print("You can't type")
    
    return class_dnd

    

def healthcalc(class_dnd, abilitymod_list):
    health = 0

    print("Welcome to the health rolling portion of the Character Creator")
    print(f"You chose {class_dnd} as your class")

    if class_dnd == "Paladin":
        print("Paladins have 1d10 for each level plus the Con modifier")
        health = random.randint(1, 10)
        health += abilitymod_list[5]
        print(f"Health = {health}")
        user_input = input("Rolling 1d10... Would you like to roll again? (y/n) ").lower()
        while user_input == "y":
            health = random.randint(1, 10)
            health += abilitymod_list[5]
            print(f"Your Paladin's health is {health}")
            user_input = input("Rolling 1d10... Would you like to roll again? (y/n)").lower()
    elif class_dnd == "Fighter":
        print("Fighter have 1d10 for each level")
        health = random.randint(1, 10)
        print(f"Health = {health}")
        user_input = input("Rolling 1d10... Would you like to roll again? (y/n)").lower()
        while user_input == "y":
            health = random.randint(1, 10)
            health += abilitymod_list[5]
            print(f"Your Fighter's health is {health}")
            user_input = input("Rolling 1d10... Would you like to roll again? ").lower()



    print("Congrats! You are one step closer to completing your character")
    return health


    
    

def ability_score(abilityscore_list, abilitymod_list):
    print("Welcome to the ability score part of the Character Creation")
    print("We are going to roll 4d6 for each ability and drop the lowest score")

    for i in range(6):
        rolls = [random.randint(1, 6) for _ in range(4)]
        min_roll = min(rolls)
        rolls.remove(min_roll)
        abilityscore_list[i] = sum(rolls)

    print(f"Ability Scores: {abilityscore_list}")
    abilitymod_list = mod_determine(abilityscore_list)
    print(f"Ability Modifiers: {abilitymod_list}")

def mod_determine(abilityscore_list):
    abilitymod_list = [0, 0, 0, 0, 0, 0]
    
    #Charaisma mod
    if abilityscore_list[0] == 1:
        abilitymod_list[0] = -5
    elif abilityscore_list[0] == 2 or abilityscore_list[0] == 3:
        abilitymod_list[0] = -4
    elif abilityscore_list[0] == 4 or abilityscore_list[0] == 5:
        abilitymod_list[0] = -3       
    elif abilityscore_list[0] == 6 or abilityscore_list[0] == 7:
        abilitymod_list[0] =-2
    elif abilityscore_list[0] == 8 or abilityscore_list[0] == 9:
        abilitymod_list[0] =-1
    elif abilityscore_list[0] == 10 or abilityscore_list[5] == 11:
        abilitymod_list[0] = 0
    elif abilityscore_list[0] == 12 or abilityscore_list[0] == 13:
        abilitymod_list[0] = 1
    elif abilityscore_list[0] == 14 or abilityscore_list[0] == 15:
        abilitymod_list[0] = 2
    elif abilityscore_list[0] == 16 or abilityscore_list[0] == 17:
        abilitymod_list[0] = 3
    elif abilityscore_list[0] == 18 or abilityscore_list[0] == 19:
        abilitymod_list[0] = 4
    elif abilityscore_list[0] == 20 or abilityscore_list[0] == 21:
        abilitymod_list[0] = 5
    elif abilityscore_list[0] == 22 or abilityscore_list[0] == 23:
        abilitymod_list[0] = 6
    else:
        abilitymod_list[0] = 7
    
    #STRENGTH MOD
    if abilityscore_list[1] == 1:
        abilitymod_list[1] = -5
    elif abilityscore_list[1] == 2 or abilityscore_list[5] == 3:
        abilitymod_list[1] = -4
    elif abilityscore_list[1] == 4 or abilityscore_list[5] == 5:
        abilitymod_list[1] = -3       
    elif abilityscore_list[1] == 6 or abilityscore_list[1] == 7:
        abilitymod_list[1] =-2
    elif abilityscore_list[1] == 8 or abilityscore_list[1] == 9:
        abilitymod_list[1] =-1
    elif abilityscore_list[1] == 10 or abilityscore_list[1] == 11:
        abilitymod_list[1] = 0
    elif abilityscore_list[1] == 12 or abilityscore_list[1] == 13:
        abilitymod_list[1] = 1
    elif abilityscore_list[1] == 14 or abilityscore_list[1] == 15:
        abilitymod_list[1] = 2
    elif abilityscore_list[1] == 16 or abilityscore_list[1] == 17:
        abilitymod_list[1] = 3
    elif abilityscore_list[1] == 18 or abilityscore_list[1] == 19:
        abilitymod_list[1] = 4
    elif abilityscore_list[1] == 20 or abilityscore_list[1] == 21:
        abilitymod_list[1] = 5
    elif abilityscore_list[1] == 22 or abilityscore_list[1] == 23:
        abilitymod_list[1] = 6
    else:
        abilitymod_list[1] = 7
    

    if abilityscore_list[2] == 1:
        abilitymod_list[2] = -5
    elif abilityscore_list[2] == 2 or abilityscore_list[2] == 3:
        abilitymod_list[2] = -4
    elif abilityscore_list[2] == 4 or abilityscore_list[2] == 5:
        abilitymod_list[2] = -3       
    elif abilityscore_list[2] == 6 or abilityscore_list[2] == 7:
        abilitymod_list[2] =-2
    elif abilityscore_list[2] == 8 or abilityscore_list[2] == 9:
        abilitymod_list[2] =-1
    elif abilityscore_list[2] == 10 or abilityscore_list[2] == 11:
        abilitymod_list[2] = 0
    elif abilityscore_list[2] == 12 or abilityscore_list[2] == 13:
        abilitymod_list[2] = 1
    elif abilityscore_list[2] == 14 or abilityscore_list[2] == 15:
        abilitymod_list[2] = 2
    elif abilityscore_list[2] == 16 or abilityscore_list[2] == 17:
        abilitymod_list[2] = 3
    elif abilityscore_list[2] == 18 or abilityscore_list[2] == 19:
        abilitymod_list[2] = 4
    elif abilityscore_list[2] == 20 or abilityscore_list[2] == 21:
        abilitymod_list[2] = 5
    elif abilityscore_list[2] == 22 or abilityscore_list[2] == 23:
        abilitymod_list[2] = 6
    else:
        abilitymod_list[2] = 7

    if abilityscore_list[3] == 1:
        abilitymod_list[3] = -5
    elif abilityscore_list[3] == 2 or abilityscore_list[3] == 3:
        abilitymod_list[3] = -4
    elif abilityscore_list[3] == 4 or abilityscore_list[3] == 5:
        abilitymod_list[3] = -3       
    elif abilityscore_list[3] == 6 or abilityscore_list[3] == 7:
        abilitymod_list[3] =-2
    elif abilityscore_list[3] == 8 or abilityscore_list[3] == 9:
        abilitymod_list[3] =-1
    elif abilityscore_list[3] == 10 or abilityscore_list[3] == 11:
        abilitymod_list[3] = 0
    elif abilityscore_list[3] == 12 or abilityscore_list[3] == 13:
        abilitymod_list[3] = 1
    elif abilityscore_list[3] == 14 or abilityscore_list[3] == 15:
        abilitymod_list[3] = 2
    elif abilityscore_list[3] == 16 or abilityscore_list[3] == 17:
        abilitymod_list[3] = 3
    elif abilityscore_list[3] == 18 or abilityscore_list[3] == 19:
        abilitymod_list[3] = 4
    elif abilityscore_list[3] == 20 or abilityscore_list[3] == 21:
        abilitymod_list[3] = 5
    elif abilityscore_list[3] == 22 or abilityscore_list[3] == 23:
        abilitymod_list[3] = 6
    else:
        abilitymod_list[3] = 7


    if abilityscore_list[4] == 1:
        abilitymod_list[4] = -5
    elif abilityscore_list[4] == 2 or abilityscore_list[4] == 3:
        abilitymod_list[4] = -4
    elif abilityscore_list[4] == 4 or abilityscore_list[4] == 5:
        abilitymod_list[4] = -3       
    elif abilityscore_list[4] == 6 or abilityscore_list[4] == 7:
        abilitymod_list[4] =-2
    elif abilityscore_list[4] == 8 or abilityscore_list[4] == 9:
        abilitymod_list[4] =-1
    elif abilityscore_list[4] == 10 or abilityscore_list[4] == 11:
        abilitymod_list[4] = 0
    elif abilityscore_list[4] == 12 or abilityscore_list[4] == 13:
        abilitymod_list[4] = 1
    elif abilityscore_list[4] == 14 or abilityscore_list[4] == 15:
        abilitymod_list[4] = 2
    elif abilityscore_list[4] == 16 or abilityscore_list[4] == 17:
        abilitymod_list[4] = 3
    elif abilityscore_list[4] == 18 or abilityscore_list[4] == 19:
        abilitymod_list[4] = 4
    elif abilityscore_list[4] == 20 or abilityscore_list[4] == 21:
        abilitymod_list[4] = 5
    elif abilityscore_list[4] == 22 or abilityscore_list[4] == 23:
        abilitymod_list[4] = 6
    else:
        abilitymod_list[4] = 7


    if abilityscore_list[5] == 1:
        abilitymod_list[5] = -5
    elif abilityscore_list[5] == 2 or abilityscore_list[5] == 3:
        abilitymod_list[5] = -4
    elif abilityscore_list[5] == 4 or abilityscore_list[5] == 5:
        abilitymod_list[5] = -3       
    elif abilityscore_list[5] == 6 or abilityscore_list[5] == 7:
        abilitymod_list[5] =-2
    elif abilityscore_list[5] == 8 or abilityscore_list[5] == 9:
        abilitymod_list[5] =-1
    elif abilityscore_list[5] == 10 or abilityscore_list[5] == 11:
        abilitymod_list[5] = 0
    elif abilityscore_list[5] == 12 or abilityscore_list[5] == 13:
        abilitymod_list[5] = 1
    elif abilityscore_list[5] == 14 or abilityscore_list[5] == 15:
        abilitymod_list[5] = 2
    elif abilityscore_list[5] == 16 or abilityscore_list[5] == 17:
        abilitymod_list[5] = 3
    elif abilityscore_list[5] == 18 or abilityscore_list[5] == 19:
        abilitymod_list[5] = 4
    elif abilityscore_list[5] == 20 or abilityscore_list[5] == 21:
        abilitymod_list[5] = 5
    elif abilityscore_list[5] == 22 or abilityscore_list[5] == 23:
        abilitymod_list[5] = 6
    else:
        abilitymod_list[5] = 7
    
    

    return abilitymod_list
    
    
   

def printsheet(abilitymod_list, abilityscore_list, health, class_dnd, weaponlist):
    name = input('Congrats on completing your character, what would you like to name them?')
    
    
    #Strength-0 Charisma-1 Wisdom-2 Intelligence-3 Dexterity-4 Constitution-5
    
    print("\n------------------------ CHARACTER SHEET ------------------------")
    print(f"Name: {name}\t\tClass: {class_dnd}\t\tLevel: {1}")
    print("------------------------------------------------------------------")
    print(f"Strength:     {abilityscore_list[0]} (+{abilitymod_list[0]})")
    print(f"Dexterity:    {abilityscore_list[4]} (+{abilitymod_list[4]})")
    print(f"Constitution: {abilityscore_list[5]} (+{abilitymod_list[5]})")
    print(f"Intelligence: {abilityscore_list[3]} (+{abilitymod_list[3]})")
    print(f"Wisdom:       {abilityscore_list[2]} (+{abilitymod_list[2]})")
    print(f"Charisma:     {abilityscore_list[1]} (+{abilitymod_list[1]})")
    print("------------------------------------------------------------------")
    print(f"Health: {health}")
    print("---------------------------Weapons & Items------------------------")
    for weapon in weaponlist:
        print(weaponlist)


    user_input = input("Would you like to import this into a .txt file? (y/n) ").lower()
    if user_input == "y":
        filename = input("What would you like to name the file? Please type '.txt' at the end of the choosen name. ")
        txtdoc(abilitymod_list, abilityscore_list, health, class_dnd, name, filename)
    elif user_input == "n": 
        startover_input = input("Would you like to make another character? (y/n)").lower()
        if startover_input == "y":
            welcome()
        else:
            print('Thank you!')
    

def txtdoc(abilitymod_list, abilityscore_list, health, class_dnd, name, filename="character_sheet.txt"):
    try:
        # Get the current working directory
        current_directory = os.getcwd()

        # Create the full file path
        full_path = os.path.join(current_directory, filename)

        # Add ".txt" extension if not present in the filename
        if not filename.endswith(".txt"):
            full_path += ".txt"

        with open(full_path, 'w') as file:
            character_sheet = "\n------------------------ CHARACTER SHEET ------------------------\n"
            character_sheet += f"Name: {name}\t\tClass: {class_dnd}\t\tLevel: 1\n"
            character_sheet += "------------------------------------------------------------------\n"
            character_sheet += f"Strength:     {abilityscore_list[0]} (+{abilitymod_list[0]})\n"
            character_sheet += f"Dexterity:    {abilityscore_list[4]} (+{abilitymod_list[4]})\n"
            character_sheet += f"Constitution: {abilityscore_list[5]} (+{abilitymod_list[5]})\n"
            character_sheet += f"Intelligence: {abilityscore_list[3]} (+{abilitymod_list[3]})\n"
            character_sheet += f"Wisdom:       {abilityscore_list[2]} (+{abilitymod_list[2]})\n"
            character_sheet += f"Charisma:     {abilityscore_list[1]} (+{abilitymod_list[1]})\n"
            character_sheet += "------------------------------------------------------------------\n"
            character_sheet += f"Health: {health}\n"
            character_sheet += "------------------------------------------------------------------\n"
            file.write(character_sheet)
        
        print(f"Congrats on finishing your character! {filename} should be in {full_path}, good luck finding it!\n\n")
        
        userinput = input("To go back to the main menu please type 'M' and hit enter and to quit please type 'Q' and hit enter.").lower
        if userinput == "m":
            print(f"--------Loading--------\n\n")
            welcome()
        elif userinput == "q":
            print(f"goodbye")
            exit()
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
    

        
def weaponselection(class_dnd):
    
   

    # Weapon list
    weapon_list = []

    print("Welcome to the Weapon Selection part of the process.")
    print("------------------------------------------------------")

    
    if class_dnd == "Paladin":
        userinput = input("Please (a) choose a martial weapon and a shield or (b) choose two martial weapons: ").lower()

        if userinput == "a":
            print("Name\t\tCost\t\tDamage\t\tWeight\t\tProperties")
            print("--------------------------------------------------------------")
            for weapon in library_dnd.simpweapons_martial:
                print(f"{weapon['name']}\t\t{weapon['cost']}\t\t{weapon['damage']}\t\t{weapon['weight']}\t\t{', '.join(weapon['properties'])}")

            weapon_input = input("Please select one weapon: ")
            
            selected_weapon = next((w for w in library_dnd.simpweapons_martial if w['name'] == weapon_input), None)
            if selected_weapon:
                weapon_list.append(selected_weapon)
            else:
                print("Invalid weapon selection.")
                return None
            
            # Append "Shield" to the list
            weapon_list.append("Shield")

        elif userinput == "b":
            print("Name\t\tCost\t\tDamage\t\tWeight\t\tProperties")
            print("--------------------------------------------------------------")
            for weapon in library_dnd.simpweapons_martial:
                print(f"{weapon['name']}\t\t{weapon['cost']}\t\t{weapon['damage']}\t\t{weapon['weight']}\t\t{', '.join(weapon['properties'])}")

            first_weapon_input = input("Please select first weapon: ")
            second_weapon_input = input("Please select second weapon: ")
            
            # Search for the selected weapons in the dictionary
            selected_first_weapon = next((w for w in library_dnd.simpweapons_martial if w['name'] == first_weapon_input), None)
            selected_second_weapon = next((w for w in library_dnd.simpweapons_martial if w['name'] == second_weapon_input), None)

            if selected_first_weapon and selected_second_weapon:
                weapon_list.append(selected_first_weapon)
                weapon_list.append(selected_second_weapon)
            else:
                print("Invalid weapon selection.")
                return None

    elif class_dnd == "Fighter":
        userinput = input("Please (a) choose a martial weapon and a shield or (b) choose two martial weapons: ").lower()

        if userinput == "a":
            print("Name\t\tCost\t\tDamage\t\tWeight\t\tProperties")
            print("--------------------------------------------------------------")
            for weapon in library_dnd.simpweapons_martial:
                print(f"{weapon['name']}\t\t{weapon['cost']}\t\t{weapon['damage']}\t\t{weapon['weight']}\t\t{', '.join(weapon['properties'])}")

            weapon_input = input("Please select one weapon: ")
        
            # Search for the selected weapon in the dictionary
            selected_weapon = next((w for w in library_dnd.simpweapons_martial if w['name'] == weapon_input), None)
            if selected_weapon:
                weapon_list.append(selected_weapon)
            else:
                print("Invalid weapon selection.")
                return None
            
            # Append "Shield" to the list
            weapon_list.append("Shield")

        elif userinput == "b":
            print("Name\t\tCost\t\tDamage\t\tWeight\t\tProperties")
            print("--------------------------------------------------------------")
            for weapon in library_dnd.simpweapons_martial:
                print(f"{weapon['name']}\t\t{weapon['cost']}\t\t{weapon['damage']}\t\t{weapon['weight']}\t\t{', '.join(weapon['properties'])}")

            first_weapon_input = input("Please select first weapon: ")
            second_weapon_input = input("Please select second weapon: ")
            
            # Search for the selected weapons in the dictionary
            selected_first_weapon = next((w for w in library_dnd.simpweapons_martial if w['name'] == first_weapon_input), None)
            selected_second_weapon = next((w for w in library_dnd.simpweapons_martial if w['name'] == second_weapon_input), None)

            if selected_first_weapon and selected_second_weapon:
                weapon_list.append(selected_first_weapon)
                weapon_list.append(selected_second_weapon)
            else:
                print("Invalid weapon selection.")
                return None

        userinput = input("Please choose between (a) a light crossbow and 20 bolts or (b) two handaxes").lower()
        print("Name\t\tCost\t\tDamage\t\tWeight\t\tProperties")
        print("--------------------------------------------------------------")
        print(f"{library_dnd.simpweapons_ranged[0]}")
        print(f"{library_dnd.simpweapons_melee[3]}")
        
        if userinput == "a":
            
            weapon_list.append(f"{library_dnd.simpweapons_ranged[0]}")
        
        elif userinput == "b":
            
            weapon_list.append(f"{library_dnd.simpweapons_melee[3]}")
            weapon_list.append(f"{library_dnd.simpweapons_melee[3]}")

        
    

    

# LET'S GOOOOO
welcome()
