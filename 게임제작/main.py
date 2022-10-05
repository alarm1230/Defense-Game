import os
import pygame
import sys
from pygame.locals import *
from time import sleep

class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, size, image_path):
        super(AnimatedSprite, self).__init__()

        self.xpos = position[0]
        self.ypos = position[1]

        images = []
        for image in image_path:
            images.append(pygame.image.load(image))

        # rect 만들기
        self.rect = pygame.Rect(position, size)
        # rect크기와 이미지 크기 맞추기
        self.images = [pygame.transform.scale(image, size) for image in images]

        # 캐릭터 첫번째 이미지
        self.index = 0
        self.image = self.images[self.index]

    def update(self, speed=10):

        self.index += speed / 10

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[int(self.index)]

        self.rect.x = self.xpos
        self.rect.y = self.ypos


class Hero(AnimatedSprite):
    def __init__(self, position, size, image_path):
        super().__init__(position, size, image_path)

    def update(self):
        super().update(1)



class Game:

    def __init__(self):
        # 화면 크기 설정
        self.width = 1200
        self.height = 800
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
        self.font = pygame.font.Font("./resources/fonts/LeeSeoyun.ttf", 70)

        # 캐릭터 파일 경로
        self.hero_path = "./resources/images/heros/"
        self.hero_images = os.listdir(self.hero_path)
        self.hero_path_list = [os.path.join(self.hero_path, hero) for hero in self.hero_images]


        # 게임 화면 출력
        self.start_screen()
        self.screen_transition(reverse=True)
        self.main()


    def main(self):
        self.running = True

        

        hero = Hero(position=(100, 600), size=(200, 200), image_path=self.hero_path_list)



        all_sprites = pygame.sprite.Group(hero)

        while self.running:

            for event in pygame.event.get(): # 발생한 입력 event 목록의 event마다 검사
                if event.type == QUIT: # event의 type이 QUIT에 해당할 경우
                    pygame.quit() # pygame을 종료한다
                    sys.exit() # 창을 닫는다

                # elif event.type == KEYDOWN:
                #     if event.key == K_LEFT:
                #         hero.xpos -= 10
                #     if event.key == K_RIGHT:
                #         hero.xpos += 10
                #     if event.key == K_UP:
                #         hero.ypos -= 10
                #     if event.key == K_DOWN:
                #         hero.ypos += 10

            keys = pygame.key.get_pressed()

            if keys[K_UP]:
                hero.ypos -= 10
            if keys[K_DOWN]:
                hero.ypos += 10
            if keys[K_LEFT]:
                hero.xpos -= 10
            if keys[K_RIGHT]:
                hero.xpos += 10

            

            self.window.fill((255, 255, 255))

            


            all_sprites.update()
            all_sprites.draw(self.window)

            pygame.display.update()
            self.clock.tick(self.fps)

    def start_screen(self):
        background = pygame.image.load("./resources/images/backgrounds/JH_Background_1004.png")
        background = pygame.transform.scale(background, self.window_size)

        letz_start = "Press anywhere to start!!"
        btn_font = pygame.font.Font("./resources/fonts/LeeSeoyun.ttf", 20)
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