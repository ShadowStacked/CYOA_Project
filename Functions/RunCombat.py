from Models.Character import * 
from Models.GameOver_Restart_Continue import * 
import Functions.Choices as Choices
from Functions.RunCombat import *
from CodedTests import *
import os

def runCombat(enemies: list[Character], player: Character, lose_Game_Over_Or_Restart: GameOver_Restart_Continue = GameOver_Restart_Continue.GAME_OVER, unlock_Haki_This_Fight: bool = False):

    # region copy variables for restart if needed    
    enemies_ForRestart = enemies
    player_ForRestart = player
    lose_Game_Over_Or_Restart_ForRestart= lose_Game_Over_Or_Restart
    unlock_Haki_This_Fight_ForRestart = unlock_Haki_This_Fight
    # endregion
    
    combatants_list = list(enemies)
    combatants_list.insert(0, player)
    endState = lose_Game_Over_Or_Restart
    playerMaxHealth = player.base_health
    print("Starting combat!")

    while player.base_health > 0 and len(combatants_list) > 1:              
        
        for combatant in combatants_list:
            
            # if combatant is player, run player choice function and get enemy to act on if player choses attack or special attack, if enemy is defeated remove from combatants list:
            if combatant.name == player.name:
                enemyToActOn = Choices.playerChoice(player, enemies)
                if enemyToActOn != None:
                    enemyToActOn = enemies[enemies.index(enemyToActOn)]
                    combatants_list.remove(enemyToActOn) if enemyToActOn.base_health <= 0 else None
                    
            else:
            # if combatant is enemy, run enemy choice function:
                Choices.enemyChoice(player, combatant)            
            
            # if combatant is enemy, check if enemy is defeated and remove from combatants list:
            if combatant.name != player.name and combatant.base_health <= 0:
                print(f"{combatant.name} has been defeated!") if combatants_list.count > 1 else print(f"Last enemy, {combatant.name} has been defeated!")
                combatants_list.remove(combatant)
            
            #if combatant is player, player has less than 20% of health and unlock haki is true, set player.hasHaki to true and end combat:
            if combatant.name == player.name and player.base_health <= playerMaxHealth * 0.2 and unlock_Haki_This_Fight == True:
                player.hasHaki = True
                print(f"{player.name} has unlocked Armament Haki and the enemy retreats!")
                return
            # if combatant is player and player is defeated, check if game over or restart:
            ## if game over, end combat and print game over message
            if combatant.name == player.name and player.base_health <= 0 and endState == GameOver_Restart_Continue.GAME_OVER:
                print(f"Game over! {player.name} has been defeated!")
                combatants_list.remove(player)
                return
            ## if restart, restart fight and print restart message
            elif combatant.name == player.name and player.base_health <= 0 and endState == GameOver_Restart_Continue.RESTART:
                print(f"{player.name} has been defeated! Restarting fight...")
                # restart fight
                runCombat(enemies_ForRestart, player_ForRestart, lose_Game_Over_Or_Restart_ForRestart, unlock_Haki_This_Fight_ForRestart)
