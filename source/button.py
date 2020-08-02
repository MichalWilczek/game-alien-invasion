import pygame.font


class Button:

    def __init__(self, alien_invasion, msg):
        """Button attributes initialization"""
        self.screen = alien_invasion.screen
        self.screen_rect = self.screen.get_rect()

        # button characteristics definition
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # creation of centered rectangle
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # message displayed by the button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Message placement in the generated picture and text centering in the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Showing empty button and, then, the message inside of it"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
