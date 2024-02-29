from config import UIConfig


class NavigationSubMenu(list):
    ui_config = UIConfig()
    SUB_MENU_SALE = [
        (1, "Prodaja stanova", f"{ui_config.base_url}/prodaja-stanova"),
        (2, "Prodaja stanova Beograd", f"{ui_config.base_url}/prodaja-stanova/beograd"),
        (3, "Prodaja stanova Novi Sad", f"{ui_config.base_url}/prodaja-stanova/novi-sad"),
        (4, "Prodaja stanova Niš", f"{ui_config.base_url}/prodaja-stanova/nis"),
        (5, "Prodaja stanova Kragujevac", f"{ui_config.base_url}/prodaja-stanova/kragujevac"),
        (6, "Prodaja stanova Subotica", f"{ui_config.base_url}/prodaja-stanova/subotica"),
        (7, "Prodaja stanova Zrenjanin", f"{ui_config.base_url}/prodaja-stanova/zrenjanin"),
        (8, "Prodaja stanova Pančevo", f"{ui_config.base_url}/prodaja-stanova/pancevo"),
        (9, "Prodaja kuća", f"{ui_config.base_url}/prodaja-kuca"),
        (10, "Prodaja kuća Beograd", f"{ui_config.base_url}/prodaja-kuca/beograd"),
        (11, "Prodaja kuća Novi Sad", f"{ui_config.base_url}/prodaja-kuca/novi-sad"),
        (12, "Prodaja kuća Niš", f"{ui_config.base_url}/prodaja-kuca/nis"),
        (13, "Prodaja kuća Kragujevac", f"{ui_config.base_url}/prodaja-kuca/kragujevac"),
        (14, "Prodaja kuća Subotica", f"{ui_config.base_url}/prodaja-kuca/subotica"),
        (15, "Prodaja kuća Zrenjanin", f"{ui_config.base_url}/prodaja-kuca/zrenjanin"),
        (16, "Prodaja kuća Pančevo", f"{ui_config.base_url}/prodaja-kuca/pancevo"),
        (17, "Prodaja zemljišta", f"{ui_config.base_url}/prodaja-placeva"),
        (18, "Prodaja poslovnih prostora", f"{ui_config.base_url}/prodaja-poslovnih-prostora"),
        (19, "Prodaja garaža i parkinga", f"{ui_config.base_url}/prodaja-garaza-i-parkinga"),
        (20, "Vodič za kupovinu", f"{ui_config.base_url}/blog/vodic-za-kupovinu-nekretnine/"),
        (21, "Lista agencija", f"{ui_config.base_url}/agencije"),
        (22, "Lista investitora", f"{ui_config.base_url}/investitori")
    ]
    SUB_MENU_RENT = []
    SUB_MENU_NEW = []
    SUB_MENU_ADVERTISEMENT = []
