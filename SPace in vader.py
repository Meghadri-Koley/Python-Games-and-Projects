import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('spaceship.png')
pygame.display.set_caption("Space Invaders")

playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load('ufo.png')
enemyX = 370
enemyY = 50
enemyX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
