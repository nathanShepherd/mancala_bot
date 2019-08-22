import pygame
import math
pygame.init()

K = (0, 0, 0); W = (100, 255, 255)
R =(204,0,204); G =(70,255,70); B =(153,0,76)
COLS = [W, R, G, B, R, W, G, B, G, W, R, B, G]*3
size = (700, 500)
display = pygame.display.set_mode(size)
pygame.display.set_caption('Manacala')

bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, size)

clock = pygame.time.Clock()

done = False

p1_board = size[0] - 450
p2_board = size[0] - 300

POS = {}
for i in range(1, 7):
    POS[i] = (i * 100, p1_board + 20)
    POS[i + 6] = (i * 100, p2_board - 20)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def sprite(num, pos):
    # find rotation of a pt on circle given a circle and pt in the plane
    r = 15
    for s in range(0, num):
      theta = 2*math.pi * (s / num)
      x = int(r*math.cos(theta))
      y = int(r*math.sin(theta))
      x = POS[pos][0] + x
      y = POS[pos][1] + y
      pygame.draw.circle(display, COLS[s], (x, y), 12)
    

def draw_board():
    for pos in range(100, 700, 100):
        pygame.draw.circle(display, K, (pos, p1_board + 20), 38)

        pygame.draw.circle(display, K, (pos, p2_board - 20), 38)

    pygame.draw.ellipse(display, K, [8, p1_board - 32, 47, 220])
    pygame.draw.ellipse(display, K, [647, p1_board - 32, 47, 220])


    sprite(5, 1)
    sprite(3, 2)
    sprite(4, 3)
    sprite(10, 4)
    sprite(20, 5)
    sprite(6, 6)
    sprite(36, 7)


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        print(event)

    display.blit(bg, (0, 0))

    draw_board()   
   

    pygame.display.update()
    clock.tick(60)

print(POS)
pygame.quit()
quit()

