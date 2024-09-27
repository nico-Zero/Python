import pygame
import math
import random

pygame.init()
X = 800
Y = 600

# Creating a screen
screen = pygame.display.set_mode((X, Y))

# Changing Title of the windows
pygame.display.set_caption("Space Invader")
icon = pygame.image.load(
    "002-battleship.png"
)
pygame.display.set_icon(icon)

# Player
player_i = pygame.image.load(
    "/png/005-battleship.png"
)
player_x = 370
player_y = 480


def Player(x, y):
    screen.blit(player_i, (x, y))


# Enemy
enemy_i = []
enemy_x = []
enemy_y = []
change_x = []
change_y = []
number_e = 10

for i in range(number_e):
    enemy_i.append(
        pygame.image.load(
            "/png/003-ufo.png"
        )
    )
    enemy_x.append(random.randint(0, 756))
    enemy_y.append(random.randint(10, 150))
    change_x.append(1)
    change_y.append(30)


def Enemy(x, y):
    for i in range(number_e):
        screen.blit(enemy_i[i], (x, y))


# Game loop
r = True
c_x = 0
c_y = 0

# Background
background = pygame.image.load(
    "/space_stars_sky_night_116649_800x600.jpg"
)

# Bullet
bullet = pygame.image.load(
    "/32pix_bullet/png/001-bullet.png"
)
bullet_x = 0
bullet_y = player_y - 32
b_change_y = 50
b = False


def bul(x, y):
    global b
    global bullet_y
    screen.blit(bullet, (x, y))
    if y <= 0:
        bullet_y = player_y - 32
        b = False


# Collision
def col(ex, ey, bx, by):
    global change_x
    d = math.sqrt(math.pow(ex - bx, 2) + math.pow(ey - by, 2))
    if d < 32 and by < 400:
        for i in range(number_e):
            if change_x[i] < 0:
                change_x[i] = -(abs(change_x[i]) + 0.05)
            else:
                change_x[i] = abs(change_x[i]) + 0.05
        return True
    else:
        return False


# win count
wins = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


def Wins():
    score = font.render(f"Score : {wins}", True, (255, 255, 255))
    screen.blit(score, (textX, textY))


# game over
font_g = pygame.font.Font("freesansbold.ttf", 100)
text_X = 100
text_Y = 200


def game_over():
    score = font_g.render(f"GAME OVER", True, (255, 255, 255))
    screen.blit(score, (text_X, text_Y))


while r:
    # Background color
    screen.fill((0, 0, 0, 0))
    screen.blit(background, (0, 0))
    speed = 12
    # Exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
        # Key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                c_x = -speed
            if event.key == pygame.K_RIGHT:
                c_x = speed
            if event.key == pygame.K_UP:
                c_y = -speed
            if event.key == pygame.K_DOWN:
                c_y = speed
            if event.key == pygame.K_SPACE:
                if b == False:
                    bullet_x = player_x
                    bullet_y = player_y - 32
                    # bul((bullet_x + 16),bullet_y )
                    b = True
        if event.type == pygame.KEYUP:
            if (
                event.key == pygame.K_LEFT
                or event.key == pygame.K_RIGHT
                or event.key == pygame.K_UP
                or event.key == pygame.K_DOWN
            ):
                c_x = 0
                c_y = 0

    # Boundry chacking
    player_x += c_x
    if player_x <= 0:
        player_x = 1
    elif player_x >= 737:
        player_x = 736

    player_y += c_y
    if player_y <= 0:
        player_y = 1
    elif player_y >= 537:
        player_y = 536

    # Bullet movenent
    if b:
        bul((bullet_x + 16), bullet_y)
        bullet_y -= b_change_y

    # Calling Player
    Player(player_x, player_y)

    # Enemy movenent
    for i in range(number_e):
        if enemy_x[i] <= 0:
            enemy_x[i] = 1
            change_x[i] *= -1
            enemy_y[i] += change_y[i]
        elif enemy_x[i] >= 737:
            enemy_x[i] = 736
            change_x[i] *= -1
            enemy_y[i] += change_y[i]

        if enemy_y[i] > 536:
            for j in range(number_e):
                enemy_y[j] = 2000
            game_over()
            break

        enemy_x[i] += change_x[i]

        if col(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            enemy_x[i] = random.randint(0, 756)
            enemy_y[i] = random.randint(10, 150)
            wins += 1

        Enemy(enemy_x[i], enemy_y[i])

    Wins()
    pygame.display.update()
