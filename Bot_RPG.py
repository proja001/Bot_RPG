from random import randint

role = ''
roles = ["Mage","Warlock","Hunter","Warrior","Druid"]
mana_roles = ["Mage","Warlock","Druid"]

player_attributes = {}
monster_attributes = {}

player_damage = randint(0,15)
monster_damage = randint(0,10)
mana_consumption = randint(0,10)

monsters = ["Wolf","Bear","Zombie","Cyclops","Dracula"]
monster_attributes['HP'] = randint(0,100) 

monster_idx = randint(0,len(monsters))
random_monster = monsters[monster_idx]

player_attributes['HP'] = 100
player_attributes['Mana'] = 100

name = input("Enter your character name: ")
player_attributes['Name'] = name

while True:
    try:
        age = int(input("Enter your character's age: "))
    except ValueError:
        print("Please enter a valid age.")
        continue
    else:
        player_attributes['Age'] = age
        break

while role not in roles:
    try:
        print("Enter your character's role from the following list: ")
        print(*roles, sep = ", ")
        role = input()
    except:
        print("Please enter a valid role.")
        continue
    else:
        player_attributes['Role'] = role

print("Congradulations! You have created {0}.".format(player_attributes['Name']))

print("\nBeginning adventure....\n")

init_action = input("You have encountered a " + str(random_monster) + ". Would you like to fight (Y, N)? ").upper()

while init_action != 'Y' or init_action != 'N':
    if init_action == 'Y':
        print("You have chosen to fight " + str(random_monster))
        break
    elif init_action == 'N':
        print("You have chosen to abandon the fight.")
        break
    else:
        init_action = input("Please enter Y to fight or N to abandon the fight: ").upper()
if role in mana_roles:
    print("\n{0} | HP: {1} | Mana: {2}".format(player_attributes['Name'],player_attributes['HP'],player_attributes['Mana']))
else:
    print("\n{0} | HP: {1}".format(player_attributes['Name'],player_attributes['HP']))
print("\n{0} | HP: {1}".format(str(random_monster),str(monster_attributes['HP'])))

while True:
    action = input("Please enter Y to continue fight or N to abandon fight: ").upper()
    if action == 'Y':
        monster_attributes['HP'] = monster_attributes['HP'] - player_damage
        player_attributes['Mana'] = player_attributes['Mana'] - mana_consumption
        player_attributes['HP'] = player_attributes['HP'] - monster_damage
        if monster_attributes['HP'] > 0:
            print("\n{0} | HP: {1}".format(random_monster,str(monster_attributes['HP'])))
            print("\nYou have done " + str(player_damage) + " damage to " + str(random_monster))
            print("\nThe monster has done " + str(monster_damage) + " damage to " + str(player_attributes['Name']))
        elif monster_attributes['HP'] <= 0:
            monster_attributes['Name'] = random_monster
            print("\n{0} | HP: 0".format(monster_attributes['Name']))
            print("\nYou have defeated the monster!")
            break
        elif player_attributes['HP'] <= 0:
            player_attributes['Name'] = name
            print("\n{0} | HP: 0".format(player_attributes['Name']))
            print("\nYou have died. Game Over.")
            break
        #if role in mana_roles:
            #if player_attributes['HP'] > 0 and monster_attributes['HP'] > 0:
                #print("\n{0} | HP: {1} | Mana: {2}".format(player_attributes['Name'],player_attributes['HP'],player_attributes['Mana']))
            #elif player_attributes['HP'] <= 0 and monster_attributes['HP'] != 0:
                #print("\n{0} | HP: 0".format(player_attributes['Name']))
                #print("\nYou have died. Game Over.")
                #break
            #elif player_attributes['HP'] != 0 and monster_attributes['HP'] <= 0:
                #print("\n{0} | HP: 0".format(monster_attributes['Name']))
                #print("\nYou have defeated the monster!")
                #break
            #elif player_attributes['Mana'] <= 0 and monster_attributes['HP'] > 0 and player_attributes['HP'] > 0:
                #print("\nYou have ran out of mana. Please wait or use a mana potion to recover mana.")
                #break
        #elif role not in mana_roles:
        # if player_attributes['HP'] > 0 and monster_attributes['HP'] > 0:
        #     print("\n{0} | HP: {1}".format(player_attributes['Name'],player_attributes['HP']))
        # elif player_attributes['HP'] > 0 and monster_attributes['HP'] <= 0:
        #     monster_attributes['Name'] = random_monster
        #     print("\n{0} | HP: 0".format(monster_attributes['Name']))
        #     print("\nYou have defeated the monster!")
        #     break
        # elif player_attributes['HP'] <= 0 and monster_attributes['HP'] > 0:
        #     player_attributes['Name'] = name
        #     print("\n{0} | HP: 0".format(player_attributes['Name']))
        #     print("\nYou have died. Game Over.")
        #     break
    elif action == 'N':
        print("\nYou have chosen to abandon the fight.")
        break