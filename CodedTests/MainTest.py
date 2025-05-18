from GlobalImports import *

# a test file to try out running the combat functions

def runTests():
    myCharacter = Character(name="Austin", 
                            base_health=100, 
                            base_attack=10, 
                            special_attack=5, 
                            defense=10, 
                            speed=10, 
                            fruit_ability="none", 
                            haki_points=10, 
                            weapon=WeaponType.SWORD("Excalibur", 10, 10), 
                            hasHaki=False)
    
    enemy1 = Character(name="Bad guy number 1", 
                            base_health=100, 
                            base_attack=10, 
                            special_attack=5, 
                            defense=10, 
                            speed=10, 
                            fruit_ability="none", 
                            haki_points=10, 
                            weapon=WeaponType.SWORD("Big evil sword", 10, 10), 
                            hasHaki=False)
    enemies_list = [enemy1]


    runCombat(enemies= enemies_list,
                        player= myCharacter,
                        lose_Game_Over_Or_Restart= GameOver_Restart_Continue.GAME_OVER,
                        unlock_Haki_This_Fight= False)
runTests()