import unittest
from unittest.mock import patch, MagicMock
from GlobalImports import *
from Models.WeaponType import Sword

class Test_test_choices(unittest.TestCase):
    
    ##player choice tests
    #attack
    
    @patch('builtins.input', side_effect=["A", "Enemy1"])
    def test_playerChoice_attack(self, mock_input):
        player = MagicMock(spec=Character)
        player.weapon = Sword
        player.weapon.attack = 10
        player.defense = 5
        player.special_attack = 20
        player.base_health = 100

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.defense = 3
        enemy1.base_health = 30

        enemies = [enemy1]

        result = Choices.playerChoice(player, enemies)
        self.assertEqual(result, enemy1)
        self.assertEqual(enemy1.base_health, 23)

    #defend
    @patch('builtins.input', side_effect=["D"])
    @patch('Functions.Choices.randrange', return_value=0)
    def test_playerChoice_defend(self, mock_randrange, mock_input):
        player = MagicMock(spec=Character)
        player.weapon.value.return_value.attack = 10
        player.defense = 5
        player.special_attack = 20
        player.base_health = 100

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.weapon.value.return_value.attack = 8
        enemy1.defense = 3
        enemy1.base_health = 30

        enemies = [enemy1]

        Choices.playerChoice(player, enemies)
        self.assertEqual(player.base_health, 97)

    #special attack
    @patch('builtins.input', side_effect=["S", "Enemy1"])
    def test_playerChoice_special_attack(self, mock_input):
        player = MagicMock(spec=Character)
        player.weapon.value.return_value.attack = 10
        player.defense = 5
        player.special_attack = 20
        player.base_health = 100

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.defense = 3
        enemy1.base_health = 30

        enemies = [enemy1]

        result = Choices.playerChoice(player, enemies)
        self.assertEqual(result, enemy1)
        self.assertEqual(enemy1.base_health, 13)

    ##enemy choice tests
    #attack
    @patch('Functions.Choices.randrange', return_value=0)
    def test_enemyChoice_attack(self, mock_randrange):
        player = MagicMock(spec=Character)
        player.defense = 5
        player.base_health = 100

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.weapon.value.return_value.attack = 8
        enemy1.special_attack = 15

        Choices.enemyChoice(player, enemy1)
        self.assertEqual(player.base_health, 97)

    #special attack
    @patch('Functions.Choices.randrange', return_value=1)
    def test_enemyChoice_special_attack(self, mock_randrange):
        player = MagicMock(spec=Character)
        player.defense = 5
        player.base_health = 100

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.weapon.value.return_value.attack = 8
        enemy1.special_attack = 15

        Choices.enemyChoice(player, enemy1)
        self.assertEqual(player.base_health, 90)

if __name__ == '__main__':
    unittest.main()
