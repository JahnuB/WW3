import pygame
from base_sprites import ButtonSprite
from events import *
        
class StartButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Start Game", pos)
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(NEXTSCREEN))
        
class ResumeButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Resume", pos)
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(RESUME))
        
class OptionsButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Options", pos)
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(OPTIONSMENU))
        
class ShowFPSButton(ButtonSprite):
    def __init__(self, pos, active):
        super().__init__("Toggle FPS Counter", pos)
        self.active = active
        self.image = self.font.render(self.text, True, self.color, (40, 40, 40) if not self.active else (150, 40, 40))
        
    def whenClicked(self):
        self.active = not self.active
        print(self.active)
        if self.active: self.background = (150, 40, 40)
        else: self.background = (40, 40, 40)
        pygame.event.post(pygame.event.Event(SHOW_FPS))
    
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and not self.touching:
            self.image = self.font.render(self.text, True, self.color, (50, 50, 50) if not self.active else (160, 50, 50))
            self.touching = True
        elif not self.rect.collidepoint(pygame.mouse.get_pos()) and self.touching:
            self.image = self.font.render(self.text, True, self.color, (40, 40, 40) if not self.active else (150, 40, 40))
            self.touching = False
            
        left, right, middle = pygame.mouse.get_pressed()
        if self.touching and left and not self.clicked:
            self.clicked = True
            self.whenClicked()
            self.image = self.font.render(self.text, True, self.color, (100, 100, 100) if not self.active else (255, 100, 100))
        elif self.clicked and not left:
            self.image = self.font.render(self.text, True, self.color, (50, 50, 50) if not self.active else (160, 50, 50))
            self.clicked = False
        
class BackButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Back", pos)
        self.prevScreen = None
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(BACK))

        
class QuitButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Quit", pos)
    
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        
#Map Screen specific buttons

class PopulationButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Population", pos)
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(POPULATION_MENU))

class EconomyButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Economy", pos)
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(ECONOMY_MENU))

class RelationsButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Relations", pos)
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(RELATIONS_MENU))

class ResourcesButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Resources", pos)
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(RESOURCES_MENU))

class MilitaryButton(ButtonSprite):
    def __init__(self, pos):
        super().__init__("Military", pos)
        
    def whenClicked(self):
        pygame.event.post(pygame.event.Event(MILITARY_MENU))