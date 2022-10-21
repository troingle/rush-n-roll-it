# Essential
import pygame
import os  # Only essential if assets are used

# Very useful
import math
import random
import time

pygame.font.init()

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
LIME = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
CYAN = 0, 255, 255
MAGENTA = 255, 0, 255
SILVER = 192, 192, 192
GREY = 128, 128, 128
DARKGREY = 64, 64, 64
MAROON = 128, 0, 0
OLIVE = 128, 128, 0
GREEN = 0, 128, 0
PURPLE = 128, 0, 128
TEAL = 0, 128, 128
NAVY = 0, 0, 128

CASINO_RED = (76, 16, 34)
CASINO_ORANGE = (126, 64, 41)
CASINO_YELLOW = (175, 132, 57)

# CONSTANTS
SCREEN_WIDTH, SCREEN_HEIGHT = 576, 576  # Resolution of screen
FPS = 60  # How many times the game should update per second
GAME_TITLE = "RUSH 'N ROLL IT"
PLAYER_POSITION = pygame.Rect(304, 304, 32, 32)

# Variables
velocity = 3
bullet_velocity = 6
bullets = []
bullet_count = []
angle = 0
level = 1
total_dice_num = 0
count = 0
dice_nums = []
enemies = []
enemy_nums = []
x = 0
x2 = 0
score = 0
fail = False
hit_enemy = False
second_count = -600
timer = 0
immune = 60
immune_ticking = False
dice_two_count = 0

pygame.mixer.init()  # Initializes pygame's sound system

# Loads assets
MUSIC = pygame.mixer.music.load(os.path.join("DiceGameAssets", "backgroundMusic.wav"))
pygame.mixer.music.set_volume(0.5)
SHOOT_SOUND = pygame.mixer.Sound(os.path.join("DiceGameAssets", "shoot_sound.wav"))
HIT_SOUND = pygame.mixer.Sound(os.path.join("DiceGameAssets", "hit_sound.wav"))
WIN_SOUND = pygame.mixer.Sound(os.path.join("DiceGameAssets", "win_sound.wav"))
PLAYER_SPRITE = pygame.image.load(os.path.join("DiceGameAssets", "tophat_player.png"))  # Loads image from a folder
PLAYER_SPRITE = pygame.transform.scale(PLAYER_SPRITE, (32, 32))  # Makes image size in pixels as desired (32, 32)
BG = pygame.image.load(os.path.join("DiceGameAssets", "bg_placeholder.png"))  # Loads image from a folder
BG = pygame.transform.scale(BG, (576, 576))  # Makes image size in pixels as desired (576, 576)

ARROW = pygame.image.load(os.path.join("DiceGameAssets", "bg_placeholder.png"))  # Loads image from a folder
ARROW = pygame.transform.scale(ARROW, (576, 576))  # Makes image size in pixels as desired (576, 576)

D1 = pygame.image.load(os.path.join("DiceGameAssets", "tdice_1.png"))  # Loads image from a folder
D1 = pygame.transform.scale(D1, (32, 32))
D2 = pygame.image.load(os.path.join("DiceGameAssets", "tdice_2.png"))  # Loads image from a folder
D2 = pygame.transform.scale(D2, (32, 32))
D3 = pygame.image.load(os.path.join("DiceGameAssets", "tdice_3.png"))  # Loads image from a folder
D3 = pygame.transform.scale(D3, (32, 32))
D4 = pygame.image.load(os.path.join("DiceGameAssets", "tdice_4.png"))  # Loads image from a folder
D4 = pygame.transform.scale(D4, (32, 32))
D5 = pygame.image.load(os.path.join("DiceGameAssets", "tdice_5.png"))  # Loads image from a folder
D5 = pygame.transform.scale(D5, (32, 32))
D6 = pygame.image.load(os.path.join("DiceGameAssets", "tdice_6.png"))  # Loads image from a folderD6
D6 = pygame.transform.scale(D6, (32, 32))

E1 = pygame.image.load(os.path.join("DiceGameAssets", "dice_1.png"))  # Loads image from a folder
E1 = pygame.transform.scale(E1, (32, 32))
E2 = pygame.image.load(os.path.join("DiceGameAssets", "dice_2.png"))  # Loads image from a folder
E2 = pygame.transform.scale(E2, (32, 32))
E3 = pygame.image.load(os.path.join("DiceGameAssets", "dice_3.png"))  # Loads image from a folder
E3 = pygame.transform.scale(E3, (32, 32))
E4 = pygame.image.load(os.path.join("DiceGameAssets", "dice_4.png"))  # Loads image from a folder
E4 = pygame.transform.scale(E4, (32, 32))
E5 = pygame.image.load(os.path.join("DiceGameAssets", "dice_5.png"))  # Loads image from a folder
E5 = pygame.transform.scale(E5, (32, 32))
E6 = pygame.image.load(os.path.join("DiceGameAssets", "dice_6.png"))  # Loads image from a folderD6
E6 = pygame.transform.scale(E6, (32, 32))

dice_number = {
    1: D1,
    2: D2,
    3: D3,
    4: D4,
    5: D5,
    6: D6
}

enemy_num = {
    1: E1,
    2: E2,
    3: E3,
    4: E4,
    5: E5,
    6: E6
}

dice = []

# Setup
pygame.init()  # Initializes pygame
pygame.font.init()  # Initializes pygame's fonts
pygame.display.set_caption(GAME_TITLE)  # The title of the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Makes game window

FONT = pygame.font.Font("DiceGameAssets/ToonArounddf.otf", 32)  # Font name, font size. Taken from pygame
SMALL_FONT = pygame.font.Font("DiceGameAssets/ToonArounddf.otf", 22)  # Font name, font size. Taken from pygame
TITLE_FONT = pygame.font.Font("DiceGameAssets/ToonArounddf.otf", 48)


# Functions
def player_movement(keys_pressed):
    # Add movement on key press and change direction
    global angle
    if keys_pressed[pygame.K_a]:  # Left
        angle = 90
        if PLAYER_POSITION.x - velocity >= 25:
            PLAYER_POSITION.x -= velocity
        else:
            PLAYER_POSITION.x = 25
    if keys_pressed[pygame.K_d]:  # Right
        angle = 270
        if PLAYER_POSITION.x + velocity <= 510:
            PLAYER_POSITION.x += velocity
        else:
            PLAYER_POSITION.x = 510
    if keys_pressed[pygame.K_w]:  # Up
        angle = 0
        if PLAYER_POSITION.y - velocity >= 30:
            PLAYER_POSITION.y -= velocity
        else:
            PLAYER_POSITION.y = 30
    if keys_pressed[pygame.K_s]:  # Down
        angle = 180
        if PLAYER_POSITION.y + velocity <= 458:
            PLAYER_POSITION.y += velocity
        else:
            PLAYER_POSITION.y = 458


def draw_to_screen(dice_nums, timer):
    global PLAYER_SPRITE
    # The rest
    screen.blit(BG, (0, 0))
    screen.blit(pygame.transform.rotate(PLAYER_SPRITE, angle), (PLAYER_POSITION))
    for bullet in bullets:
        pygame.draw.rect(screen, CASINO_ORANGE, bullet[0])
    for i in range(len(dice)):
        screen.blit(dice_number[dice_nums[i]], (dice[i].x, dice[i].y))
    for i in range(len(enemies)):
        screen.blit(enemy_num[enemy_nums[i]], (enemies[i].x, enemies[i].y))

    scoretext = FONT.render("Score: " + str(score), 1, WHITE)
    screen.blit(scoretext, (30, 516))

    leveltext = FONT.render("Level: " + str(level), 1, WHITE)
    screen.blit(leveltext, (200, 516))

    timer_text = FONT.render("Timer: " + str(timer//60), False, WHITE)
    screen.blit(timer_text, (360, 516))

def handle_bullets():
    global enemies
    global score
    global randnums
    global hit_enemy
    for bullet in bullets:
        if bullet[1] == 0:
            bullet[0].y -= bullet_velocity
        elif bullet[1] == 270:
            bullet[0].x += bullet_velocity
        elif bullet[1] == 90:
            bullet[0].x -= bullet_velocity
        else:
            bullet[0].y += bullet_velocity
        # Bullets die off screen
        if bullet[0].y > 596 or bullet[0].y < 32 or bullet[0].x > 596 or bullet[0].x < 32:
            bullets.remove(bullet)

        a = len(bullets)
        b = len(enemies)
        for i in range(a):
            for k in range(b):
                try:
                    if pygame.Rect.colliderect(bullets[i][0], enemies[k]):
                        pygame.mixer.Sound.play(HIT_SOUND)
                        score += enemy_nums[k]
                        del bullets[i]
                        del enemies[k]
                        del enemy_nums[k]
                        hit_enemy = True
                except:
                    pass


def create_bullet():
    pygame.mixer.Sound.play(SHOOT_SOUND)
    bullet = ((pygame.Rect(PLAYER_POSITION.x + 12, PLAYER_POSITION.y + 12, 8, 8)), angle)
    bullets.append(bullet)


def spawn_dice():
    global total_dice_num
    global count
    # controls the dice count based on level
    if level == 0 or level == 1:
        dice_count = 1
    elif level >= 2:
        dice_count = level

    # gets the random dice position and adds the dice to a list
    while len(dice) <= dice_count:
        dice_x = (50 + 50 * len(dice))
        dice_y = (50)
        die = pygame.Rect(dice_x, dice_y, 32, 32)
        dice.append(die)
        dice_nums.append(random.randint(1, 6))
        total_dice_num = sum(dice_nums)

    return dice_nums, total_dice_num


def spawn_enemies():
    global x
    global fail
    global score
    global second_count
    global level
    global immune_ticking
    global enemies
    global enemy_nums
    global hit_enemy
    global dice_texture
    global dice
    global dice_nums
    global dice_number
    global dice_countd
    global dice_two_count
    global immune
    global timer

    # wait 1 second before doing stuff
    if immune_ticking:
        immune += 1
    x += 1
    timer += 1
    if timer >= 1800:
        timer = 0
        score = 9999

    second_count += 1
    if second_count >= 120 and len(enemies) > 4:
        second_count = 0
        del enemies[0]
        del enemy_nums[0]
    if x >= 120 and len(enemies) < 5:  # max 5 enemies
        x = 0
        # generates a random position for the enemy
        enemy_x = random.randint(30, 550)
        enemy = pygame.Rect(enemy_x, 85, 32, 32)
        enemies.append(enemy)
        randnum = random.randint(1, 6)
        # Dice adjustment
        if random.randint(1, 5) >= level:
            if randnum > 4:
                randnum -= 1

            if randnum > 5:
                if random.randint(1, 2) == 1:
                    randnum -= 3

        enemy_nums.append(randnum)
        if hit_enemy == True:
            # score += random_nums[0] # this adds and deletes the FIRST number of the list
            # del random_nums[0] # ^
            hit_enemy = False
    for enemy in enemies:  # enemy movement AI
        if enemy.x > PLAYER_POSITION.x:
            enemy.x -= 1
        elif enemy.x < PLAYER_POSITION.x:
            enemy.x += 1
        if enemy.y > PLAYER_POSITION.y:
            enemy.y -= 1
        elif enemy.y < PLAYER_POSITION.y:
            enemy.y += 1

    # Enemy collision
    for enemy in enemies:
        if pygame.Rect.colliderect(enemy, PLAYER_POSITION) and immune >= 60:
            pygame.mixer.Sound.play(HIT_SOUND)
            immune = 0
            immune_ticking = True
            score -= 6
            if score < 0:
                score = 0

    if score > total_dice_num:  # if the score goes above the right number
        fail = True  # fails not implemented yet
        level += 1
        dice = []
        score = 0
        timer = 0
        dice_count = []
        enemies = []
        dice_nums = []
        enemy_nums = []
        dice_numbers = []
        level = 0
        score = 0
    elif score == total_dice_num:
        pygame.mixer.Sound.play(WIN_SOUND)
        level += 1
        dice = []
        score = 0
        timer = 0
        dice_count = []
        enemies = []
        dice_nums = []
        enemy_nums = []
        dice_numbers = []


# Main loop

# Variables used in game
run = True
title_running = True
clock = pygame.time.Clock()

# Menu buttons
start_game_box = pygame.Rect(SCREEN_WIDTH / 2 - 96, SCREEN_HEIGHT / 2 - 96, 176, 48)
exit_game_box = pygame.Rect(SCREEN_WIDTH / 2 - 96, SCREEN_HEIGHT / 2 + 32, 176, 48)

# Title screen
while title_running:
    screen.fill(CASINO_RED)
    # Draw buttons and text
    pygame.draw.rect(screen, CASINO_RED, start_game_box)
    pygame.draw.rect(screen, CASINO_RED, exit_game_box)
    screen.blit((FONT.render("START GAME", False, WHITE)), (SCREEN_WIDTH / 2 - 76, SCREEN_HEIGHT / 2 - 96))
    screen.blit((FONT.render("EXIT", False, WHITE)), (SCREEN_WIDTH / 2 - 24, SCREEN_HEIGHT / 2 + 20))
    screen.blit((SMALL_FONT.render("KILLING AN ENEMY GIVES YOU THEIR NUMBER", False, WHITE)),
                (112, SCREEN_HEIGHT / 2 + 102))
    screen.blit((SMALL_FONT.render("GET THE EXACT NUMBER ON THE DICE TO WIN", False, WHITE)),
                (112, SCREEN_HEIGHT / 2 + 172))

    screen.blit((SMALL_FONT.render("DON'T LET THE TIMER REACH 30. YOU WILL DIE", False, WHITE)),
                (112, SCREEN_HEIGHT / 2 + 242))

    screen.blit((TITLE_FONT.render(GAME_TITLE, False, WHITE)), (SCREEN_WIDTH / 2 - 136, SCREEN_HEIGHT / 2 - 256))
    pygame.display.update()
    # Quitting
    for event in pygame.event.get():
        # Closes game from window
        if event.type == pygame.QUIT:
            title_running = False
            run = False

        # Close game
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_game_box.collidepoint(pygame.mouse.get_pos()):
                title_running = False

            # Close title and game
            elif exit_game_box.collidepoint((pygame.mouse.get_pos())):
                run = False
                title_running = False

    clock.tick(FPS)

pygame.mixer.music.play(-1)
# Game loop
while run:
    # Gets input
    for event in pygame.event.get():
        # Closes game when told to
        if event.type == pygame.QUIT:
            run = False
        # Makes bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(bullets) < 3:
                create_bullet()
    # Game logic
    newlevel = level
    if fail == True:
        enemies = []
        bullets = []
        bullet_count = []
        angle = 0
        timer = 0
        total_dice_num = 0
        count = 0
        dice_nums = []
        enemies = []
        enemy_nums = []
        x = 0
        x2 = 0
        score = 0
        hit_enemy = False

    keys_pressed = pygame.key.get_pressed()
    player_movement(keys_pressed)
    handle_bullets()
    dice_nums, total_dice_num = spawn_dice()
    spawn_enemies()

    # Draw things to screen
    draw_to_screen(dice_nums, timer)
    if fail == True:
        for i in range(FPS):
            clock.tick(FPS)
            screen.blit((FONT.render("You Failed", False, BLACK)), (200, 200))
            pygame.display.update()
        fail = False

    # Updates screen and runs at set FPS
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()  # Quits game when loop is stopped
