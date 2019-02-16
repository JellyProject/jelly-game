import math

""" Parametres """
# hydrocarbures a ajouter a chaque pile pour chaque joueur
HYDROCARBON_STOCKS_PER_PLAYER = [(10, 3), (15, 2), (math.inf, 1)]

MAX_STATE_VALUE = 100
ENVIRONMENTAL_REGENERATION_LEVEL = 30

MAX_LENGTH_USER_NAME = 30
DEFAULT_USER_NAME = "MiguelDePatatas"
MAX_LENGTH_BUILDINGS_NAME = 50


""" Valeurs initiales """
ENVIRONMENTAL_INITIAL_VALUE = 100
SOCIAL_INITIAL_VALUE = 50
ECONOMIC_INITIAL_VALUE = 50

UM_INITIAL_STOCK = 10
HYDROCARBON_INITIAL_STOCK = 0

UM_INITIAL_PRODUCTION = 0
HYDROCARBON_INITIAL_PRODUCTION = 1
HYDROCARBON_INITIAL_CONSUMPTION = 0
POLLUTION_INITIAL_PRODUCTION = 1
ELECTRICITY_INITIAL_PRODUCTION = 0
FOOD_INITIAL_PRODUCTION = 0
WASTE_INITIAL_PRODUCTION = 0
