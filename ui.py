import pygame


class UI:
    def __init__(self, surface):

        # Setup
        self.display_surface = surface

        # Health
        self.health_bar = pygame.image.load('graphics/ui/health_bar.png').convert_alpha()
        self.health_bar_topleft = (49, 30)
        self.bar_max_width = 164
        self.bar_height = 12

        # Coins
        self.coin = pygame.image.load('graphics/ui/coin.png').convert_alpha()
        # 50, 61
        self.coin_rect = self.coin.get_rect(topleft=(30, 42))
        self.font = pygame.font.Font('graphics/ui/ARCADEPI.TTF', 25)

        # Key

    def show_health(self, current_health, full):
        self.display_surface.blit(self.health_bar, (20, 20))
        current_health_ratio = current_health / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width, self.bar_height))
        pygame.draw.rect(self.display_surface, '#FFFFFF', health_bar_rect)

    def show_coins(self, amount):
        self.display_surface.blit(self.coin, self.coin_rect)
        coin_amount_surf = self.font.render(str(amount), False, 'white')
        coin_amount_rect = coin_amount_surf.get_rect(midleft=(self.coin_rect.right + 4, self.coin_rect.centery))
        self.display_surface.blit(coin_amount_surf, coin_amount_rect)

    def show_key(self, amount):
        key_amount_surf = self.font.render(str(amount), False, 'white')
        key_amount_rect = key_amount_surf.get_rect(midleft=(50, 120))
        self.display_surface.blit(key_amount_surf, key_amount_rect)
