from GlobalImports import *
import msvcrt

def playerChoice(player: Character, enemies: list[Character]):
    print("What will you do? Attack, Defend, Special Attack? (A, D, S) ", end='', flush=True)
    key = msvcrt.getch().decode('utf-8').upper()
    print("\z" + " " * 50 + "\r", end='', flush=True) # clear the line

    match key:
        # attack
        case "A":
            player_weapon = player.weapon
            player_damage = player_weapon.attack             
            if len(enemies) > 1:
                while True:
                    enemyToAttack = input(f"Who will you attack? {', '.join([enemy.name for enemy in enemies])}")
                    if enemyToAttack in [enemy.name for enemy in enemies]:
                        print(f"You attack {enemyToAttack}.")
                        enemyToAttack = enemies[[enemy.name for enemy in enemies].index(enemyToAttack)]
                        break
                    else:
                        print(f"Invalid choice. Please choose again.")                    
            else:
                enemyToAttack = enemies[0]
                enemyToAttackIndex = 0
            damage_to_enemy = max(0, player_damage - enemies[0].defense)
            enemies[enemyToAttackIndex].base_health -= damage_to_enemy
            print(f"You attack {enemyToAttack.name} for {player_damage} damage. {enemyToAttack.name} defends for {enemyToAttack.defense} damage, taking {damage_to_enemy} damage.")
            if enemies[enemyToAttackIndex].base_health <= 0:
                print(f"{enemyToAttack.name} has been defeated!") if enemies.count > 1 else print(f"Last enemy, {enemyToAttack.name} has been defeated!")
            return enemyToAttack
        # defend
        case "D":
            print("You will defend against the enemy's attack.")
            enemyToAttack = enemies[randrange(0, len(enemies))]
            weapon = enemyToAttack.weapon
            damage = max(0, weapon.attack - player.defense)
            player.base_health -= damage
            print(f"{enemyToAttack.name} attacks you for {weapon.attack} damage. You defend for {player.defense} damage, taking {damage} damage.")
        # special attack
        case "S":
            player_special_attack = player.special_attack
            if enemies.count > 1:
                while True:
                    enemyToSpecialAttack = input(f"Who will you special attack? {', '.join([enemy.name for enemy in enemies])}")
                    if enemyToSpecialAttack in [enemy.name for enemy in enemies]:
                        print(f"You special attack {enemyToSpecialAttack}.")
                        enemyToSpecialAttack = enemies[[enemy.name for enemy in enemies].index(enemyToSpecialAttack)]
                        break
                    else:
                        print(f"Invalid choice. Please choose again.")
            else:
                enemyToSpecialAttack = enemies[0]
                damage_to_enemy = max(0, player_special_attack - enemies[enemyToSpecialAttack].defense)
                enemies[enemyToSpecialAttack].base_health -= damage_to_enemy
                print(f"You special attack {enemies[enemyToSpecialAttack].name} for {player_special_attack} damage. {enemies[enemyToSpecialAttack].name} defends for {enemies[enemyToSpecialAttack].defense} damage, taking {damage_to_enemy} damage.")
                return enemyToSpecialAttack
        # invalid choice
        case _:
            print("Invalid choice. Please choose again.")
            playerChoice(player, enemies)

def enemyChoice(player: Character, enemyToAct: Character):
    choices = ["attack", "special attack"]
    choice = choices[randrange(0, 1)]
    print(f"It is {enemyToAct.name}'s turn.")
    print(f"{enemyToAct.name} chooses to {choice}.")
    match choice:
        case "attack":
            enemy_weapon = enemyToAct.weapon
            damage = max(0, enemy_weapon.attack - player.defense)
            player.base_health -= damage
            print(f"{enemyToAct.name} attacks you for {enemy_weapon.attack} damage. You defend for {player.defense} damage, taking {damage} damage.")
        case "special attack":
            enemy_special_attack = enemyToAct.special_attack
            damage = max(0, enemy_special_attack - player.defense)
            player.base_health -= damage
            print(f"{enemyToAct.name} attacks you for {enemy_weapon.attack} damage. You defend for {player.defense} damage, taking {damage} damage.")
        case _:
            pass