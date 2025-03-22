# import keyboard
import os
from sys import stdout
from time import sleep 
import re

player_name = []

def slow(text, delay=0.03):
    if text: # only process if the string is not zero length
        for c in text:
            print(c, end='', flush=True)
            sleep(delay)
        if text[-1] != '\n':
            print()

title = """
 ██████╗ ███╗   ██╗███████╗    ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗
██╔═══██╗████╗  ██║██╔════╝    ██╔══██╗██║   ██║████╗  ██║██║ ██╔╝
██║   ██║██╔██╗ ██║█████╗      ██████╔╝██║   ██║██╔██╗ ██║█████╔╝ 
██║   ██║██║╚██╗██║██╔══╝      ██╔═══╝ ██║   ██║██║╚██╗██║██╔═██╗ 
╚██████╔╝██║ ╚████║███████╗    ██║     ╚██████╔╝██║ ╚████║██║  ██╗
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
"""

print(title)

while True:
    player_name = input("What is your name?\n").strip()
    
    if player_name and re.match("^[A-Za-z-' ]+$", player_name):  
        break  # Valid name entered, exit loop
    print("Try again. Please enter a valid name (letters, hyphens, and apostrophes only).")


os.system('cls' if os.name == 'nt' else 'clear')

print("The small and quiet rock in the middle of the ocean known as Duck Island was where you were born.\n")
print("This small island on the East Blue usually birthed fishermen, salt miners, and the occasional Marine.\n")
print("Marine ships would often dock here just long enough to resupply before heading back out again.\n")
print("To them, Duck Island was a dot on a map. A quick stop to get some food and have fun with the local girls.\n")
print("To you, every passing ship made you long for the open seas. To dive head first into freedom and leave your predetermined life behind. To be anything you wanted to be.")
input("\nPress Enter to continue...") 

os.system('cls' if os.name == 'nt' else 'clear')
print("The years pass by and you find yourself in your local bar again.\n")
print("The redness in your face that once went away after a night of sleep seems to linger longer and longer.\n")
input("Press Enter to continue...")

os.system('cls' if os.name == 'nt' else 'clear')
slow("Let me go!")
input("Press Enter to continue...")

os.system('cls' if os.name == 'nt' else 'clear')
print("\nYou turn your head.\n")
print("You see one of the local Marines harrassing one of the bar maids.\n")
print("What was her name again?\n")
print("You can't remember.\n")
print("Your body moves before your mind. It must be the liquor.")
print("You voice slurs as you yell out.\n")
input("Press Enter to continue...")

os.system('cls' if os.name == 'nt' else 'clear')
slow("g....GEEEET AwwwaaY!\n")
input("Press Enter to continue...")

# os.system('cls' if os.name == 'nt' else 'clear')
