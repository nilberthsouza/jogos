import pygame
import random

# Configurações do jogo
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Jogo da Cobrinha')
        self.clock = pygame.time.Clock()

    def reset(self):
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.apple = self.spawn_apple()

    def spawn_apple(self):
        while True:
            x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return x, y

    def run(self):
        self.reset()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.direction = UP
            elif keys[pygame.K_DOWN]:
                self.direction = DOWN
            elif keys[pygame.K_LEFT]:
                self.direction = LEFT
            elif keys[pygame.K_RIGHT]:
                self.direction = RIGHT

            head_x, head_y = self.snake[0]
            if self.direction == UP:
                head_y -= 1
            elif self.direction == DOWN:
                head_y += 1
            elif self.direction == LEFT:
                head_x -= 1
            elif self.direction == RIGHT:
                head_x += 1

            if (head_x, head_y) in self.snake or head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
                self.reset()

            self.snake.insert(0, (head_x, head_y))

            if (head_x, head_y) == self.apple:
                self.apple = self.spawn_apple()
            else:
                self.snake.pop()

            self.screen.fill(WHITE)
            for segment in self.snake:
                pygame.draw.rect(self.screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(self.screen, RED, (self.apple[0] * GRID_SIZE, self.apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.display.flip()
            self.clock.tick(10)

if __name__ == '__main__':
    game = SnakeGame()
    game.run()
