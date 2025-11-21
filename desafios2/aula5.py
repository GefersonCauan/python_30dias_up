# criar um clone do jogo T-Rex Game do Google Chrome usando Python e a biblioteca Pygame, simple e funcional.
# o jogo deve incluirobstaculos nao tao grossos, sem muita dificuldade.

import pygame
import random
import sys
from pygame.locals import QUIT, KEYDOWN, K_SPACE

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Game Clone")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = 300
GRAVITY = 0.6
JUMP_VELOCITY = -12
FONT = pygame.font.SysFont(None, 36)
SCORE = 0

class Dino:
    def __init__(self):
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = GROUND_HEIGHT - self.rect.height
        self.velocity_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = JUMP_VELOCITY
            self.is_jumping = True

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        if self.rect.y >= GROUND_HEIGHT - self.rect.height:
            self.rect.y = GROUND_HEIGHT - self.rect.height
            self.is_jumping = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle:
    def __init__(self):
        self.width = random.randint(20, 30)
        self.height = random.randint(30, 50)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = GROUND_HEIGHT - self.height
        self.speed = 4.8

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.reset()
        
    def reset(self):
        self.width = random.randint(20, 30)
        self.height = random.randint(30, 50)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = GROUND_HEIGHT - self.height   
        self.speed = 6

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def main():
    global SCORE
    dino = Dino()
    obstacles = [Obstacle()]
    score = 0
    running = True

    while running:
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (WIDTH, GROUND_HEIGHT), 2)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    dino.jump()

        dino.update()
        dino.draw(screen)

        if len(obstacles) == 0 or obstacles[-1].rect.x < WIDTH - 200:
            obstacles.append(Obstacle())

        for obstacle in obstacles:
            obstacle.update()
            obstacle.draw(screen)
            if dino.rect.colliderect(obstacle.rect):
                running = False

        obstacles = [ob for ob in obstacles if ob.rect.right > 0]

        score += 1
        score_text = FONT.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print(f"Game Over! Your Score: {score}")

if __name__ == "__main__":
    main() 