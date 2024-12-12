import pygame
import fiona
from constants import fonts, colors
from shapely.geometry import shape

class Sprite(pygame.sprite.Sprite):
    def __init__(self, size, color, position, name):
        super().__init__()
        self.image = pygame.Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.name = name
    
class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image, position, name):
        super().__init__()
        self.image = image
        self.image = pygame.image.load(self.image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.name = name

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, family, color, position, size, name, background=None):
        super().__init__()
        self.color = color
        self.background = background
        self.text = text
        self.font = pygame.font.Font(family, size)
        self.image = self.font.render(text, True, color, background)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.name = name
        
    def __init__(self, text):
        super().__init__()
        self.color = colors.DEFAULT_TEXT_COLOR
        self.text = text
        self.font = pygame.font.Font(fonts.DEFAULT_UI_FONT_SIZE, fonts.DEFAULT_UI_FONT_SIZE)
        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        self.name = text

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
                

class ButtonSprite(TextSprite):
    def __init__(self, text, position, name):
        super().__init__(text, fonts.DEFAULT_TITLE, (0,0,0), position, 30, (40, 40, 40), name)
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
            
#ISprite contains anything interactable that is drawn on the screen.
#UISprite can contain other UISprites.
class UISprite(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.width, self.height = size
        self.updateElements = False
        self.elements = {
            "top_l": [],
            "top_c": [],
            "top_r" : [],
            "cen_l": [],
            "cen_C": [],
            "cen_r" : [],
            "bot_l": [],
            "bot_c": [],
            "bot_c" : []
        }
    
    #Default is add to bottom of UI
    def addElement(self, element, name, pos):
        #Need to change for elements on the same line
        if isinstance(element, TextSprite):
            self.elements[pos] = TextSprite(' '.join([i.capitalize() for i in name.split('_')]),
                                             fonts.DEFAULT_TITLE,
                                             colors.DEFAULT_TEXT_COLOR,
                                             self.getNewPos(pos),
                                             fonts.DEFAULT_UI_FONT_SIZE,
                                             name)
    
    def getNewPos(self, pos):
        elPos = self.elements[pos]
        return elPos[len(elPos - 1)].rect.y + 50 #change later

    
    def update(self):
        if self.updateElements:
            self.doUpdateElements()
            self.updateElements = False

    def doUpdateElements(self):
        pass

class CheckBox(pygame.sprite.Sprite):
    def __init__(self): pass