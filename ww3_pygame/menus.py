from base_sprites import Sprite, Button, TextSprite, UISprite
from constants import colors, fonts
from buttons import *
import pygame

DEFAULT_FONT = "segoeui"
DEFAULT_FONT_SIZE = 40

class MainMenu:
    def __init__(self, pos):
        x, y = pos
        self.sprites = pygame.sprite.LayeredUpdates()
        self.mmImage = base_sprites.ImageSprite("ww3_pygame/images/russia-map3.png", (x, y + 200))
        self.title = base_sprites.TextSprite("World War 3", fonts.COUNTRY_TITLE_FONT, (255,255,255), pos, 50)
        self.bgColor = (0,0,0)
       
        self.startButton = StartButton((x, y + 200))
        self.quitButton = QuitButton((x, y + 300))
        
        #Add all sprites to sprite list
        self.sprites.add(self.mmImage, self.title, self.startButton, self.quitButton)

class EscapeMenu:
    def __init__(self, dimens):
        width, height = dimens
        x = width / 2
        y = height / 2
        self.sprites = pygame.sprite.LayeredUpdates()
        self.boxBg = Sprite((300, 400), colors.DEFAULT_MENU_BG, (x, y))
        self.title = TextSprite("World War 3", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 40), DEFAULT_FONT_SIZE)
        self.resumeButton = ResumeButton((self.boxBg.rect.centerx + 10, self.boxBg.rect.centery - 10))
        self.optionsButton = OptionsButton((self.boxBg.rect.centerx + 10, self.boxBg.rect.centery + 50))
        self.quitButton = QuitButton((self.boxBg.rect.centerx + 10, self.boxBg.rect.centery + 110))
        self.sprites.add(self.boxBg, self.title, self.resumeButton, self.optionsButton, self.quitButton)
        
class OptionsMenu:
    def __init__(self, dimens, fpsActive):
        width, height = dimens
        x = width / 2
        y = height / 2
        self.sprites = pygame.sprite.LayeredUpdates()
        self.boxBg = Sprite((y, x), colors.DEFAULT_MENU_BG, (x, y))
        self.backButton = BackButton((self.boxBg.rect.centerx, self.boxBg.rect.height + self.boxBg.rect.y - 40))
        self.title = TextSprite("Options", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.centerx, self.boxBg.rect.y + 50), DEFAULT_FONT_SIZE + 10)
        self.fpsButton = ShowFPSButton((self.boxBg.rect.centerx, self.boxBg.rect.y + 150), fpsActive)
        self.sprites.add(self.boxBg, self.title, self.fpsButton, self.backButton)
        
class PopulationMenu(base_sprites.UISprite):
    def __init__(self, dimens, country):
        width, height = dimens
        x = width / 2
        y = height / 2
        self.country = country
        self.sprites = pygame.sprite.LayeredUpdates()
        
        self.boxBg = Sprite((y + 200, x), colors.DEFAULT_MENU_BG, (x,y))
        
        self.countryName = TextSprite(self.country.name, DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 50), DEFAULT_FONT_SIZE + 20)
        
        self.populationText = TextSprite("Population", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 100), DEFAULT_FONT_SIZE - 10)
        self.populationTextNumber = TextSprite(f"{self.country.pop:,}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 100), DEFAULT_FONT_SIZE - 10)
        
        self.happinessText = TextSprite("Happiness", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 200), DEFAULT_FONT_SIZE)
        
        self.financialText = TextSprite("Financial", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 250), DEFAULT_FONT_SIZE - 10)
        self.financialTextNumber = TextSprite(str(self.country.popStats['avg_h']['financial']), DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 250), DEFAULT_FONT_SIZE - 10)
        
        self.safetyText = TextSprite("Safety", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 300), DEFAULT_FONT_SIZE - 10)
        self.safetyTextNumber = TextSprite(str(self.country.popStats['avg_h']['safety']), DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 300), DEFAULT_FONT_SIZE - 10)
        
        self.educationText = TextSprite("Education", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 350), DEFAULT_FONT_SIZE - 10)
        self.educationTextNumber = TextSprite(str(self.country.popStats['avg_h']['education']), DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 350), DEFAULT_FONT_SIZE - 10)
        
        self.healthText = TextSprite("Health", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 400), DEFAULT_FONT_SIZE - 10)
        self.healthTextNumber = TextSprite(str(self.country.popStats['avg_h']['health']), DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 400), DEFAULT_FONT_SIZE - 10)
        
        self.leadershipText = TextSprite("Leadership", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 450), DEFAULT_FONT_SIZE - 10)
        self.leadershipTextNumber = TextSprite(str(self.country.popStats['avg_h']['leadership']), DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 450), DEFAULT_FONT_SIZE - 10)
        
        self.backButton = BackButton((self.boxBg.rect.x + self.boxBg.rect.width - 100, self.boxBg.rect.y + self.boxBg.rect.height - 100))
        
        self.sprites.add(self.boxBg, self.countryName, self.backButton, self.populationText, self.populationTextNumber, self.happinessText, 
                         self.financialText, self.financialTextNumber,
                         self.safetyText, self.safetyTextNumber,
                         self.educationText, self.educationTextNumber,
                         self.healthText, self.healthTextNumber,
                         self.leadershipText, self.leadershipTextNumber)
        
class EconomyMenu(base_sprites.UISprite):
    def __init__(self, dimens, country):
        super().__init__()
        width, height = dimens
        x = width / 2
        y = height / 2
        self.country = country
        self.sprites = pygame.sprite.LayeredUpdates()
        
        self.boxBg = Sprite((y + 200, x), colors.DEFAULT_MENU_BG, (x,y))
        self.backButton = BackButton((self.boxBg.rect.x + self.boxBg.rect.width - 100, self.boxBg.rect.y + self.boxBg.rect.height - 100))
        
        self.countryName = TextSprite(self.country.name + " Economy", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 50), DEFAULT_FONT_SIZE + 20)
        """
        self.bankBalanceText = TextSprite("Bank Balance", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 100), DEFAULT_FONT_SIZE - 10)
        self.bankBalanceTextNumber = TextSprite(self.country.currency + " " + f"{self.country.treasury["cash"][0]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 100), DEFAULT_FONT_SIZE - 10)
        
        self.incometaxRateText = TextSprite("Income Tax Rate", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 150), DEFAULT_FONT_SIZE - 15)
        self.incometaxRateTextNumber = TextSprite(str(self.country.taxrates['income_tax']) + "%", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 150), DEFAULT_FONT_SIZE - 10)
        self.salestaxRateText = TextSprite("Sales Tax Rate", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 200), DEFAULT_FONT_SIZE - 15)
        self.salestaxRateTextNumber = TextSprite(str(self.country.taxrates['sales_tax']) + "%", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 200), DEFAULT_FONT_SIZE - 10)
        
        self.incomeText = TextSprite("Income", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 250), DEFAULT_FONT_SIZE)
        
        self.incometaxText = TextSprite("Income Tax", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 200, self.boxBg.rect.y + 300), DEFAULT_FONT_SIZE - 20)
        self.incometaxTextNumber = TextSprite(self.country.currency + " " + f"{self.country.income["income_tax"]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 300), DEFAULT_FONT_SIZE - 20)
        self.salestaxText = TextSprite("Sales Tax", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 200, self.boxBg.rect.y + 325), DEFAULT_FONT_SIZE - 20)
        self.salestaxTextNumber = TextSprite(self.country.currency + " " + f"{self.country.income["sales_tax"]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 325), DEFAULT_FONT_SIZE - 20)
        
        self.expensesText = TextSprite("Expenses", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 400), DEFAULT_FONT_SIZE)
        
        self.socialText = TextSprite("Social Programs", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 200, self.boxBg.rect.y + 450), DEFAULT_FONT_SIZE - 20)
        self.socialTextNumber = TextSprite(self.country.currency + " " + f"{self.country.budget["social_programs"]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 450), DEFAULT_FONT_SIZE - 20)
        self.maintenanceText = TextSprite("Maintenance", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 200, self.boxBg.rect.y + 475), DEFAULT_FONT_SIZE - 20)
        self.maintenanceTextNumber = TextSprite(self.country.currency + " " + f"{self.country.budget["maintenance"]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 475), DEFAULT_FONT_SIZE - 20)
        self.resourceMiningText = TextSprite("Resource Mining", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 200, self.boxBg.rect.y + 500), DEFAULT_FONT_SIZE - 20)
        self.resourceMiningTextNumber = TextSprite(self.country.currency + " " + f"{self.country.budget["resource_mining"]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 500), DEFAULT_FONT_SIZE - 20)
        self.militaryText = TextSprite("Military", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 200, self.boxBg.rect.y + 525), DEFAULT_FONT_SIZE - 20)
        self.militaryTextNumber = TextSprite(self.country.currency + " " + f"{self.country.budget["military"]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 525), DEFAULT_FONT_SIZE - 20)
        """
        self.elements["bank_balance"] = [
            TextSprite("Bank Balance", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 100), DEFAULT_FONT_SIZE - 10),
            TextSprite(self.country.currency + " " + f"{self.country.treasury["cash"][0]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 100), DEFAULT_FONT_SIZE - 10)
        ]
        for taxRate in self.country.taxrates.keys():
            self.elements[taxRate] = [
                TextSprite(' '.join([i.capitalize() for i in taxRate.split('_')]), DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 100 + (50 * len(self.elements))), DEFAULT_FONT_SIZE - 15),
                TextSprite(str(self.country.taxrates[taxRate]) + "%", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 100 + (50 * len(self.elements))), DEFAULT_FONT_SIZE - 10)
            ]
        self.elements["income_title"] = TextSprite("Income", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 100 + (50 * len(self.elements))), DEFAULT_FONT_SIZE)
        for income in self.country.income.keys():
            self.elements[income] = [
                TextSprite(' '.join([i.capitalize() for i in income.split('_')]), DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 150, self.boxBg.rect.y + 100 + (50 * len(self.elements))), DEFAULT_FONT_SIZE - 15),
                TextSprite(self.country.currency + " " + f"{self.country.income[income]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 150, self.boxBg.rect.y + 100 + (50 * len(self.elements))), DEFAULT_FONT_SIZE - 10)
            ]
        self.elements["expenses_title"] = TextSprite("Expenses", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 100 + (50 * len(self.elements))), DEFAULT_FONT_SIZE)
        for expense in self.country.budget.keys():
            self.elements[expense] = [
                TextSprite(' '.join([i.capitalize() for i in expense.split('_')]), DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + 200, self.boxBg.rect.y + 100 + (50 * len(self.elements))), DEFAULT_FONT_SIZE - 20),
                TextSprite(self.country.currency + " " + f"{self.country.budget[expense]:,.2f}", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 100 + (50 * len(self.elements))), DEFAULT_FONT_SIZE - 20)
            ]
        self.sprites.add(self.boxBg, self.backButton, self.countryName,
                         self.elements.values())
        

class RelationsMenu:
    def __init__(self, dimens, country):
        width, height = dimens
        x = width / 2
        y = height / 2
        self.country = country
        self.sprites = pygame.sprite.LayeredUpdates()
        
        self.boxBg = Sprite((y + 200, x), colors.DEFAULT_MENU_BG, (x,y))
        self.backButton = BackButton((self.boxBg.rect.x + self.boxBg.rect.width - 100, self.boxBg.rect.y + self.boxBg.rect.height - 100))
        
        self.sprites.add(self.boxBg, self.backButton)

class ResourcesMenu(base_sprites.UISprite):
    def __init__(self, dimens, country):
        super().__init__()
        width, height = dimens
        x = width / 2
        y = height / 2
        self.country = country
        self.sprites = pygame.sprite.LayeredUpdates()
        
        self.boxBg = Sprite((y + 200, x), colors.DEFAULT_MENU_BG, (x,y))
        self.backButton = BackButton((self.boxBg.rect.x + self.boxBg.rect.width - 100, self.boxBg.rect.y + self.boxBg.rect.height - 100))
        
        self.countryName = TextSprite(self.country.name + " Resources", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 50), DEFAULT_FONT_SIZE + 20)
        """
        self.oilText = TextSprite("Oil", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 150), DEFAULT_FONT_SIZE - 10)
        self.oilTextNumber = TextSprite(str(self.country.treasury["oil"][0]) + " (+" + str(self.country.treasury["oil"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 150), DEFAULT_FONT_SIZE - 10)
        
        self.coalText = TextSprite("Coal", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 200), DEFAULT_FONT_SIZE - 10)
        self.coalTextNumber = TextSprite(str(self.country.treasury["coal"][0]) + " (+" + str(self.country.treasury["coal"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 200), DEFAULT_FONT_SIZE - 10)
        
        self.woodText = TextSprite("Wood", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 250), DEFAULT_FONT_SIZE - 10)
        self.woodTextNumber = TextSprite(str(self.country.treasury["wood"][0]) + " (+" + str(self.country.treasury["wood"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 250), DEFAULT_FONT_SIZE - 10)
        
        self.goldText = TextSprite("Gold", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 300), DEFAULT_FONT_SIZE - 10)
        self.goldTextNumber = TextSprite(str(self.country.treasury["gold"][0]) + " (+" + str(self.country.treasury["gold"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 300), DEFAULT_FONT_SIZE - 10)
        
        self.steelText = TextSprite("Steel", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 350), DEFAULT_FONT_SIZE - 10)
        self.steelTextNumber = TextSprite(str(self.country.treasury["steel"][0]) + " (+" + str(self.country.treasury["steel"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 350), DEFAULT_FONT_SIZE - 10)
        
        self.ironText = TextSprite("Iron", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 400), DEFAULT_FONT_SIZE - 10)
        self.irontextNumber = TextSprite(str(self.country.treasury["iron"][0]) + " (+" + str(self.country.treasury["iron"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 400), DEFAULT_FONT_SIZE - 10)
        
        self.foodText = TextSprite("Food", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 450), DEFAULT_FONT_SIZE - 10)
        self.foodTextNumber = TextSprite(str(self.country.treasury["food"][0]) + " (+" + str(self.country.treasury["food"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 450), DEFAULT_FONT_SIZE - 10)
        
        self.stoneText = TextSprite("Stone", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 500), DEFAULT_FONT_SIZE - 10)
        self.stoneTextNumber = TextSprite(str(self.country.treasury["stone"][0]) + " (+" + str(self.country.treasury["stone"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 500), DEFAULT_FONT_SIZE - 10)
        
        self.clayText = TextSprite("Clay", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 550), DEFAULT_FONT_SIZE - 10)
        self.clayTextNumber = TextSprite(str(self.country.treasury["clay"][0]) + " (+" + str(self.country.treasury["clay"][1]) + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 550), DEFAULT_FONT_SIZE - 10)
        """
        
        for treasure in self.country.treasury.keys():
            if treasure == "cash": continue
            self.elements[treasure] = [
                TextSprite(treasure.capitalize(), DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 150 + (50 * len(self.elements))), DEFAULT_FONT_SIZE - 10),
                TextSprite(f"{self.country.treasury[treasure][0]:,}"+ " (+" + f"{self.country.treasury[treasure][1]:,}" + ")", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 150 + (50 * len(self.elements))), DEFAULT_FONT_SIZE - 10)
            ]
        self.sprites.add(self.boxBg, self.backButton,
                         self.countryName, self.elements.values())

    def doUpdateElements(self):
        for treasure in self.elements.keys():
            self.elements[treasure][1].assignNewText(f"{self.country.treasury[treasure][0]:,}"+ " (+" + f"{self.country.treasury[treasure][1]:,}" + ")")
        


class MilitaryMenu:
    def __init__(self, dimens, country):
        width, height = dimens
        x = width / 2
        y = height / 2
        self.country = country
        self.sprites = pygame.sprite.LayeredUpdates()
        
        self.boxBg = Sprite((y + 200, x), colors.DEFAULT_MENU_BG, (x,y))
        self.backButton = BackButton((self.boxBg.rect.x + self.boxBg.rect.width - 100, self.boxBg.rect.y + self.boxBg.rect.height - 100))
        
        self.countryName = TextSprite(self.country.name + " Military", DEFAULT_FONT, colors.DEFAULT_TEXT_COLOR, (self.boxBg.rect.centerx, self.boxBg.rect.y + 50), DEFAULT_FONT_SIZE + 20)
        
        self.infoTextSprites = {}
        for recruit in self.country.recruits.keys():
            self.infoTextSprites[recruit] = [
                TextSprite(recruit.capitalize(), DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 150 + (50 * len(self.infoTextSprites))), DEFAULT_FONT_SIZE - 10),
                TextSprite(f"{self.country.recruits[recruit]:,}", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 150 + (50 * len(self.infoTextSprites))), DEFAULT_FONT_SIZE - 10)
            ]
        
        for arsenal in self.country.arsenal.keys():
            self.infoTextSprites[arsenal] = [
                TextSprite(arsenal.capitalize(), DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + 200, self.boxBg.rect.y + 150 + (50 * len(self.infoTextSprites))), DEFAULT_FONT_SIZE - 10),
                TextSprite(f"{self.country.arsenal[arsenal]:,}", DEFAULT_FONT, (0,0,0), (self.boxBg.rect.x + self.boxBg.rect.width - 200, self.boxBg.rect.y + 150 + (50 * len(self.infoTextSprites))), DEFAULT_FONT_SIZE - 10)
            ]
        
        
        self.sprites.add(self.boxBg, self.backButton, self.countryName,
                         self.infoTextSprites.values())