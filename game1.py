import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("My first game")


clock = pygame.time.Clock()

x = 50
y = 400
width = 40
height = 60
vel = 5
isJump = False
jumpCount = 5

run = True
while run:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        if x <= 0:
            x = 500
    elif keys[pygame.K_RIGHT]:
        x += vel
        if x >= 500:
            x = 0

    if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
        y -= (jumpCount ** 2) * 0.5
        neg = 1
        isJump = True
        if y <= 0:
            y = 500
    elif isJump:
        if neg == 1:
            y += (jumpCount ** 2) * 0.5
        isJump = False
    else:
        if keys[pygame.K_UP]:
            y -= vel
            if y <= 0:
                y = 500
        elif keys[pygame.K_DOWN]:
            y += vel
            if y >= 500:
                y = 0






    if keys[pygame.K_q]:
        run = False




    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, 20, 50), 3)
    pygame.display.update()


pygame.quit()