import pygame

# Game Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CLOCK = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('opensans', 75)

class Game:
    WHITE_COLOR = (255, 255, 255)
    BLACK_COLOR = (0, 0, 0)
    REFRESH_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(Game.WHITE_COLOR)
        pygame.display.set_caption(title)

    def collision_logic(self, game_over: bool, player_win: bool):
        if game_over and player_win:
            text = FONT.render('You Won!', True, Game.BLACK_COLOR)
        elif game_over and player_win == False:
            text = FONT.render('You lost ...', True, Game.BLACK_COLOR)
        self.game_screen.blit(text, (300, 350))
        pygame.display.update()
        CLOCK.tick(1)

    def run_game_loop(self):
        game_over = False
        player_win = False
        direction = 0
        player = Player('./Assets/player.png', 375, 700, 60, 60)
        enemy1 = Enemy('./Assets/monster4.png', 20, 580 , 75, 50, 7)
        enemy2 = Enemy('./Assets/monster3.png', 20, 365 , 75, 50, 10)
        enemy3 = Enemy('./Assets/monster2.png', 20, 150 , 75, 75, 12)
        chest = GameObject('./Assets/chest.png', 375, 25, 50, 50)
        background = GameObject('./Assets/background.png', 0, 0, 800, 800)
        while not game_over:
            # List of events (actions performed by user such as clicks and key presses)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    # Detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                    # Detect when key is released
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)
            
            # Refresh Game Screen before drawing player
            self.game_screen.fill((110, 159, 211))
            background.draw(self.game_screen)
            chest.draw(self.game_screen)
            # Update Game Object positions and redraw
            player.move(direction, self.height)
            player.draw(self.game_screen)
            enemy1.move(self.width)
            enemy1.draw(self.game_screen)
            enemy2.move(self.width)
            enemy2.draw(self.game_screen)
            enemy3.move(self.width)
            enemy3.draw(self.game_screen)
            # Check for Collisions between enemies and goal
            if player.detect_collision(enemy1):
                game_over = True
                player_win = False
                self.collision_logic(game_over, player_win)
                break
            elif player.detect_collision(enemy2):
                game_over = True
                player_win = False
                self.collision_logic(game_over, player_win)
                break
            elif player.detect_collision(enemy3):
                game_over = True
                player_win = False
                self.collision_logic(game_over, player_win)
                break
            elif player.detect_collision(chest):
                game_over = True
                player_win = True
                self.collision_logic(game_over, player_win)
                break
            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            CLOCK.tick(Game.REFRESH_RATE)
        # Play again if the player won
        if player_win != True:
            self.run_game_loop()
        else:
            return

# GameObject is the parent class for the player, background, and treasure object
class GameObject:

    def __init__(self, image_file, x, y, width, height):
        object_image = pygame.image.load(image_file)
        # Scale image up
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        # 'Blit' the image on the background, at the position in the tuple
        background.blit(self.image, (self.x_pos, self.y_pos))

class Player(GameObject):
    SPEED = 10

    def __init__(self, image_file, x, y, width, height):
        super().__init__(image_file, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= Player.SPEED
        elif direction < 0:
            self.y_pos += Player.SPEED
        # Lower Screen Limit
        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50
        # Upper Screen Limit
        elif self.y_pos <= 20:
            self.y_pos = 20
    
    def detect_collision(self, other_body: GameObject):
        # Return false if player is above or below the enemy (since we can't ever hit them)
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        
        # Return false if player is too far to the right or left of enemy
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.height < other_body.x_pos:
            return False
        
        # If every check passes, then there must be collision
        return True

class Enemy(GameObject):

    def __init__(self, image_file, x, y, width, height, speed):
        super().__init__(image_file, x, y, width, height)
        self.speed = speed
    
    def move(self, max_width):
        # Left side screen limit
        if self.x_pos <= 0:
            self.speed = abs(self.speed)
        # Right side screen limit
        elif self.x_pos >= max_width - 75:
            self.speed = -abs(self.speed)
        # Keep moving
        self.x_pos += self.speed

# Start Game
if __name__ == "__main__":
    pygame.init()
    game = Game('Python Game Project - Chai Grindean',SCREEN_WIDTH, SCREEN_HEIGHT)
    game.run_game_loop()
    # End Game
    pygame.quit()
    quit()
