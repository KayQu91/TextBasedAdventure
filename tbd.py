class Hero:

    def __init__(self, hp, dmg, armor, elixir):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.elixir = elixir


hero = Hero(5, 0, 0, 5)
enemy = Hero(3, 0.5, 0, 0)
# enemy_medium = Hero(3, 1, 0, 0)


def attack_enemy():
    while True:
        if hero.hp > 0:
            print("Hero HP:", hero.hp)
            hero.hp -= enemy.dmg
            print("Hero HP:", hero.hp)
        else:
            break


def attack_hero():
    while True:
        if enemy.hp > 0:
            print("Enemy HP:", enemy.hp)
            enemy.hp -= hero.dmg
            print("Enemy HP:", enemy.hp)
        else:
            break


def use_elixir():
    if hero.elixir > 0 and hero.hp <= 2:
        hero.elixir - 1 and hero.hp == 5
    elif hero.elixir < 1:
        print("You don´t have any elixirs left in your inventory!")
    else:
        print("You can´t use an elixir right now")

while True:
    start_game = input(
        "Welcome hero! Do you want to start an adventure? Type 'yes' to start or 'quit' to quit: ").lower()
    if start_game == "yes" or start_game == "y":
        user_name = input("Great! Let´s start with your name: ")
    elif start_game == "q" or start_game == "quit":
        quit()
    else:
        print("Please, type 'yes' or 'quit'!")

print(f"So, {user_name}. We need your help finding the Treasure.")

user_weapon = input(
    "But first pick up the weapon of your choice! Type 'Sword' or 'Hammer': ").lower()
if user_weapon == "sword":
    hero.dmg += 1
    hero.armor += 1
    print(
        f"Great, you picked {user_weapon}. Now, it´s time to start your adventure!")
elif user_weapon == "hammer":
    hero.dmg += 1.5
    hero.armor += 0.5
    print(
        f"Great, you picked {user_weapon}. Now, it´s time to start your adventure!")
else:
    print("You failed to pick a weapon! You lost!")
    quit()

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
user_choice = input(
    "Do you want to fight the old man or run away? (fight/run) ").lower()
if user_choice == "fight":
    print("Attack the old man to knock him out!")
    while True:
        if enemy.hp > 0:
            attack_hero()
            attack_enemy()
            print(hero.hp, enemy.hp, hero.armor)
        elif hero.hp <= 0:
            print("Wasted!")
            quit()
else:
    print("Close call, but you could escape and continue your journey!")
