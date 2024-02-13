from enum import Enum


class UIRoutes(str, Enum):
    SALE_APARTMENTS = '/prodaja-stanova'
    SALE_HOUSES = '/prodaja-kuca'
    RENT_APARTMENTS = '/izdavanje-stanova'
    RENT_HOUSES = '/izdavanje-kuca'
