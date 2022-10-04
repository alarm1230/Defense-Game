import os
import pygame
import sys
from pygame.locals import *
from time import sleep


class Game:

    def __init__(self):
        # 화면 크기 설정
        self.width = 600
        self.height = 400
        self.window_size = (self.width, self.height)

        # 프레임 수 설정
        self.fps = 60

        # 기타 상수들
        self.title = "준호 타운을 지켜줘!!"
        self.running = False

        # 초기화 및 화면 설정
        pygame.init()
        pygame.display.set_caption(self.title)
        self.window = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()

        # 기타 설정들
        self.font = pygame.font.Font("게임제작/아마도/LeeSeoyun.ttf", 70)

        self.start_screen()
        self.screen_transition(reverse=True)
        self.main()


    def main(self):
        self.running = True

        while self.running:

            for event in pygame.event.get(): # 발생한 입력 event 목록의 event마다 검사
                if event.type == QUIT: # event의 type이 QUIT에 해당할 경우
                    pygame.quit() # pygame을 종료한다
                    sys.exit() # 창을 닫는다

            self.window.fill((255, 255, 255))


            pygame.display.update()
            self.clock.tick(self.fps)

    def start_screen(self):
        background = pygame.image.load("게임제작/아마도/background1.webp")
        background = pygame.transform.scale(background, self.window_size)

        letz_start = "Press anywhere to start!!"
        btn_font = pygame.font.Font("게임제작/아마도/LeeSeoyun.ttf", 20)
        btn_color = (255, 255, 255)

        start_btn =  btn_font.render(letz_start, 1, btn_color)
        start_btn_rect = start_btn.get_rect()
        start_btn_rect.center = (self.width / 2, self.height / 1.45)

        counter = 0
        line_start = 0
        line_end = len(self.title)

        in_control = True

        if self.running == False:
            while in_control:

                title = self.font.render(self.title[:line_start], 1, (0, 0, 0))
                title_rect = title.get_rect()
                title_rect.center = (self.width/2, self.height/3)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        in_control = False
                        break

                self.window.blit(background, (0, 0))
                self.window.blit(title, title_rect)

                if counter == 1:
                    self.window.blit(start_btn, start_btn_rect)
                    counter = 0
                else:
                    counter = 1

                if line_start < line_end:
                    line_start += 1
                    sleep(0.2)
                else:
                    sleep(0.5)

                pygame.display.update()
                self.clock.tick(self.fps)

    def screen_transition(self, reverse=False, step=5):
        in_control = True

        if not reverse:
            red, green, blue = 0, 0, 0
        elif reverse:
            red, green, blue = 255, 255, 255

        while in_control:
            transition = (red, green, blue)

            if not reverse:
                if red >= 255:
                    break
            elif reverse:
                if red <= 0:
                    break

            if not reverse:
                red += step
                green += step
                blue += step
            elif reverse:
                red -= step
                green -= step
                blue -= step

            self.window.fill(transition)

            pygame.display.update()
            self.clock.tick(self.fps)


class Monster:
    pass



game = Game()