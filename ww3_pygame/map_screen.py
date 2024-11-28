import pygame
from base_sprites import *
from buttons import PopulationButton, EconomyButton, RelationsButton, ResourcesButton, MilitaryButton
from country import Russia
from constants import colors

DEFAULT_FONT = "georgia"
DEFAULT_FONT_SIZE = 40

class MapUI:
    def __init__(self, dimens, country):
        #Name of country at top
        self.sprites = pygame.sprite.LayeredUpdates()
        self.country = country
        width, height = dimens
        self.countryName = TextSprite(self.country.name, DEFAULT_FONT, (255,255,255), (width / 2, 100), DEFAULT_FONT_SIZE + 10)
        self.populationButton = PopulationButton((width - 200, 200))
        self.populationText = TextSprite(f"{country.pop:,}", DEFAULT_FONT, (255,255,255), (self.populationButton.rect.centerx, self.populationButton.rect.y + 50), DEFAULT_FONT_SIZE - 10)
        self.economyButton = EconomyButton((width - 200, 300))
        self.economyText = TextSprite(country.currency + " " + f"{country.treasury["cash"][0]:,.2f}", DEFAULT_FONT, (255,255,255) , (self.economyButton.rect.centerx, self.economyButton.rect.y + 50), DEFAULT_FONT_SIZE - 10)
        #self.economyText = TextSprite(country.currency + " " + f"{sum(country.income.values()) - sum(country.budget.values()):,.2f}", DEFAULT_FONT, (0,255,0) if (sum(country.income.values()) - sum(country.budget.values())) > 0 else (255,0,0) , (self.economyButton.rect.centerx, self.economyButton.rect.y + 50), DEFAULT_FONT_SIZE - 10)
        self.relationsButton = RelationsButton((width - 200, 400))
        countryRelations = sum(country.relations.values()) / len(country.relations.values())
        self.relationsText = TextSprite("Good" if countryRelations >= 50 else "Bad", DEFAULT_FONT, (0,255,0) if countryRelations >= 50 else (255,0,0), (self.relationsButton.rect.centerx, self.relationsButton.rect.y + 50), DEFAULT_FONT_SIZE - 10)
        self.resourcesButton = ResourcesButton((width - 200, 500))
        self.militaryButton = MilitaryButton((width - 200, 600))
        self.militaryText = TextSprite(str(sum(self.country.recruits.values())), DEFAULT_FONT, (255,255,255), (self.militaryButton.rect.centerx, self.militaryButton.rect.y + 50), DEFAULT_FONT_SIZE - 10)
        self.sprites.add(self.countryName, 
                         self.populationButton, self.populationText,
                         self.economyButton, self.economyText,
                         self.relationsButton, self.relationsText,
                         self.resourcesButton,
                         self.militaryButton, self.militaryText)