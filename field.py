import pygame

FPS = 60
#поле
W = 1200
H = 700
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
BLACK =(0,0,0)

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

#hero
x = W // 2
y = H // 2
r = 50
#bullet
xb = W // 2
yb = H // 2

while 1:
    sc.fill(WHITE)

    pygame.draw.circle(sc, BLUE, (x, y), r)

    pygame.display.update()
    keys = pygame.key.get_pressed()
    '''for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if keys[pygame.K_w]:
            pygame.draw.circle(sc, BLACK, (xb, yb), 10)
    if yb < 400:
        yb += 2'''


    if keys[pygame.K_LEFT]:
        if  keys[pygame.K_UP] == 1:
            x -= 2
            y -= 2
        if  keys[pygame.K_DOWN] == 1:
            x -= 2
            y += 2
        if keys[pygame.K_DOWN]==0 and keys[pygame.K_UP] == 0:
            x-=3

    if keys[pygame.K_RIGHT] ==1:
        if  keys[pygame.K_UP] == 1:
            x += 2
            y -= 2
        if  keys[pygame.K_DOWN]==1:
            x += 2
            y += 2
        if keys[pygame.K_DOWN]==0 and keys[pygame.K_UP] == 0:
            x+=3
    if keys[pygame.K_UP] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0:
        y-=3
    if keys[pygame.K_DOWN] and keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0:
        y+=3
    pygame.display.update()
    pygame.time.delay(30)


