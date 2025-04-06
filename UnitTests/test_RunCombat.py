import unittest
from unittest.mock import patch, MagicMock
from Functions.RunCombat import runCombat
from GlobalImports import *
from Models.WeaponType import Sword

class Test_test_runCombat(unittest.TestCase):
    @patch('Functions.Choices.playerChoice', return_value=0)
    @patch('Functions.Choices.enemyChoice')
    def test_runCombat_player_wins(self, mock_enemyChoice, mock_playerChoice):
        player = MagicMock(spec=Character)
        player.name = 'Player'
        player.base_health = 100
        player.hasHaki = False
        player.weapon = WeaponType.SWORD
        player.defense = 5
        player.special_attack = 20

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.base_health = 30
        enemy1.defense = 3

        enemies = [enemy1]

        runCombat(enemies, player)

        self.assertTrue(player.base_health > 0)
        self.assertEqual(len(enemies), 0)

    @patch('Functions.Choices.playerChoice', return_value=None)
    @patch('Functions.Choices.enemyChoice')
    def test_runCombat_player_loses(self, mock_enemyChoice, mock_playerChoice):
        player = MagicMock(spec=Character)
        player.name = 'Player'
        player.base_health = 1
        player.hasHaki = False
        player.weapon = WeaponType.SWORD
        player.defense = 5
        player.special_attack = 20

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.base_health = 30
        enemy1.defense = 3

        enemies = [enemy1]

        with patch('builtins.print') as mocked_print:
            runCombat(enemies, player, GameOver_Restart_Continue.GAME_OVER, unlock_Haki_This_Fight=False)
            mocked_print.assert_any_call("Game over! Player has been defeated!")

    @patch('Functions.Choices.playerChoice', return_value=None)
    @patch('Functions.Choices.enemyChoice')
    def test_runCombat_player_unlocks_haki(self, mock_enemyChoice, mock_playerChoice):
        player = MagicMock(spec=Character)
        player.name = 'Player'
        player.base_health = 10
        player.hasHaki = False
        player.weapon = WeaponType.SWORD
        player.defense = 5
        player.special_attack = 20

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.base_health = 30
        enemy1.defense = 3

        enemies = [enemy1]

        with patch('builtins.print') as mocked_print:
            runCombat(enemies, player, unlock_Haki_This_Fight=True)
            self.assertTrue(player.hasHaki)
            mocked_print.assert_any_call("Player has unlocked Armament Haki and the enemy retreats!")

    @patch('Functions.Choices.playerChoice', return_value=None)
    @patch('Functions.Choices.enemyChoice')
    def test_runCombat_restart(self, mock_enemyChoice, mock_playerChoice):
        player = MagicMock(spec=Character)
        player.name = 'Player'
        player.base_health = 1
        player.hasHaki = False
        player.weapon = WeaponType.SWORD
        player.defense = 5
        player.special_attack = 20

        enemy1 = MagicMock(spec=Character)
        enemy1.name = 'Enemy1'
        enemy1.base_health = 30
        enemy1.defense = 3

        enemies = [enemy1]

        with patch('builtins.print') as mocked_print:
            with patch('Functions.RunCombat.runCombat') as mock_runCombat:
                mock_runCombat.side_effect = runCombat
                runCombat(enemies, player, lose_Game_Over_Or_Restart=GameOver_Restart_Continue.RESTART)
                mocked_print.assert_any_call("Player has been defeated! Restarting fight...")
                self.assertTrue(mock_runCombat.called)

if __name__ == '__main__':
    unittest.main()
