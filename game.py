import pygame

pygame.init()

K = (0, 0, 0); W = (255, 255, 255)
R =(255,0,0); B =(0,255,0); G =(0,0,255)

size = (700, 500)
display = pygame.display.set_mode(size)
pygame.display.set_caption('Manacala')

bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, size)

clock = pygame.time.Clock()

done = False

p1_board = size[0] - 450
p2_board = size[0] - 300

def draw_board():
    for pos in range(100, 700, 100):
        pygame.draw.circle(display, K, (pos, p1_board + 20), 38)
        pygame.draw.circle(display, K, (pos, p2_board - 20), 38)

    pygame.draw.ellipse(display, K, [8, p1_board - 32, 47, 220])
    pygame.draw.ellipse(display, K, [647, p1_board - 32, 47, 220])




while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        print(event)

    display.blit(bg, (0, 0))

    draw_board()   
   

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

