import pygame, sys
import random
from pygame import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(10, 20), Vector2(9, 20), Vector2(8, 20)]
        self.direction = Vector2(1, 0)
        self.add_block = False
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,pygame.Color('blue'),snake_rect)
    def movement(self):
        if self.add_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, self.body[0] + self.direction)
            self.body = body_copy
            self.add_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, self.body[0] + self.direction)
            self.body = body_copy

    def new_block(self):
        self.add_block = True
class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.rect(screen,(255, 0, 0), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


pygame.init()
cell_size = 20
cell_number = 30
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption("Snake game by Revanth")
time = pygame.time.Clock()
fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

score_font = pygame.font.SysFont("comicsansms", 35)
def Score(score):
    value = score_font.render("Your Score: " + str(score), True, pygame.Color('yellow'))
    screen.blit(value, [0,0])
length_of_snake = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.movement()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if snake.direction != Vector2(-1, 0):
                    snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if snake.direction != Vector2(1, 0):
                    snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_UP:
                if snake.direction != Vector2(0, 1):
                    snake.direction =(0, -1)
            if event.key == pygame.K_DOWN:
                if snake.direction != Vector2(0, -1):
                    snake.direction = (0, 1)
    if not 0<= snake.body[0].x < cell_number or not 0 <= snake.body[0].y < cell_number:
        sys.exit()
    for block in snake.body[2:]:
        if block == snake.body[0]:
            sys.exit()
    if snake.body[0] == fruit.pos:
        fruit.randomize()
        snake.new_block()
        length_of_snake += 1
    screen.fill(pygame.Color('green'))
    fruit.draw_fruit()
    snake.draw_snake()
    Score(score= length_of_snake)
    pygame.display.update()
    time.tick(60)
