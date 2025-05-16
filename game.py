import pygame
import time
import random
import sys
import os


# Инициализация pygame
pygame.init()

# Определение цветов (RGB)
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Размеры окна
window_width = 600
window_height = 400

# Создание окна игры
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Змейка')

# Часы для контроля скорости игры
clock = pygame.time.Clock()

# Размер блока и скорость змейки
block_size = 10
snake_speed = 15

# Шрифт для отображения счета
font_style = pygame.font.SysFont(None, 30)

# bg = pygame.image.load('bg1.png').convert()

# def drawWindow():
# screen.blit(bg, (0, 0))

def paused():
    screen.fill(black)

    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_ojects("Paused", largeText)
    TextRect.center =((window_width_width/2), (window_height/2))
    game_display.blit(TextRect, TextSurf)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def show_score(score):
    """Отображение текущего счета"""
    score_text = font_style.render("Счет: " + str(score), True, white)
    game_display.blit(score_text, [10, 10])

def message(msg, color):
    """Отображение сообщения на экране"""
    rendered_message = font_style.render(msg, True, color)
    game_display.blit(rendered_message, [window_width / 6, window_height / 3])

def draw_snake(snake_list, block_size):
    """Отрисовка змейки"""
    for segment in snake_list:
        pygame.draw.rect(game_display, white, [segment[0], segment[1], block_size, block_size])

is_paused = False



def game_loop():
    """Основной игровой цикл"""
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = window_width / 2
    y1 = window_height / 2

    # Изменение позиции змейки
    x1_change = 0
    y1_change = 0

    # Тело змейки (список координат)
    snake_list = []
    snake_length = 1

    # Координаты еды
    foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0

    # Координаты препятствий
    obstacles = []
    for i in range(5):
        obsx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
        obsy = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0


    while not game_over:

        # Экран окончания игры
        while game_close:
            game_display.fill(black)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
            show_score(snake_length - 1)
            pygame.display.update()

            # Обработка нажатий клавиш на экране окончания игры
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        os.kill(os.getpid(), 9)
                        game_over = True
                        game_close = False       
                    if event.key == pygame.K_c:
                        game_loop()
                    
                                        
                                        
                    
                        
                    

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x1_change = +block_size
                    y1_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -block_size
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = +block_size
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                if pause == True:
                    screen.fill(black)
                    font = pygame.font.SysFont("Britanic Bold", 40)
                    pygame.display.flip()

                    


        # Проверка столкновения со стенами
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Обновление позиции змейки
        x1 += x1_change
        y1 += y1_change

        # Отрисовка игрового поля
        game_display.fill(black)

        # Отрисовка еды
        pygame.draw.rect(game_display, green, [foodx, foody, block_size, block_size])
        pygame.draw.rect(game_display, red, [obsx, obsy, block_size, block_size])


        # Добавление текущей позиции змейки в список
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Удаление лишних элементов змейки
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Проверка на столкновение с самим собой
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Отрисовка змейки
        draw_snake(snake_list, block_size)

        # Отображение счета
        show_score(snake_length - 1)

        # Обновление экрана
        pygame.display.update()


        

        # Проверка на поедание еды
        if x1 == foodx and y1 == foody:
            global snake_speed
            # Создаем новую еду
            foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            # Увеличиваем длину змейки
            snake_length += 1
            snake_speed += 50

        if x1 == obsx and y1 ==obsy:
            game_close = True

    


        # Контроль скорости игры
        clock.tick(snake_speed)        

        # Завершение pygame
        # pygame.quit()
        # quit()

        # Проверка столкновения со стенами
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Обновление позиции змейки
        x1 += x1_change
        y1 += y1_change

        # Отрисовка игрового поля
        # game_display.fill(black)

        # Отрисовка еды
        pygame.draw.rect(game_display, green, [foodx, foody, block_size, block_size])

        # Добавление текущей позиции змейки в список
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Удаление лишних элементов змейки
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Проверка на столкновение с самим собой
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Отрисовка змейки
        draw_snake(snake_list, block_size)

        # Отображение счета
        show_score(snake_length - 1)

        # Обновление экрана
        pygame.display.update()

        # Проверка на поедание еды
        if x1 == foodx and y1 == foody:
            # Создаем новую еду
            foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            # Увеличиваем длину змейки
            snake_length += 1

        # Контроль скорости игры
        clock.tick(snake_speed)

    # Завершение pygame
    pygame.quit()
    quit()

game_loop()