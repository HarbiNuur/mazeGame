import pygame
import sys
import time


# Initialise Pygame
pygame.init()
# add event
keyPress = pygame.key.get_pressed
# Set up some constants
width = 900
height = 650
block_size = 65
# adding time for reading movement commands
clock = pygame.time.Clock()
vel = 5
# Create the screen
gameScreen = pygame.display.set_mode((width, height))
gameScreen.fill((128, 0, 128))  # purple background
pygame.display.set_caption("Welcome to the maze")

# Color library
white = (245, 245, 220)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (173, 216, 230)
orange = (255, 165, 0)
purple = (128, 0, 128)
pink = (255,192,203)

# Displaying messages for completing the levels etc
def textDisplay(text):
  renderFont = pygame.font.Font("freesansbold.ttf", 30)
  textsc = renderFont.render(text, True, black)
  surface, rect = textsc, textsc.get_rect()
  rect.center = ((width / 2), (height / 2))
  gameScreen.blit(surface, rect)
  pygame.display.update()
  


# Define classes
class GameEntity:
    def __init__(self, color, x_position, y_position):
        self.color = color
        self.x_position = x_position
        self.y_position = y_position


# want to make the player a different shape than the area so I made it a circle, I added x and y position to the player class
class Player(GameEntity):
    def __init__(
        self, color, radius, x_position, y_position, oldx_position, oldy_position, vel
    ):
        super().__init__(color, x_position, y_position)
        self.radius = radius
        self.oldx_position = oldx_position
        self.oldy_position = oldy_position
        self.vel = vel


def update_position(self, oldx_position, oldy_position):
    time.sleep(0.1)
    self.x_position = self.oldx_position
    self.y_position = self.oldy_position


class Wall(GameEntity):
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)


class Door(Wall):
    def __init__(sef, color, x_position, y_position):
        super().__init__(color, x_position, y_position)

class Exit(GameEntity):
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)


class Area(GameEntity):
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)


class Key(
    GameEntity,
):
    def __init__(self, color, x_position, y_position):
        super().__init__(color, x_position, y_position)


# Create instances
W = Wall(blue, 0, 0)
E = Exit(green, 0, 0)
S = Player(red, 10, 80, 80, 80, 80, 5)
O = Area(white, 0, 0)
P = Key(orange, 0, 0)
D = Door(black,0,0)
#


# Create maze maze1 and maze2 are the easy mazes
maze1 = [
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, O, O, O, O, O, O, O, O, W, O, O, O, W, W],
    [W, O, O, O, O, O, O, O, O, O, O, W, W, W, W],
    [W, O, W, W, W, W, W, W, O, W, O, O, O, O, W],
    [W, O, W, O, O, O, O, O, O, O, O, W, O, W, W],
    [W, O, W, O, W, W, W, W, O, W, W, W, W, W, W],
    [W, O, O, O, O, O, O, O, O, O, O, W, W, W, W],
    [W, W, W, W, W, W, W, W, O, W, O, O, W, O, W],
    [W, W, W, W, W, W, W, W, W, O, O, O, W, W, W],
    [W, W, W, W, W, W, W, W, W, E, W, W, W, W, W],
]

maze2 = [
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, O, O, O, W, W, W, W, W, W, W, W, W, O, W],
    [W, O, W, O, W, O, O, O, O, O, O, O, W, O, W],
    [W, O, W, O, W, W, W, W, W, W, W, W, W, O, W],
    [W, O, W, O, W, W, O, O, O, O, O, O, O, O, W],
    [W, O, W, O, W, O, W, O, W, O, W, W, W, W, W],
    [W, O, W, O, W, O, O, O, O, O, W, O, O, O, W],
    [W, O, W, O, W, O, W, W, W, O, W, O, W, O, W],
    [W, O, W, O, O, O, O, O, O, O, W, O, O, O, W],
    [W, E, W, W, W, W, W, W, W, W, W, W, W, W, W],
]

# maze 3 and maze 4 are the hard mode mazes, in this mode they need to find a key
maze3 = [
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, O, W, W, O, O, O, O, O, O, O, O, O, W],
    [W, W, O, W, W, W, W, W, O, O, W, W, O, W, W],
    [W, O, O, O, O, O, O, O, O, W, O, O, O, W, W],
    [W, W, O, W, W, W, O, W, O, W, O, W, O, W, W],
    [W, W, O, W, W, W, O, W, O, W, O, W, D, E, W],
    [W, W, O, W, O, O, O, W, W, O, O, W, W, W, W],
    [W, W, W, W, O, W, O, W, O, O, W, W, O, W, W],
    [W, W, O, P, O, W, O, O, O, W, W, W, O, W, W],
    [W, W, W, W, W, W, W, W, W, W, W, O, O, W, W],
]
maze32 = [
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, O, W, W, O, O, O, O, O, O, O, O, O, W],
    [W, W, O, W, W, W, W, W, O, O, W, W, O, W, W],
    [W, O, O, O, O, O, O, O, O, W, O, O, O, W, W],
    [W, W, O, W, W, W, O, W, O, W, O, W, O, W, W],
    [W, W, O, W, W, W, O, W, O, W, O, W, O, E, W],
    [W, W, O, W, O, O, O, W, W, O, O, W, W, W, W],
    [W, W, W, W, O, W, O, W, O, O, W, W, O, W, W],
    [W, W, O, P, O, W, O, O, O, W, W, W, O, W, W],
    [W, W, W, W, W, W, W, W, W, W, W, O, O, W, W],
]
maze4 = [[W, W, W ,W ,W ,W ,W ,W ,W, W, E, W, W ,W ,W],
        [W, W, W, O, O, W, W, W, O, W, D, W, W, W, W,],
        [W, O, O, O ,O ,W ,O ,W ,O, W, O, O, O ,W ,W,],
        [W, W, O ,W ,W ,W ,O ,W ,W ,W, O ,W ,O ,W ,W,],
        [W, O, P ,O, O, O ,W ,W ,W ,O, O ,W ,O ,O ,W,],
        [W, O, W, W, W, W, O, W, W ,O, W ,O ,O ,O ,W,],
        [W, O ,O ,O, O ,O ,O ,O ,O ,O ,W, W ,W ,W ,W,],
        [W, O, O ,W ,W ,W ,W ,W ,W ,O ,W ,W ,O ,O ,W,],
        [W, O, O ,W ,O ,O ,O ,W ,W ,O ,O ,O ,O ,W ,W,],
        [W, W, W, W ,W ,W ,W ,W ,W ,W ,W ,W ,W ,W ,W ],]

maze42 = [[W, W, W ,W ,W ,W ,W ,W ,W, W, E, W, W ,W ,W],
        [W, W, W, O, O, W, W, W, O, W, O, W, W, W, W,],
        [W, O, O, O ,O ,W ,O ,W ,O, W, O, O, O ,W ,W,],
        [W, W, O ,W ,W ,W ,O ,W ,W ,W, O ,W ,O ,W ,W,],
        [W, O, P ,O, O, O ,W ,W ,W ,O, O ,W ,O ,O ,W,],
        [W, O, W, W, W, W, O, W, W ,O, W ,O ,O ,O ,W,],
        [W, O ,O ,O, O ,O ,O ,O ,O ,O ,W, W ,W ,W ,W,],
        [W, O, O ,W ,W ,W ,W ,W ,W ,O ,W ,W ,O ,O ,W,],
        [W, O, O ,W ,O ,O ,O ,W ,W ,O ,O ,O ,O ,W ,W,],
        [W, W, W, W ,W ,W ,W ,W ,W ,W ,W ,W ,W ,W ,W ],]

# Draw the maze, # I had to expand this code so that the player can be spawned
# to a different shape to the rest of the blocks. The player is now a circle and everything else are rectangles
def renderMaze(maze):
    for y, row in enumerate(maze):
      for x, block in enumerate(row):
       pygame.draw.rect(
        gameScreen, block.color,
        pygame.Rect(x * block_size, y * block_size, block_size, block_size))
#define Key change
def keyChange1():
  textDisplay("The door has now been unlocked!") 
  time.sleep(2)
  gameScreen.fill(white) 
  renderMaze(maze32)
def keyChange2():
  textDisplay("The door has now been unlocked!") 
  time.sleep(2)
  gameScreen.fill(white) 
  renderMaze(maze42)
#define gameEndings
def gameEnd1():
  textDisplay("Get ready for the next level in 5 seconds!")
  time.sleep(5)
  gameScreen.fill(white) 
  renderMaze(maze2)
#This is for the hard mode maze, it will open maze 4 instead of maze 2
def gameEnd2():
    textDisplay("You have beaten Easy mode! Hard mode will now commence")
    time.sleep(5)
    gameScreen.fill(white)
    renderMaze(maze3)
#this should occur for the final level so for maze 2 and maze 4. The game exits
def gameEnding():
    textDisplay("You have beaten the game! The game will now exit")
    time.sleep(5)
    pygame.quit()
    sys.exit()


current_maze = maze1

if current_maze == maze1:
    S = Player(red,10,80,80,80,80,5)
else:
    pass
if current_maze == maze2:
    S = Player(red,10,860,80,860,90,5)
else:
  pass
if current_maze == maze3:
  S = Player(red,10,160,80,160,80,5)
else:
  pass
if current_maze == maze4:
  S = Player(red,10,860,300,860,300,5)
else:
  pass
  
#Main game loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Save the old position
    old_x = S.x_position
    old_y = S.y_position

    # Update the position based on user input
    S.x_position += (keys[pygame.K_d] - keys[pygame.K_a]) * vel
    S.y_position += (keys[pygame.K_s] - keys[pygame.K_w]) * vel

    # Check for collisions with walls
    new_block_x = int(S.x_position) // block_size
    new_block_y = int(S.y_position) // block_size

    if isinstance(current_maze[new_block_y][new_block_x], Wall):
        # If a wall is detected, restore the old position
        S.x_position = old_x
        S.y_position = old_y
  
  #check for the key in maze 3 and maze 4
    if isinstance(current_maze[new_block_y][new_block_x], Key):
      if current_maze == maze3:
        keyChange1()
        current_maze = maze32
      elif current_maze == maze4:
         keyChange2()
         current_maze = maze42

    # If the player reaches the exit
    if isinstance(current_maze[new_block_y][new_block_x], Exit):
        if current_maze == maze1:
            gameEnd1()
            current_maze = maze2
            S.x_position, S.y_position = 860, 80  # Move player to starting position of maze2
        elif current_maze == maze2:
            gameEnd2()
            current_maze =  maze3
            S.x_position, S.y_position = 160, 80  # Move player to starting position of maze2
        elif current_maze == maze32:
            gameEnd1()
            current_maze = maze4
            S.x_position, S.y_position = 860, 300  # Move player to starting position of maze4
        elif current_maze == maze42:
            gameEnding()

    gameScreen.fill(white)  # Clears the screen.
    renderMaze(current_maze)
    pygame.draw.circle(
        gameScreen, S.color, (int(S.x_position), int(S.y_position)), 10, 0
    )  # This makes the player visibly move
    pygame.display.flip()  # Update the display.

pygame.quit()
sys.exit()
