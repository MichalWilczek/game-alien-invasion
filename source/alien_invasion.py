import sys
from time import sleep
import pygame
from source.settings import Settings
from source.game_stats import GameStats
from source.scoreboard import Scoreboard
from source.button import Button
from source.ship import Ship
from source.alien import Alien
from source.bullet import Bullet


class AlienInvasion:
    """General class dedicated to managing the resources and the way the game works"""

    def __init__(self, full_screen=False):
        """Game initialization and resources creation"""
        pygame.init()
        self.settings = Settings()

        if full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        # statistical data + scores data storage
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # button creation
        self.play_button = Button(self, "Game")

    def run_game(self):
        """Starting the main game loop"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

            # display of the last modified screen
            pygame.display.flip()

    def _check_events(self):
        """Respond to key presses and mouse events"""
        # waiting for a key or a mouse button to be pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """Starting the new game after clicking the "game" button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # reset score data
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # deleting game settings
            self.settings.initialize_dynamic_settings()

            # hiding the mouse cursor
            pygame.mouse.set_visible(False)

            # deleting statistical data
            self.stats.reset_stats()
            self.stats.game_active = True

            # deleting the content of aliens and bullets lists
            self.aliens.empty()
            self.bullets.empty()

            # creation of a new fleet and centering of the ship
            self._create_fleet()
            self.ship.center_ship()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Reaction for the collision between alien and bullet"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # getting rid of the available bullets and creation of a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # incrementing the level number
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """Definition of the full fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Position update of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # checking collisions between aliens and ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # searching for aliens reaching the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """The adequate reaction of alien reaches an edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Moving all the fleet down and change of direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Reaction when alien hits the ship"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Verification if any alien reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # the same as in case of hitting the ship with an alien
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # displaying the score data
        self.sb.show_score()

        # displaying the "game" button only when the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # creating and starting the game
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
