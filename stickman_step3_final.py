# python game with pygame : Jumping stickman
import pygame
import sys

# step1 : set screen, fps
# step2 : show stickman, jump stickman
# step3 : show tree, move tree

pygame.init()
pygame.display.set_caption('Jumping stickman')
MAX_WIDTH = 800
MAX_HEIGHT =1000 


def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # stickman
    imgStick1 = pygame.image.load('images/stickman1.png')
    imgStick2 = pygame.image.load('images/stickman2.png')
    stick_height = imgStick1.get_size()[1]
    stick_bottom = MAX_HEIGHT - stick_height
    stick_x = 50
    stick_y = stick_bottom
    jump_top = 500
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # tree
    imgTree = pygame.image.load('images/tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    while True:
        screen.fill((255, 255, 255))

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False

        # stickman move
        if is_go_up:
            stick_y -= 10.0
        elif not is_go_up and not is_bottom:
            stick_y += 10.0

        # stickman top and bottom check
        if is_go_up and stick_y <= jump_top:
            is_go_up = False

        if not is_bottom and stick_y >= stick_bottom:
            is_bottom = True
            stick_y = stick_bottom

        # tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))

        # draw stickman
        if leg_swap:
            screen.blit(imgStick1, (stick_x, stick_y))
            leg_swap = False
        else:
            screen.blit(imgStick2, (stick_x, stick_y))
            leg_swap = True

        # update
        pygame.display.update()
        fps.tick(30)
        


if __name__ == '__main__':
    main()
