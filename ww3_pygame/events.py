import pygame

#Custom events
NEXTSCREEN = pygame.USEREVENT + 1   #Switch screen
RESUME = pygame.USEREVENT + 2       #Resume game
OPTIONSMENU = pygame.USEREVENT + 3  #Options screen
SHOW_FPS = pygame.USEREVENT + 4     #Toggle FPS counter
BACK = pygame.USEREVENT + 5         #Go back

POPULATION_MENU = pygame.USEREVENT + 5
ECONOMY_MENU = pygame.USEREVENT + 6
RELATIONS_MENU = pygame.USEREVENT + 7
RESOURCES_MENU = pygame.USEREVENT + 8
MILITARY_MENU = pygame.USEREVENT + 9

INCREMENT_DAY = pygame.USEREVENT + 99