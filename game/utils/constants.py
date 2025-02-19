import pygame
import os
from game.assets.Music import *

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG_1 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track_2.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_BLINK1 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_blink1.png"))
SPACESHIP_BLINK2 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_blink2.png"))
SPACESHIP_BLINK3 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_blink3.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))

BOSS_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/BOSS_1.png"))

FONT_STYLE = 'freesansbold.ttf'

BULLET_ENEMY_TYPE = "enemy"
BULLET_BOSS_TYPE = "boss"
BULLET_SPACESHIP_TYPE = "player"

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"

RESET = "reset"

MUSIC_MENU = os.path.join("menu.wav")
MUSIC_BOSS = os.path.join("boss.mp3")
MUSIC_ROUND = os.path.join("round1.wav")