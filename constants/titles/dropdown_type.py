from enum import Enum


class DropdownType(str, Enum):
    APARTMENT = "Stanovi"
    HOUSE = "Kuće"
    OFFICE = "Poslovni prostori"
    LOT = "Placevi"
    VEHICLESPOT = "Garaže/parking"
