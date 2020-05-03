import pygame
from pygame import *

import color

class InputBox:

    def __init__(self, y, x, w, h, border, text = '', block = False):

        pygame.init()

        self.border = border
        self.rect = pygame.Rect(x + self.border, y + self.border, w, h)
        self.color = color.WHITE
        self.text = text
        self.font = pygame.font.Font(None, 70)
        self.txt_surface = self.font.render(text, True, color.BLACK)
        self.active = False
        self.block = block

    # Handle events
    def handle_event(self, event):

        if not self.block:

            # If the user clicked on the input_box rect
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.rect.collidepoint((event.pos)):

                    # Toggle the active variable
                    self.active = not self.active

                else:
                    self.active = False

                # Change the current color of the input box
                self.color = color.BLACK if self.active else color.WHITE

            # Test and update value of input box
            elif event.type == pygame.KEYDOWN:

                if self.active:

                    # Reset input box
                    if event.key == pygame.K_0 or event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        self.text = ''
                        text = pygame.K_0

                    # Change value of the input box
                    elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                        self.text = event.unicode
                        text = self.text

                    else:
                        text = None
                    
                    # Return (value, y_pos, x_pos)
                    if text is not None:
                        return (text, self.rect.y - self.border, self.rect.x - self.border)

        return (None, None, None)

    # Update value setting color
    def update(self, valid):

        self.txt_surface = self.font.render(self.text, True, color.GREEN if valid else color.RED)

    # Draw input box
    def draw(self, screen):

        # Blit the rect.
        pygame.draw.rect(screen, color.WHITE, self.rect)

        if self.active:
            pygame.draw.rect(screen, self.color, self.rect, 1)

        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 36 - self.border, self.rect.y + 32 - self.border))