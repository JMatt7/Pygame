import pygame

pygame.init()

win = pygame.display.set_mode((1900, 1000))

pygame.display.set_caption("My first game")

walkSkeleton = [pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__001.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__002.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__003.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__004.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__005.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__006.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__007.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__008.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__009.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__010.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__011.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__012.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__013.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__014.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__015.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__016.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__017.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__018.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__019.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__020.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__021.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__022.png')]

jumpSkeleton = [
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__000.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__001.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__002.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__003.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__004.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__005.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__006.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__007.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__008.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__009.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__010.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__011.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__012.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__013.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__014.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__015.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__016.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__017.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__018.png'),
             pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Jumping__019.png')]

bg = pygame.image.load('Background/m002SewerSetPNG.png')
char = pygame.image.load('Characters/Monster - Skeleton/FW_Skeleton_Walking__000.png')
clock = pygame.time.Clock()


class Character(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 20

    def walkright(self, win):
        if self.walkCount + 1 >= 22:
            self.walkCount = 0

        elif self.right:
            win.blit(walkSkeleton[self.walkCount], (self.x, self.y))
            self.walkCount += 1

    def static(self, win):
        win.blit(char, (self.x, self.y))

    def jump(self, win):
        if self.jumpCount - 1 <= 0:
            self.jumpCount = 20

        elif self.isJump:
            win.blit(jumpSkeleton[(20 - self.jumpCount)], (self.x, self.y))
            self.walkCount -= 1

def drawBackground():
    win.blit(bg, (0, 0))
    if skeleton.right == 1:
        skeleton.walkright(win)
    elif skeleton.isJump == 1:
        skeleton.jump(win)
    else:
        skeleton.static(win)

    pygame.display.update()


skeleton = Character(100, 670, 146, 206)
run = True

while run:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and skeleton.x > skeleton.vel:
        skeleton.x += skeleton.vel
        skeleton.right = True
        skeleton.left = False
    else:
        skeleton.right = False
        skeleton.left = False
        skeleton.walkCount = 0

    if not skeleton.isJump:
        if keys[pygame.K_SPACE]:
            skeleton.isJump = True
            skeleton.right = False
            skeleton.left = False
            skeleton.walkCount = 0

    else:
        if skeleton.jumpCount >= 10:
            skeleton.y -= ((20 - skeleton.jumpCount) ** 2) * 0.5
            skeleton.jumpCount -= 1
        elif 0 <= skeleton.jumpCount < 10:
            skeleton.y += ((10 - skeleton.jumpCount) ** 2) * 0.5
            skeleton.jumpCount -= 1
        else:
            skeleton.isJump = False
            skeleton.jumpCount = 20

    if keys[pygame.K_q]:
        run = False

    drawBackground()

pygame.quit()