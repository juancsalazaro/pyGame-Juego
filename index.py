import pygame
import sys

class Coin:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

def main_game():
    pygame.init()
    game_window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Aventura en las Alturas - Juego Principal")

    player_right_image = pygame.image.load("recursos/spritesPlayer/playerRight.png")
    player_left_image = pygame.image.load("recursos/spritesPlayer/playerLeft.png")
    
    player_rect = player_right_image.get_rect()
    player_rect.center = (120, 120)

    player_x = player_rect.x
    player_y = 120
    player_speed = 2
    jump_height = 10
    gravity = 0.5
    is_jumping = False

    jump_cooldown = 1.0
    time_since_last_jump = 0.0

    coin_image = pygame.image.load("recursos/coin.png")
    coins = [Coin(220, 50, coin_image), Coin(490, 300, coin_image), Coin(490, 370, coin_image), Coin(490, 440, coin_image), Coin(620, 190, coin_image), Coin(680, 190, coin_image)]

    font = pygame.font.Font("recursos/Anton-Regular.ttf", 24)

    text_lines = ["¡Obten los 6 coins para ganar"]
    line_height = 14

    text_surfaces = [font.render(line, True, (255, 255, 255)) for line in text_lines]
    text_rects = [surface.get_rect(center=(800 // 2, 20 + i * line_height)) for i, surface in enumerate(text_surfaces)]

    background_image = pygame.image.load("recursos/fondoGamePrincipal.png")
    platform_image1 = pygame.image.load("recursos/plataforma1.png")
    platform_image2 = pygame.image.load("recursos/plataforma1.png")
    platform_image3 = pygame.image.load("recursos/plataforma2.png")
    platform_image4 = pygame.image.load("recursos/plataforma3.png")
    platform_image5 = pygame.image.load("recursos/plataforma4.png")
    platform_image6 = pygame.image.load("recursos/plataforma4.png")
    platform_image7 = pygame.image.load("recursos/plataforma4.png")
    platform_image8 = pygame.image.load("recursos/plataforma3.png")
    platform_image1 = pygame.transform.scale(platform_image1, (100, 200))
    platform_image2 = pygame.transform.scale(platform_image2, (100, 200))
    platform_image3 = pygame.transform.scale(platform_image3, (150, 50))
    platform_image4 = pygame.transform.scale(platform_image3, (150, 50))
    platform_image5 = pygame.transform.scale(platform_image3, (50, 50))
    platform_image6 = pygame.transform.scale(platform_image3, (50, 50))
    platform_image7 = pygame.transform.scale(platform_image3, (50, 50))
    platform_image8 = pygame.transform.scale(platform_image3, (150, 50))
    platform_rect1 = platform_image1.get_rect(topleft=(60, 120))
    platform_rect2 = platform_image2.get_rect(topleft=(320, 140))
    platform_rect3 = platform_image3.get_rect(topleft=(600, 240))
    platform_rect4 = platform_image4.get_rect(topleft=(450, 500))
    platform_rect5 = platform_image5.get_rect(topleft=(720, 500))
    platform_rect6 = platform_image6.get_rect(topleft=(00, 500))
    platform_rect7 = platform_image7.get_rect(topleft=(250, 500))
    platform_rect8 = platform_image8.get_rect(topleft=(150, 500))

    is_facing_right = True

    score = 0
    font = pygame.font.Font(None, 36)  # Crea una fuente para el contador de monedas
    coin_count = 0 
    game_over = False
    running = True
    while running:
        current_time = pygame.time.get_ticks() / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for coin in coins:
                if player_rect.colliderect(coin.rect):
                    coins.remove(coin)
                    coin_count += 1
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            is_facing_right = False
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
            is_facing_right = True

        if keys[pygame.K_SPACE] and not is_jumping and on_platform:
            if current_time - time_since_last_jump >= jump_cooldown:
                is_jumping = True
                time_since_last_jump = current_time

                if is_facing_right:
                    player_x += 20
                else:
                    player_x -= 20

        if is_jumping:
            player_y -= jump_height
            jump_height -= gravity
            if player_y >= 120:
                is_jumping = False
                jump_height = 10
                player_y = 120

        on_platform = False
        if (player_rect.colliderect(platform_rect1) and player_y <= platform_rect1.top) or \
        (player_rect.colliderect(platform_rect2) and player_y <= platform_rect2.top) or \
        (player_rect.colliderect(platform_rect3) and player_y <= platform_rect3.top) or \
        (player_rect.colliderect(platform_rect4) and player_y <= platform_rect4.top) or \
        (player_rect.colliderect(platform_rect5) and player_y <= platform_rect5.top) or \
        (player_rect.colliderect(platform_rect6) and player_y <= platform_rect6.top) or \
        (player_rect.colliderect(platform_rect7) and player_y <= platform_rect7.top) or \
        (player_rect.colliderect(platform_rect8) and player_y <= platform_rect8.top):
            on_platform = True

        if not on_platform and player_y < 600:
            player_y += gravity

        player_rect.x = player_x
        player_rect.y = player_y

        game_window.blit(background_image, (0, 0))
        game_window.blit(platform_image1, platform_rect1)
        game_window.blit(platform_image2, platform_rect2)
        game_window.blit(platform_image3, platform_rect3)
        game_window.blit(platform_image4, platform_rect4)
        game_window.blit(platform_image5, platform_rect5)
        game_window.blit(platform_image6, platform_rect6)
        game_window.blit(platform_image7, platform_rect7)
        game_window.blit(platform_image8, platform_rect8)
        
        if player_rect.left < 0 or player_rect.right > 800 or player_rect.top < 0 or player_rect.bottom > 600:
            game_over = True
            font = pygame.font.Font("recursos/Anton-Regular.ttf", 42)
            game_over_text = font.render('¡Game Over!', True, (255, 0, 0))
            game_window.blit(game_over_text, (300, 250))


        for coin in coins:
                coin.draw(game_window)

        if is_facing_right:
            game_window.blit(player_right_image, player_rect.topleft)
        else:
            game_window.blit(player_left_image, player_rect.topleft)

        coin_text = font.render(f'Coins: {coin_count}', True, (255, 255, 255))
        game_window.blit(coin_text, (700, 10))

        for surface, rect in zip(text_surfaces, text_rects):
            game_window.blit(surface, rect)
        
        if coin_count >= 6:
            game_over = True
            font = pygame.font.Font("recursos/Anton-Regular.ttf", 42)
            game_over_text = font.render('¡Has ganado!', True, (255, 255, 255))
            game_window.blit(game_over_text, (300, 250))

        pygame.display.update()

        if game_over:
                pygame.time.delay(2000)
                pygame.quit()

    pygame.quit()

def main_menu():
    import pygame
    import sys

    pygame.init()

    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Aventura en las Alturas - Menú")

    background_image = pygame.image.load("recursos/fondoMenu.png")

    start_button_image = pygame.image.load("recursos/boton-inicio.png")
    exit_button_image = pygame.image.load("recursos/boton-exit.png")

    start_button_rect = start_button_image.get_rect()
    start_button_rect.center = (window_width // 2, window_height // 2 + 20)

    exit_button_rect = exit_button_image.get_rect()
    exit_button_rect.center = (window_width // 2, window_height // 2 + 120)

    font = pygame.font.Font("recursos/Anton-Regular.ttf", 42)

    text_lines = ["¡Bienvenido a", "Aventura en las Alturas!"]
    line_height = 42

    text_surfaces = [font.render(line, True, (255, 255, 255)) for line in text_lines]
    text_rects = [surface.get_rect(center=(window_width // 2, 150 + i * line_height)) for i, surface in enumerate(text_surfaces)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    main_game()
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))

        for surface, rect in zip(text_surfaces, text_rects):
            screen.blit(surface, rect)

        screen.blit(start_button_image, start_button_rect)
        screen.blit(exit_button_image, exit_button_rect)

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
