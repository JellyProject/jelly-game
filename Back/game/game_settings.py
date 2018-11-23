import math

""" Parametres """
# hydrocarbures a ajouter a chaque pile pour chaque joueur
HYDROCARBON_STOCKS_PER_PLAYER = Hydrocarbon_stock((10, 3), (15, 2), (inf, 1))

MAX_STATE_VALUE = 100
ENVIRONMENTAL_REGENERATION_LEVEL = 30


""" Valeurs initiales """
ENVIRONMENTAL_INITIAL_VALUE = 100
SOCIAL_INITIAL_VALUE = 50
ECONOMICAL_INITIAL_VALUE = 50

UM_INITIAL_STOCK = 0
HYDROCARBONS_INITIAL_STOCK = 0
POLLUTION_INITIAL_STOCK = 0

UM_INITIAL_PRODUCTION = 0
HYDROCARBONS_INITIAL_PRODUCTION = 0
POLLUTION_INITIAL_PRODUCTION = 0
ELECTRICITY_INITIAL_PRODUCTION = 0
FOOD_INITIAL_PRODUCTION = 0
WASTE_INITIAL_PRODUCTION = 0
