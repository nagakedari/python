import pygame
import os
import random
import math
from pygame import mixer

#Need to initalize
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invader')
current_path = os.path.dirname(__file__)
icon = pygame.image.load(os.path.join(current_path, 'spaceship_icon.png'))
pygame.display.set_icon(icon)

background = pygame.image.load(os.path.join(current_path, 'spaceship.png'))

mixer.music.load(os.path.join(current_path, 'background.wav'))
mixer.music.play(-1)

#Player
playerImg = pygame.image.load(os.path.join(current_path, 'player.png'))
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load(os.path.join(current_path, 'enemy.png')))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)



#Bullet
bulletImg = pygame.image.load(os.path.join(current_path, 'bullet.png'))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
#Ready state means we cannot see the bullet
#Fire state means bullet is moving
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def player(x, y):
    screen.blit(playerImg,(x,y))

def enemy(x, y, i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def show_score (x, y):
    score = font.render("Score :"+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text ():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def confineToBounderies(x):
    if x <= 0:
        x = 0
    elif x >=736:
        x=736
    return x

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX- bulletX, 2)+ math.pow(enemyY-bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound(os.path.join(current_path, 'laser.wav'))
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change

    playerX = confineToBounderies(playerX)

    
    for i in range(no_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyY[i] > 450 :
            for j in range(no_of_enemies):
                enemyY[j]= 2000
            game_over_text()
            break;
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i]= -1
            enemyY[i] += enemyY_change[i]
        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision == True :
            explosion_sound = mixer.Sound(os.path.join(current_path, 'explosion.wav'))
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value+= 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    
    # BUllet movement
    if bulletY <=0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
