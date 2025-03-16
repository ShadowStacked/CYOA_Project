from Models import WeaponType


class Character:
    def __init__(self, name: str, base_health: float, base_attack: float, special_attack: float, defense: float, speed: int, fruit_ability: str, haki_points: int, weapon: WeaponType):
        self.name = name
        self.base_health = base_health
        self.base_attack = base_attack
        self.special_attack = special_attack
        self.defense = defense
        self.speed = speed
        self.fruit_ability = fruit_ability
        self.haki_points = haki_points
        self.weapon = weapon
