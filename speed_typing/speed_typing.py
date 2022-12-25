import pygame
import pygame as pg
from pygame.locals import *
import sys
import time
import random


class Game:
    def __init__(self):
        self.w = 750
        self.h = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.end = False
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'time: 0 accuracy:0% wpm=0 '
        self.wpm = 0
        self.head_c = (255, 213, 103)
        self.text_c = (240, 240, 240)
        self.result_c = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('open.jpg')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        self.bg = pygame.image.load('bg.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.w, self.h))

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('typing speed test')

    def get_sentence(self):
        file = open('sentences.txt').read()
        sentence = file.split('\n')
        sentence = random.choice(sentence)
        return sentence

    def draw_text(self, screen, msg, y, fsize, fc):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, fc)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def show_result(self, screen):
        if not self.end:
            self.total_time = time.time() - self.time_start

            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
        self.accuracy = count / len(self.word) * 100
        self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
        self.end = True
        self.results = 'Time: ' + str(round(self.total_time)) + ' secs Accuracy:' + str(
            round(self.accuracy)) + '%' + ' wpm:' + str(round(self.wpm))

        self.icon_image = pygame.image.load('icon.jpg')
        self.icon_image = pygame.transform.scale(self.icon_image, (150, 150))
        self.screen.blit(self.icon_image, (self.w / 2 - 75, self.h - 140))
        self.draw_text(screen, 'Reset', self.h - 70, 60, (255, 213, 103))
        pygame.display.update()

    def run_game(self):
        self.reset_game()

        self.running = True
        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.head_c, (50, 250, 650, 50), 2)
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 650 and 250 <= y <= 300:
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                        # position of reset box
                    if (x >= 310 and x <= 510 and y >= 390 and self.end):
                        self.reset_game()
                        x, y = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_result(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 350, 28, self.result_c)
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            pygame.display.update()
        clock.tick(60)

    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))
        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.end = False

        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        self.word = self.get_sentence()
        if not self.word: self.reset_game()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        msg = 'Typing Speed Test'
        self.draw_text(self.screen, msg, 80, 80, self.head_c)
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)
        self.draw_text(self.screen, self.word, 200, 28, self.text_c)
        pygame.display.update()


Game().run_game()
