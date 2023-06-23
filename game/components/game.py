import pygame

from game.utils.constants import BG_1, BG_2, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.enemies.bosses.boss_handler import BossHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.power_ups.powerup_handler import PowerUpHandler
from game.utils import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.boss_handler = BossHandler()
        self.power_ups_handler = PowerUpHandler()
        self.number_deaths = 0
        self.score = 0
        self.scores = []
        self.round = 1

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = True
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()
            


    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.bullet_handler, self.enemy_handler, self.boss_handler)
            self.boss_handler.update(self.bullet_handler, self.round)
            self.enemy_handler.update(self.bullet_handler, self.boss_handler)
            self.bullet_handler.update(self.player, self.enemy_handler.get_list(), self.boss_handler.get_list())
            self.power_ups_handler.update(self.player)
            self.score = self.get_score()
            self.change_round()
            if not self.player.is_alive:
                pygame.time.delay(100)
                self.playing = False
                self.number_deaths += 1
            

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.boss_handler.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_ups_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        if self.round == 1:
            self.draw_round_background(BG_1)
        elif self.round == 2:
            self.draw_round_background(BG_2)

    def draw_round_background(self, BACKGROUND):
        image = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    

    def draw_menu(self):
        if self.number_deaths == 0:
            text, text_rect = text_utils.get_message("Press any key to start", 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
            self.screen.blit(self.player.image, ((SCREEN_WIDTH//2),  (SCREEN_HEIGHT//3)))
        else:
            text, text_rect = text_utils.get_message("GAME OVER", 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
            text_2, text_rect_2 = text_utils.get_message("Press any key to start again", 30, WHITE_COLOR, (SCREEN_WIDTH // 2), ((SCREEN_HEIGHT // 2) + 40) )
            self.screen.blit(text_2, text_rect_2)
            score, score_rect = text_utils.get_message(f"Your score this try was: {self.score}", 30, WHITE_COLOR, (SCREEN_WIDTH // 2), ((SCREEN_HEIGHT // 2) + 80) )
            self.screen.blit(score, score_rect)
            max_score, max_score_rect = text_utils.get_message(f"Your max score is: {max(self.scores)}", 30, WHITE_COLOR,  (SCREEN_WIDTH // 2), 40)
            self.screen.blit(max_score, max_score_rect)
            tries, tries_rect = text_utils.get_message(f"Number of Deaths: {self.number_deaths}", 30, WHITE_COLOR, (SCREEN_WIDTH // 2), (SCREEN_HEIGHT - 40))
            self.screen.blit(tries, tries_rect)
            self.screen.blit(self.player.image, ((SCREEN_WIDTH//2),  (SCREEN_HEIGHT//3)))

    def get_score(self):
        return self.enemy_handler.number_enemies_destroyed + (self.boss_handler.bosses_defetead * 100)
    
    def change_round(self):
        if self.score > 2 and self.boss_handler.bosses_defetead < 1:
            self.round = 2
        else:
            self.round = 1

    def draw_score(self):
        score, score_rect = text_utils.get_message(f"Your score is: {self.score}", 20 , WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)


    def reset(self):
        self.scores.append(self.score)
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.boss_handler.reset()
        self.power_ups_handler.reset()
        self.score = 0
        self.round = 1