

user_hp = 5
user_dmg = 1
user_def = 0
hp_elixir = 5


enemy_hp = 3
enemy_dmg = 1
enemy_def = 0

# user attacking enemy


def use_elixir():
    global hp_elixir

    if user_hp <= 5 and hp_elixir >= 0:
        hp_elixir -= 1
        user_hp == 5
    else:
        print("You are out of elixirs! Find the right choise to gain more elixirs!")


def attack_user():
    global enemy_hp
    global enemy_def

    if enemy_def <= 0:
        enemy_hp -= 1
    else:
        enemy_def -= 1

# enemy attacking user


def attack_enemy():
    global user_hp
    global user_def

    if user_def <= 0:
        user_hp -= 1
    else:
        user_def -= 1


# game intro dialoque
start_game = input(
    "Welcome hero! Do you want to start an adventure? Type 'yes' to start or 'quit' to quit: ").lower()
if start_game == "yes":
    user_name = input("Great! Let´s start with your name: ")
else:
    quit()

print(f"So, {user_name}. We need your help finding the Treasure.")

user_weapon = input(
    "But first pick up the weapon of your choice! Type 'sword' or 'hammer': ").lower()
if user_weapon == "sword" or user_weapon == "hammer":
    user_dmg += 1
    print(
        f"Great, you picked {user_weapon}. Now, it´s time to start your adventure!")
else:
    print("You failed to pick a weapon! You seem to be not ready for the adventure!")

user_choice = input(
    "After you traveled for a few hours you meet a old looking person. Do you want to talk to the stranger (y/n)? ").lower()
if user_choice == "y":
    user_choice = input(
        "Stranger: 'Hello young man. you look tired. Do you want to take a break?' Type (y/n)? ").lower()
    if user_choice == "y":
        print("The old man robbed you! You loose!")
        quit()
    else:
        print("The old man seems angry and tries to attack you!")
if user_choice == "n":
    print("The old man seems angry and tries to attack you!")
print("Attack first to surprise the old man!")

while enemy_hp > 0:
    attack_user()
    attack_enemy()
    if enemy_hp <= 0:
        print("Great! you won this battle.")
        enemy_hp == 3
    else:
        attack_user()
    if user_hp <= 0:
        print("You lost the Battle!")
        quit()
use_elixir()
print("After you won your first battle you decide to keep going to fulfill your quest!")
print(user_hp)
print(hp_elixir)
