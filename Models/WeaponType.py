from GlobalImports import *
from enum import Enum

class Sword:
    def __init__(self, name: str = "Sword", attack: float = 10, speed: int = 10):
        self.name = name
        self.attack = attack
        self.speed = speed

class Gun:
    def __init__(self, name: str = "Gun", attack: float = 15, speed: int = 5):
        self.name = name
        self.attack = attack
        self.speed = speed

class Fist:
    def __init__(self, name: str = "Fist", attack: float = 5, speed: int = 15):
        self.name = name
        self.attack = attack
        self.speed = speed

class WeaponType(Enum):
    SWORD = Sword
    GUN = Gun
    FIST = Fist

    def __call__(self, name: str, attack: float, speed: int):
        return self.value(name, attack, speed)




