import pygame
from shapely.geometry import shape
from menus import *
from base_sprites import *
import events
from map_screen import *
from enum import Enum
from country import *
from constants import fonts
import datetime

class Screen(Enum):
    MAIN_MENU = 1
    GAME = 2
   
"""
def removeOtherMenus(sprites, r_menus):
    [sprites.remove(menu.sprites) for menu in r_menus if menu]
"""

def main():
    pygame.init()

    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    SCALE_FACTOR_X = SCREEN_WIDTH / 800     #Min supported width
    SCALE_FACTOR_Y = SCREEN_HEIGHT / 600    #Min supported height
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#, pygame.FULLSCREEN)

    clock = pygame.time.Clock()
    running = True

    sprites = pygame.sprite.LayeredUpdates()
    background = Sprite(screen.get_size(), (20,20,20), (SCREEN_WIDTH/ 2, SCREEN_HEIGHT / 2))
    sprites.add(background)

    #Escape and Options Menu
    escapeMenu = optionsMenu = None

    #Main Menu Setup
    mainMenu = MainMenu((SCREEN_WIDTH / 2, 100))
    sprites.add(mainMenu.sprites)
    currentScreen = Screen.MAIN_MENU

    #Test country setup
    #country = CountrySprite("ww3_pygame/country_data/countries_detailed/ne_10m_admin_0_countries.shp", (0,0))
    russia = Country("Russia", 130592302, "₽", 2529040952)

    #Main game specific menus
    popMenu = ecoMenu = relMenu = resMenu = milMenu = None
    #statMenus = [popMenu, ecoMenu, relMenu, resMenu, milMenu] #Change to dict

    #Map Screen
    mapScreen = MapUI((SCREEN_WIDTH, SCREEN_HEIGHT), russia)
    
    currentDay = datetime.datetime.now()
    currentDaySprite = TextSprite(str(currentDay.strftime("%x")), fonts.DEFAULT_TITLE, (255,255,255), (50 * SCALE_FACTOR_X, SCREEN_HEIGHT - (25 * SCALE_FACTOR_Y)), 25)
    
    currentFPS = TextSprite("", fonts.DEFAULT_TITLE, (255,255,255), (10,10), 15)
    
    while running:
        pygame.event.pump()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                    break
                case events.NEXTSCREEN:
                    match currentScreen:
                        case Screen.MAIN_MENU:        
                            sprites.remove(mainMenu.sprites)
                            currentScreen = Screen.GAME
                            sprites.add(mapScreen.sprites, currentDaySprite)
                            pygame.time.set_timer(events.INCREMENT_DAY, 1000) #Increments day by 1 every second
                            break
                    break
                case events.INCREMENT_DAY:
                    if currentScreen == Screen.GAME:
                        currentDay += datetime.timedelta(days=1)
                        currentDaySprite.assignNewText(str(currentDay.strftime("%x")))
                        russia.updateStats(1)
                        if resMenu: 
                            #resMenu.updateElements = True
                            resMenu.doUpdateElements()
                    break
                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_ESCAPE:
                            if currentScreen is not Screen.MAIN_MENU:       #Don't show escape menu in main menu
                                if escapeMenu: 
                                    sprites.remove(escapeMenu.sprites)
                                    escapeMenu = None
                                elif optionsMenu:
                                    escapeMenu = EscapeMenu((SCREEN_WIDTH, SCREEN_HEIGHT))
                                    sprites.remove(optionsMenu.sprites)
                                    sprites.add(escapeMenu.sprites)
                                    optionsMenu = None
                                else:
                                    escapeMenu = EscapeMenu((SCREEN_WIDTH, SCREEN_HEIGHT))
                                    sprites.add(escapeMenu.sprites)
                            break
                        case _:
                            #print("?")
                            pass
                    break
                case events.RESUME:
                    if escapeMenu:
                        sprites.remove(escapeMenu.sprites)
                        escapeMenu = None
                    break
                case events.OPTIONSMENU: 
                    if escapeMenu: 
                        sprites.remove(escapeMenu.sprites)
                        escapeMenu = None
                    optionsMenu = OptionsMenu((SCREEN_WIDTH, SCREEN_HEIGHT), sprites.has(currentFPS))
                    sprites.add(optionsMenu.sprites)
                    break
                case events.SHOW_FPS:
                    if optionsMenu.fpsButton.active:
                        sprites.add(currentFPS)
                        currentFPS.assignNewText(str(round(clock.get_fps())))
                    else: sprites.remove(currentFPS)
                    break
                case events.BACK:
                    if optionsMenu:
                        sprites.remove(optionsMenu.sprites)
                        optionsMenu = None
                        escapeMenu = EscapeMenu((SCREEN_WIDTH, SCREEN_HEIGHT))
                        sprites.add(escapeMenu.sprites)
                    else:
                        """
                        for menu in statMenus:
                            if menu: 
                                sprites.remove(menu.sprites)
                                menu = None
                        """
                        if popMenu: sprites.remove(popMenu.sprites)
                        if ecoMenu: sprites.remove(ecoMenu.sprites)
                        if relMenu: sprites.remove(relMenu.sprites)
                        if resMenu: sprites.remove(resMenu.sprites)
                        if milMenu: sprites.remove(milMenu.sprites)
                        popMenu = ecoMenu = relMenu = resMenu = milMenu = None
                        
                    break
                case events.POPULATION_MENU:
                    if not popMenu and currentScreen is Screen.GAME:
                        r_menus = [optionsMenu, escapeMenu, ecoMenu, relMenu, resMenu, milMenu]
                        #removeOtherMenus(sprites, r_menus)
                        [sprites.remove(menu.sprites) for menu in r_menus if menu]
                        for menu in r_menus: menu = None
                        popMenu = PopulationMenu((SCREEN_WIDTH, SCREEN_HEIGHT), russia)
                        sprites.add(popMenu.sprites)
                    break
                case events.ECONOMY_MENU:
                    if not ecoMenu and currentScreen is Screen.GAME:
                        r_menus = [optionsMenu, escapeMenu, popMenu, relMenu, resMenu, milMenu]
                        #removeOtherMenus(sprites, r_menus)
                        [sprites.remove(menu.sprites) for menu in r_menus if menu]
                        for menu in r_menus: menu = None
                        ecoMenu = EconomyMenu((SCREEN_WIDTH, SCREEN_HEIGHT), russia)
                        sprites.add(ecoMenu.sprites)
                    break
                case events.RELATIONS_MENU:
                    if not relMenu and currentScreen is Screen.GAME:
                        r_menus = [optionsMenu, escapeMenu, popMenu, ecoMenu, resMenu, milMenu]
                        #removeOtherMenus(sprites, r_menus)
                        [sprites.remove(menu.sprites) for menu in r_menus if menu]
                        for menu in r_menus: menu = None
                        relMenu = RelationsMenu((SCREEN_WIDTH, SCREEN_HEIGHT), russia)
                        sprites.add(relMenu.sprites)
                    break
                case events.RESOURCES_MENU:
                    if not resMenu and currentScreen is Screen.GAME:
                        r_menus = [optionsMenu, escapeMenu, popMenu, ecoMenu, relMenu, milMenu]
                        #removeOtherMenus(sprites, r_menus)
                        [sprites.remove(menu.sprites) for menu in r_menus if menu]
                        for menu in r_menus: menu = None
                        resMenu = ResourcesMenu((SCREEN_WIDTH, SCREEN_HEIGHT), russia)
                        sprites.add(resMenu.sprites)
                    break
                case events.MILITARY_MENU:
                    if not milMenu and currentScreen is Screen.GAME:
                        r_menus = [optionsMenu, escapeMenu, popMenu, ecoMenu, relMenu, resMenu]
                        #removeOtherMenus(sprites, r_menus)
                        [sprites.remove(menu.sprites) for menu in r_menus if menu]
                        for menu in r_menus: menu = None
                        milMenu = MilitaryMenu((SCREEN_WIDTH, SCREEN_HEIGHT), russia)
                        sprites.add(milMenu.sprites)
                    break
                # case events.:
                #     popMenu = FinancialMenu((SCREEN_WIDTH, SCREEN_HEIGHT), russia)
                #     sprites.add(popMenu, popMenu.sprites)
                #     currentScreen = Screen.POPULATION_MENU
                
        pygame.display.flip()
        clock.tick(60)
        
        if sprites.has(currentFPS) and str(round(clock.get_fps())) is not currentFPS.text: currentFPS.assignNewText(str(round(clock.get_fps())))
        
        sprites.update()
        rects = sprites.draw(screen)
        pygame.display.update(rects)
    
    pygame.quit()

if __name__ == "__main__":
    main()

    