import pygame
import random
import sys

# ================= ИНИЦИАЛИЗАЦИЯ =================
pygame.init()

WIDTH = 800
HEIGHT = 600

# Иконка (программно, 32×32)
icon = pygame.Surface((32, 32), pygame.SRCALPHA)
pygame.draw.polygon(icon, (20, 40, 80), [(16, 3), (3, 27), (29, 27)], 0)
pygame.draw.polygon(icon, (80, 140, 255), [(16, 5), (7, 25), (25, 25)], 0)
pygame.draw.polygon(icon, (200, 220, 255), [(16, 8), (11, 20), (21, 20)], 0)
pygame.draw.line(icon, (255, 255, 180), (16, 8), (16, 22), 3)
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простой космический шутер")

clock = pygame.time.Clock()
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (220, 40, 40)
GREEN = (60, 220, 80)
BLUE  = (60, 100, 240)

# Шрифт
font = pygame.font.SysFont("arial", 36)
small_font = pygame.font.SysFont("arial", 24)

# ================= КЛАССЫ =================

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, BLUE, [(30,0), (0,40), (60,40)])
        pygame.draw.polygon(self.image, (100,180,255), [(30,5), (10,35), (50,35)])
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT-20))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((12, 25), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (255, 255, 100), [(6,0), (0,25), (12,25)])
        pygame.draw.rect(self.image, (255, 200, 50), (4, 5, 4, 15))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = -12

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 50), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, RED, (0, 10, 60, 40))
        pygame.draw.circle(self.image, (255,100,100), (20,20), 10)
        pygame.draw.circle(self.image, (255,100,100), (40,20), 10)
        pygame.draw.polygon(self.image, GREEN, [(10,40),(20,50),(30,40)])
        pygame.draw.polygon(self.image, GREEN, [(30,40),(40,50),(50,40)])
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH-50), random.randint(-100, -50)))
        # Расширенная зона попадания (чтобы легче было попасть по бокам)
        self.rect.inflate_ip(30, 10)
        self.speed_y = random.uniform(1.5, 3.0)
        self.speed_x = random.uniform(-1.5, 1.5)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top > HEIGHT:
            self.kill()
            global game_over
            game_over = True


# ================= ГРУППЫ =================
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# ================= ПЕРЕМЕННЫЕ =================
score = 0
game_over = False
running = True

ENEMY_SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_SPAWN, 1200)

# ================= ЦИКЛ =================
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.shoot()
            if event.key == pygame.K_r and game_over:
                score = 0
                game_over = False
                enemies.empty()
                bullets.empty()
                player.rect.midbottom = (WIDTH//2, HEIGHT-20)

        elif event.type == ENEMY_SPAWN and not game_over:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

    if not game_over:
        all_sprites.update()

        # Попадания (расширенные rect'ы врагов уже помогают попадать по бокам)
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
            # print(f"Попадание! Счёт: {score}")  # раскомментируй, если хочешь видеть в консоли

    screen.fill(BLACK)
    all_sprites.draw(screen)

    score_text = font.render(f"СЧЁТ: {score}", True, WHITE)
    screen.blit(score_text, (20, 15))

    if game_over:
        go_text = font.render("ИГРА ОКОНЧЕНА", True, RED)
        restart_text = small_font.render("Нажми R чтобы начать заново", True, WHITE)
        screen.blit(go_text, go_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 30)))
        screen.blit(restart_text, restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 30)))

    pygame.display.flip()

pygame.quit()
sys.exit()