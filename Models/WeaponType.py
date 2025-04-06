from GlobalImports import *

class Sword:
    def __init__(self, name: str, attack: float, speed: int):
        self.name = "Sword"
        self.attack = 10
        self.speed = 10

class Gun:
    def __init__(self, name: str, attack: float, speed: int):
        self.name = "Gun"
        self.attack = 15
        self.speed = 5

class Fist:
    def __init__(self, name: str, attack: float, speed: int):
        self.name = "Fist"
        self.attack = 5
        self.speed = 15

class WeaponType(Enum):
    SWORD = Sword
    GUN = Gun
    FIST = Fist




