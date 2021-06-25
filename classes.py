if enemy.hp <=0:
    print("Voila")
elif hero.hp <=0:
    print("fckt that")

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
print("But at first you should check for any injuries!")
print(f"Your HP is {user_hp} and your armor ist {user_def}! And you got {hp_elixir} elixirs left!")
