# Всё, что нам нужно:
import pygame
import os
import tkinter as tk
from Menu import Menu
from Play import Play
from Equipment import Equipment
from Functions import drawMenu, drawPlay, drawEquipment


if __name__ == '__main__':
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
    pygame.init()
    pygame.display.set_caption('Tower Defense')  # Название окна
    root = tk.Tk()

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    size = width, height  # Размер окна
    screen = pygame.display.set_mode(size)  # Задаём экран для работы с ним
    running = True  # Работа программы
    screenColor = (255, 245, 238)  # Цвет экрана
    menu = Menu(screen, size)  # Создаём класс окна меню
    play = Play(screen, size, './decor/buttons/BtnBack.png')  # Создаём класс окна выбора режима
    equipment = Equipment(screen, size, './decor/buttons/BtnBack.png')  # Создаём класс окна снаряжения
    while running:
        screen.fill(screenColor)  # Заполняем экран соответствующим цветом
        drawMenu(menu)  # Рисуем меню
        for event in pygame.event.get():  # Идём по всем событиям
            if event.type == pygame.QUIT:  # Если происходит выход из окна, заканчиваем программу
                running = False
            if event.type == pygame.MOUSEBUTTONUP:  # Если происходит нажатие мыши, проверяем, была ли нажата кнопка
                # В зависимости от нажатой кнопки, рисуем новое окно
                if menu.btnClick(event.pos) == 'Играть':
                    print(drawPlay(play, screenColor))
                if menu.btnClick(event.pos) == 'Снаряжение':
                    print(drawEquipment(equipment, screenColor))
            if event.type == pygame.MOUSEMOTION:
                # При движении мыши, проверяем, если курсор находится на кнопке, чтобы подсветить её
                menu.backlight(menu.btnClick(event.pos))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_e:
                    running = False

        pygame.display.flip()  # Обновляем экран