import pygame

pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
#радиус фар
r = 5

class Car:

    width_car = 50
    height_car = 20

    def __init__(self, surface, color):

        self.surf = surface
        self.color = color
        # Методы поверхности get_width() и get_height() возвращают ее размеры.
        self.x = surface.get_width()
        self.y = surface.get_height() // 2 - Car.height_car // 2

    def drive(self):

        pygame.draw.rect(self.surf, self.color, (self.x, self.y, Car.width_car, Car.height_car))
        pygame.draw.circle(self.surf, YELLOW, (self.x + 50, self.y + 5 ), r)
        pygame.draw.circle(self.surf, YELLOW, (self.x + 50, self.y + 15), r)
        pygame.draw.polygon(self.surf, YELLOW, ([self.x + 50, self.y + 5],
                                                [self.x + 70, self.y - 10],
                                                [self.x + 70, self.y + 30],
                                                [self.x + 50, self.y + 15]))
        self.x += 3
        if self.x > WIN_WIDTH:
            # если достигнут предел
            self.x = 0
    def change_up(self):
        self.y -= 10
    def change_down (self):
        self.y += 10


sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

surf_top = pygame.Surface((WIN_WIDTH, WIN_HEIGHT//2))
surf_top.fill(WHITE)

surf_road_top = pygame.Surface ((WIN_WIDTH,WIN_HEIGHT// 8))
surf_road_top.fill(BLACK)

# нижняя черная поверхность, равная другой половине окна
surf_bottom = pygame.Surface((WIN_WIDTH , WIN_HEIGHT// 2))
surf_bottom.fill(BLACK)

surf_road_bottom = pygame.Surface ((WIN_WIDTH,WIN_HEIGHT// 8))
surf_road_bottom.fill(WHITE)

surf_bottom.blit(surf_road_bottom, (0, WIN_WIDTH // 2 - 380 ))
surf_top.blit(surf_road_top, (0, WIN_WIDTH // 2 - 280 ))

sc.blit(surf_top, (0, 0))
sc.blit(surf_bottom, (0, WIN_WIDTH // 2))



# создаем черную машину для верхней поверхности
# и белую - для нижней
car_top = Car(surf_top, WHITE)
car_bottom = Car(surf_bottom, BLACK)

# какая половина активна, до первого клика - никакая
active_top = False
active_bottom = False

top_up_change = False
top_down_change = False
bottom_up_change = False
bottom_down_change = False

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.MOUSEBUTTONUP:
            # если координата X клика меньше половины окна,
            # т. е. клик произошел в верхней половине ...
            if i.pos[1] < WIN_HEIGHT // 2:
                # то активируем верхнюю, отключаем нижнюю
                active_top = True
                active_bottom = False
            elif i.pos[1] > WIN_HEIGHT // 2:
                # иначе - наоборот
                active_bottom = True
                active_top = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                top_up_change = True


            elif i.key == pygame.K_DOWN:
                bottom__down_change = True
        if top_up_change:
            car_top.change_up()
        if top_down_change:
            car_top.change_down()
        if bottom_up_change:
            car_bottom.change_up()
        if bottom_down_change:
            car_bottom.change_down()

    if active_top:
        # Если активна верхняя поверхность,
        # то заливаем только ее цветом,
        surf_top.fill(WHITE)
        # заново отрисовываем верхнюю поверхность на главной.
        surf_top.blit(surf_road_top, (0, WIN_WIDTH // 2 - 280))

        sc.blit(surf_top, (0, 0))
        # двигаем машину,
        car_top.drive()
        sc.blit(surf_top, (0, 0))

    elif active_bottom:
        # Если активна нижняя -> аналогично
        surf_bottom.fill(BLACK)

        surf_bottom.blit(surf_road_bottom, (0, WIN_WIDTH // 2 - 280))
        sc.blit(surf_bottom, (0, WIN_HEIGHT // 2))
        car_bottom.drive()
        sc.blit(surf_bottom, (0, WIN_HEIGHT // 2))
    pygame.display.update()

    pygame.time.delay(20)