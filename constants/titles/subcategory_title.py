from enum import Enum


class SubCategoryTitle(str, Enum):
    ROOM_NUMBER = "Broj soba"
    FLOOR = "Etaž"
    PLACE_TYPE = "Tip lokala"
    LOT = "Placevi"
    VEHICLESPOT = "Garaže/parking"
