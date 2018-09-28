# -*- coding:utf-8 -*-

import pygame
import time


def main():
    #1.创建窗口
    screen = pygame.display.set_mode((480,852), 0, 32)

    #创建一个背景图片
    background = pygame.image.load('./feiji/background.png')

    #创建一个飞机图片
    hero = pygame.image.load('./feiji/hero1.png')

    x = 210
    y = 700


    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (200, 700))
        pygame.display.update()
        
        x += 1
        y -= 1

        time.sleep(0.01)#刷新延迟防止cpu占用率高










if __name__ == '__main__':
    main()
