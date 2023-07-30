import pygame
import sys

# Initialise Pygame
pygame.init()
# add event
keyPress = pygame.key.get_pressed
# Set up some constants
width = 900
height = 650
block_size = 65
#adding time for reading movement commands
clock = pygame.time.Clock()
vel = 5
# Create the screen
gameScreen = pygame.display.set_mode((width, height))
gameScreen.fill((0, 0, 0))  # black background
pygame.display.set_caption("Welcome to the maze")

# Color library
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255,165,0)
purple = (128,0,128)

# Define classes


class GameEntity:

  def __init__(self, color,x_position,y_position):
    self.color = color
    self.x_position = x_position
    self.y_position = y_position

#want to make the player a different shape than the area so I made it a circle, I added x and y position to the player class
class Player(GameEntity):

  def __init__(self, color, radius,x_position,y_position,oldx_position,oldy_position,vel):
    super().__init__(color,x_position,y_position)
    self.radius = radius
    self.oldx_position = oldx_position
    self.oldy_position = oldy_position
    self.vel = vel
    


class Wall(GameEntity):

  def __init__(self, color,x_position,y_position):
    super().__init__(color,x_position,y_position)

class Door(Wall):
  def __init__(sef,color,x_position,y_position):
    super().__init__(color,x_position,y_position)


class Exit(GameEntity):

  def __init__(self, color,x_position,y_position):
    super().__init__(color,x_position,y_position)


class Area(GameEntity):

  def __init__(self, color,x_position,y_position):
    super().__init__(color,x_position,y_position)

class Key(GameEntity,):
  def __init__(self,color,x_position,y_position):
    super().__init__(color,x_position,y_position)

# Create instances
W = Wall(black,0,0)
E = Exit(green,0,0)
S = Player(blue,10,0,0,0,0,5) 
O = Area(white,0,0)
P = Key (orange,0,0)

#


# Create maze maze1 and maze2 are the easy mazes
maze1 = [[W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
         [W, O, O, O, O, O, O, O, O, W, O, O, O, W, W],
         [W, S, O, O, O, O, O, O, O, O, O, W, W, W, W],
         [W, O, W, W, W, W, W, W, O, W, O, O, O, O, W],
         [W, O, W, O, O, O, O, O, O, O, O, W, O, W, W],
         [W, O, W, O, W, W, W, W, O, W, W, W, W, W, W],
         [W, O, O, O, O, O, O, O, O, O, O, W, W, W, W],
         [W, W, W, W, W, W, W, W, O, W, O, O, W, O, W],
         [W, W, W, W, W, W, W, W, W, O, O, O, W, W, W],
         [W, W, W, W, W, W, W, W, W, E, W, W, W, W, W]]

maze2 = [[W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
         [W, O, O, O, W, W, W, W, W, W, W, W, W, O, W],
         [W, O, W, O, W, O, O, O, O, O, O, O, W, O, W],
         [W, O, W, O, W, W, W, W, W, W, W, W, W, O, W],
         [W, O, W, O, W, W, O, O, O, O, O, O, O, O, W],
         [W, O, W, O, W, O, W, O, W, O, W, W, W, W, W],
         [W, O, W, O, W, O, O, O, O, O, W, O, O, O, W],
         [W, O, W, O, W, O, W, W, W, O, W, O, W, O, W],
         [W, O, W, O, O, O, O, O, O, O, W, O, O, O, W],
         [W, E, W, W, W, W, W, W, W, W, W, W, W, W, W],]

#maze 3 and maze 4 are the hard mode mazes, in this mode they need to find a key
maze3=  [[W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
        [W, W, O, W, W, O, O, O, O, O, O, O, O, O, W],
        [W, W, O, W, W, W, W, W, O, O, W, W, O, W, W],
        [W, O, O, O ,O ,O ,O ,O, O ,W ,O ,O ,O ,W ,W],
        [W, W, O, W, W, W, O, W, O ,W ,O ,W ,O ,W ,W],
        [W ,W ,O ,W ,W ,W ,O ,W ,O ,W ,O ,W, O ,E ,W],
        [W ,W ,O ,W ,O ,O ,O ,W ,W ,O ,O, W ,W ,W ,W],
        [W ,W ,W ,W ,O ,W ,O, W ,O ,O, W ,W, O ,W ,W],
        [W, W ,O, P, O ,W ,O ,O ,O ,W ,W ,W ,O ,W ,W],
        [W, W, W, W, W, W, W, W, W, W, W, O, O, W, W],]

maze4 =[[W, W, W ,W ,W ,W ,W ,W ,W, W, E, W, W ,W ,W],
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
#to a different shape to the rest of the blocks. The player is now a circle and everything else are rectangles
def renderMaze(maze):
  for y, row in enumerate(maze):
    for x, block in enumerate(row):
      if isinstance(block,Wall):
        pygame.draw.rect(
        gameScreen, block.color,
        pygame.Rect(x * block_size, y * block_size, block_size, block_size))
      elif isinstance(block,Exit):
        pygame.draw.rect(
        gameScreen, block.color,
        pygame.Rect(x * block_size, y * block_size, block_size, block_size))
      elif isinstance(block,Key):
        pygame.draw.rect(
        gameScreen, block.color,
        pygame.Rect(x * block_size, y * block_size, block_size, block_size))

#Player Position in each maze. Will render a movable circle 
if renderMaze(maze1) == renderMaze(maze1):
     S = Player(blue,10,80,80,80,80,5) 
else: 
  pass
if renderMaze(maze2) ==  renderMaze(maze2):
  S = Player(blue,10,860,80,860,90,5)
else:
  pass
if renderMaze(maze3) == renderMaze(maze3):
  S = Player(blue,10,160,80,160,80,5)
else:
  pass
if renderMaze(maze4) ==  renderMaze(maze4):
  S = Player(blue,10,860,300,860,300,5)
else:
  pass


# Main game loop
running = True
while running:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    keys = pygame.key.get_pressed()
    #the initial call of the old x and y position is to save this to memory until we encounter a wall
    S.oldx_position = S.x_position
    S.oldy_position = S.y_position
    S.x_position += (keys[pygame.K_d] - keys[pygame.K_a]) * vel
    S.y_position += (keys[pygame.K_s] - keys[pygame.K_w]) * vel
    #When the player hits the Wall this doesn't work yet either
    distance = abs(S.x_position - W.x_position) + abs(S.y_position - W.y_position)
    if distance <= S.radius:
        S.x_position = S.oldx_position
        S.y_position = S.oldy_position
     #If the player reaches the exit this doesn't work yet
    goal = abs(S.x_position - E.x_position) + abs(S.y_position - E.y_position)
    if goal <= S.radius:
      print("Congratulations! You have beat the game")
  #When the player reaches a key

  #When the player reaches a door
    

  gameScreen.fill(white)  # Clears the screen.
  renderMaze(maze4)
  pygame.draw.circle(gameScreen,S.color,(int(S.x_position), int(S.y_position)),10,0) #This makes the player visibly move
  pygame.display.flip()  # Update the display.

  #colission


pygame.quit()
sys.exit()





#create event here where player spawns
