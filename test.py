import unittest
import game
# from Game_Project import game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game('Python Game Project - Chai Grindean',800, 800)
        self.player = game.Player('./Assets/player.png', 375, 700, 60, 60)
        self.enemy1 = game.Enemy('./Assets/monster4.png', 375, 700 , 75, 50, 7)
        self.chest = game.GameObject('./Assets/chest.png', 375, 25, 50, 50)

    def test_player_collision_with_enemy_should_return_game_over_true(self):
        # Arrange - Done in setUp()
        # Act
        actual = self.player.detect_collision(self.enemy1)
        # Assert
        self.assertTrue(actual)

    def test_player_no_collision_should_return_game_over_false(self):
        # Arrange - Done in setUp()
        # Act
        actual = self.player.detect_collision(self.chest)
        # Assert
        self.assertFalse(actual)

    def test_player_move_should_change_player_y_pos(self):
        # Arrange
        y_pos_before = self.player.y_pos
        # Act
        self.player.move(1, 800)
        actual = self.player.y_pos
        expected = y_pos_before < actual # When player moves up, y_pos decreases
        # Assert
        print('\ny_pos before: ', y_pos_before)
        print('\ny_pos after:', actual)
        self.assertNotEqual(y_pos_before, actual)

    def  tearDown(self):
        pass