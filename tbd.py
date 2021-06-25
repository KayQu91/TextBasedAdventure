class Hero:

    def __init__(self, hp, dmg, armor, elixir):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.elixir = elixir


hero = Hero(5, 0, 0, 5)
enemy = Hero(3, 0.5, 0, 0)
enemy_medium = Hero(3, 1, 0, 0)


def attack_hero():
    if enemy.hp > 0:
        enemy.hp -= hero.dmg


def attack_enemy():
    if hero.hp > 0:
        hero.hp -= enemy.dmg


def fight():
    while True:
        if enemy.hp > 0:
            print("Hero HP:", hero.hp, "Enemy HP:", enemy.hp)
            attack_hero()
            attack_enemy()
        if enemy.hp <= 0 and hero.hp > 0:
            print("You won this fight!")
            break
        if enemy.hp > 0 and hero.hp <= 0:
            print("You lost this fight!")
            quit()


# def use_elixir():
#     if hero.elixir > 0 and hero.hp < 5:
#         hero.elixir - 1 and hero.hp == 5
#     elif hero.elixir < 1:
#         print("You don´t have any elixirs left in your inventory!")
#     else:
#         print("You can´t use an elixir right now")


start_game = input(
    "Welcome hero! Do you want to start an adventure? Type 'yes' to start or 'quit' to quit: ").lower()
if start_game == "yes" or start_game == "y":
    user_name = input("Great! Let´s start with your name: ")
else:
    quit()

print(f"So, {user_name}. We need your help finding the Treasure.")

user_weapon = input(
    "But first pick up the weapon of your choice! Type 'Sword' or 'Hammer': ").lower()
if user_weapon == "sword":
    hero.dmg += 1
    print(
        f"Great, you picked {user_weapon}. Now, it´s time to start your adventure! \n")
elif user_weapon == "hammer":
    hero.dmg += 1
    print(
        f"Great, you picked {user_weapon}. Now, it´s time to start your adventure! \n")
else:
    print("You failed to pick a weapon! You lost!")
    quit()

user_choice = input(
    "After you traveled for a few hours you meet an old looking person. Do you want to talk to the stranger (y/n)? ").lower()
if user_choice == "y":
    user_choice = input(
        "Stranger: 'Hello young man. you look tired. Do you want to take a break?' Type (y/n)? ").lower()
    if user_choice == "y":
        print("The old man robbed you! You loose!")
        quit()
if user_choice == "n":
    print("The old man seems angry and tries to attack you!")
user_choice = input(
    "Do you want to fight the old man or run away? (fight/run) ").lower()
if user_choice == "fight":
    print("Attack the old man to knock him out!")
    fight()
    print("After this hard fight you should check for injuries and take a short break!")
else:
    print("Close call, but you could escape and continue your journey! \n")

print("You are traveling through nature until the sun slowly goes down. You need to find a place to rest and spend the night!")
user_choice = input(
    "Suddenly you see an old woman standing at the dark street. She looks nice and harmless. Do you want to talk to her? (y/n) ")
if user_choice == "y":
    user_choice = input(
        "Old woman: 'Hello young man. It looks like you´re from far away. The night is coming closer. Do you know where you could spend the night? (y/n) ")
    if user_choice == "n":
        print(
            "Old woman: 'Good for you, I have a free bed in our little motel not far away from here!")
    else:
        print("Old woman: 'Good for you! The nights are dangerous around here! Take care for yourself, young man! If you change our mind you know where you can find me.")
else:
    print("You walked past the old woman an keep searching for a nice place to spend the night.")
