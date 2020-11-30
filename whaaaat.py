import pygame
from math import cos, sin

SIZE = 501, 501

SCREEN = pygame.display.set_mode(SIZE)


# , [100+int(r*sin), 100+int(r*cos)]
def main():
    try:
        pygame.init()
        doing = True
        v = 0
        SCREEN.fill((0, 0, 0))
        pygame.draw.circle(SCREEN, (255, 255, 255), (250, 250), 10)
        r = 70
        center = 250, 250
        ugol_f =75
        ugol_s = 120
        first = [[250, 250], [center[0] - r * sin(ugol_f), center[0] - r * cos(ugol_f)],
                 [center[0] + r * sin(ugol_f), center[0] - r * cos(ugol_f)]]
        second = [[250, 250], [center[0] - r * sin(ugol_s), center[0] +r * cos(ugol_s)],
                  [center[0] + r * sin(ugol_s), center[0] +r * cos(ugol_s)]]
        pygame.draw.polygon(SCREEN, (255, 255, 255), first)

        pygame.draw.polygon(SCREEN, (255, 255, 255), second)
        pygame.display.flip()
        f = False
        while doing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    doing = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        ugol_f+=50
                        ugol_s+=50
                    elif event.button == 3:
                        ugol_f-=50
                        ugol_s-=50
                    f = True
            if f:
                SCREEN.fill((0,0,0))
                first = [[250, 250], [center[0] - r * sin(ugol_f), center[0] - r * cos(ugol_f)],
                         [center[0] + r * sin(ugol_f), center[0] - r * cos(ugol_f)]]
                second = [[250, 250], [center[0] - r * sin(ugol_s), center[0] + r * cos(ugol_s)],
                          [center[0] + r * sin(ugol_s), center[0] + r * cos(ugol_s)]]
                pygame.draw.polygon(SCREEN, (255, 255, 255), first)

                pygame.draw.polygon(SCREEN, (255, 255, 255), second)

    except Exception as e:
        print(e)
    pygame.quit()

if __name__ == '__main__':
    main()
