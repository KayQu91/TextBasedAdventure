

# user stats
user_hp = 5
user_dmg = 1
user_def = 0

# enemy stats
enemy_hp = 3
enemy_dmg = 1
enemy_def = 0

# user attacking enemy


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
    "But first pick up the weapon of your choice! Type 'sword' or 'hammer': ").lower
