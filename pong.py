import pygame
import random

# Configurações do jogo
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
PADDLE_SPEED = 5
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
WHITE = (255, 255, 255)

class PongGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pong Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset()

    def reset(self):
        self.paddle_a = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle_b = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.ball_speed_x = random.choice([BALL_SPEED_X, -BALL_SPEED_X])
        self.ball_speed_y = random.choice([BALL_SPEED_Y, -BALL_SPEED_Y])
        self.score_a = 0
        self.score_b = 0

    def update(self):
        # Movimentação das paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.paddle_a.top > 0:
            self.paddle_a.y -= PADDLE_SPEED
        if keys[pygame.K_s] and self.paddle_a.bottom < SCREEN_HEIGHT:
            self.paddle_a.y += PADDLE_SPEED
        if keys[pygame.K_UP] and self.paddle_b.top > 0:
            self.paddle_b.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and self.paddle_b.bottom < SCREEN_HEIGHT:
            self.paddle_b.y += PADDLE_SPEED

        # Movimentação da bola
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        # Colisões com as bordas
        if self.ball.top <= 0 or self.ball.bottom >= SCREEN_HEIGHT:
            self.ball_speed_y = -self.ball_speed_y

        # Colisões com as paletas
        if self.ball.colliderect(self.paddle_a) or self.ball.colliderect(self.paddle_b):
            self.ball_speed_x = -self.ball_speed_x

        # Pontuação
        if self.ball.left <= 0:
            self.score_b += 1
            self.reset()
        if self.ball.right >= SCREEN_WIDTH:
            self.score_a += 1
            self.reset()

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, WHITE, self.paddle_a)
        pygame.draw.rect(self.screen, WHITE, self.paddle_b)
        pygame.draw.ellipse(self.screen, WHITE, self.ball)
        score_display = self.font.render(f'{self.score_a} - {self.score_b}', True, WHITE)
        self.screen.blit(score_display, (SCREEN_WIDTH // 2 - score_display.get_width() // 2, 20))
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == '__main__':
    game = PongGame()
    game.run()
