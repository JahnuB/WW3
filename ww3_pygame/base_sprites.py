import pygame
import fiona
from shapely.geometry import shape

class Sprite(pygame.sprite.Sprite):
    def __init__(self, size, color, position):
        super().__init__()
        self.image = pygame.Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = position
    
class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.image = pygame.image.load(self.image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, family, color, position, size, background=None, bold=False):
        super().__init__()
        self.color = color
        self.background = background
        self.text = text
        self.font = pygame.font.SysFont(family, int(size * 0.9), bold)
        self.image = self.font.render(text, True, color, background)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def assignNewText(self, text):
        if self.text != text:
            self.image = self.font.render(text, True, self.color, self.background)
            
class CountrySprite(pygame.sprite.Sprite):
    def __init__(self, path, position):
        super().__init__()
        self.position = position
        
        with fiona.open(path, 'r') as shp:
            for feature in shp:
                name = feature['properties'].get('NAME', 'unknown')
                geometry = shape(feature['geometry'])
                if name == "Russia": print(name)
                #print(feature)
                #if geometry.geom_type == 'Polygon':
                #    for point in geometry.exterior.coords: print(point)


class UISprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.updateElements = False
        self.elements = {}  #Key: description; Value: TextSprite/Sprite
    
    def update(self):
        if self.updateElements:
            self.doUpdateElements()
            self.updateElements = False

    def doUpdateElements(self):
        pass
    

class Button(TextSprite):
    def __init__(self, text, position):
        super().__init__(text, "georgia", (0,0,0), position, 30, (40, 40, 40))
        self.touching = False
        self.clicked = False
        
    def whenClicked(self):
        pass

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and not self.touching:
            self.image = self.font.render(self.text, True, self.color, (50, 50, 50))
            self.touching = True
        elif not self.rect.collidepoint(pygame.mouse.get_pos()) and self.touching:
            self.image = self.font.render(self.text, True, self.color, (40, 40, 40))
            self.touching = False
            
        left, right, middle = pygame.mouse.get_pressed()
        if self.touching and left and not self.clicked:
            self.clicked = True
            self.whenClicked()
        elif self.clicked and not left:
            self.clicked = False
            

class CheckBox(pygame.sprite.Sprite):
    def __init__(self): pass