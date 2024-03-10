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
        (20, "Vodič za kupovinu", f"{ui_config.production_base_url}/blog/vodic-za-kupovinu-nekretnine"),
        (21, "Lista agencija", f"{ui_config.production_base_url}/agencije"),
        (22, "Lista investitora", f"{ui_config.production_base_url}/investitori")
    ]
    SUB_MENU_RENT = [
        (1, "Izdavanje stanova", f"{ui_config.base_url}/izdavanje-stanova"),
        (2, "Izdavanje stanova Beograd", f"{ui_config.base_url}/izdavanje-stanova/beograd"),
        (3, "Izdavanje stanova Novi Sad", f"{ui_config.base_url}/izdavanje-stanova/novi-sad"),
        (4, "Izdavanje stanova Niš", f"{ui_config.base_url}/izdavanje-stanova/nis"),
        (5, "Izdavanje stanova Kragujevac", f"{ui_config.base_url}/izdavanje-stanova/kragujevac"),
        (6, "Izdavanje stanova Subotica", f"{ui_config.base_url}/izdavanje-stanova/subotica"),
        (7, "Izdavanje stanova Zrenjanin", f"{ui_config.base_url}/izdavanje-stanova/zrenjanin"),
        (8, "Izdavanje stanova Pančevo", f"{ui_config.base_url}/izdavanje-stanova/pancevo"),
        (9, "Izdavanje kuća", f"{ui_config.base_url}/izdavanje-kuca"),
        (10, "Izdavanje kuća Beograd", f"{ui_config.base_url}/izdavanje-kuca/beograd"),
        (11, "Izdavanje kuća Novi Sad", f"{ui_config.base_url}/izdavanje-kuca/novi-sad"),
        (12, "Izdavanje kuća Niš", f"{ui_config.base_url}/izdavanje-kuca/nis"),
        (13, "Izdavanje kuća Kragujevac", f"{ui_config.base_url}/izdavanje-kuca/kragujevac"),
        (14, "Izdavanje kuća Subotica", f"{ui_config.base_url}/izdavanje-kuca/subotica"),
        (15, "Izdavanje kuća Zlatibor", f"{ui_config.base_url}/izdavanje-kuca/zlatibor"),
        (16, "Izdavanje kuća Kopaonik", f"{ui_config.base_url}/izdavanje-kuca/kopaonik"),
        (17, "Izdavanje zemljišta", f"{ui_config.base_url}/izdavanje-placeva"),
        (18, "Izdavanje poslovnih prostora", f"{ui_config.base_url}/izdavanje-poslovnih-prostora"),
        (19, "Izdavanje garaža i parkinga", f"{ui_config.base_url}/izdavanje-garaza-i-parkinga"),
        (20, "Vodič za iznajmljivanje", f"{ui_config.production_base_url}/blog/vodic-za-iznajmljivanje-nekretnine"),
        (21, "Lista agencija", f"{ui_config.production_base_url}/agencije"),
        (22, "Apartmani i stan na dan", f"{ui_config.base_url}/izdavanje-stanova?period=na_dan")
    ]
    SUB_MENU_NEW = [
        (1, "Sva novogradnja", f"{ui_config.production_base_url}/novogradnja"),
        (2, "Novogradnja u Beogradu", f"{ui_config.production_base_url}/novogradnja/beograd"),
        (3, "Novogradnja u Novom Sadu", f"{ui_config.production_base_url}/novogradnja/novi-sad"),
        (4, "Novogradnja u Nišu", f"{ui_config.production_base_url}/novogradnja/nis"),
        (5, "Novogradnja na Zlatiboru", f"{ui_config.production_base_url}/novogradnja/zlatibor"),
        (6, "Novogradnja u Pančevu", f"{ui_config.production_base_url}/novogradnja/pancevo"),
        (7, "Novogradnja u Kragujevcu", f"{ui_config.production_base_url}/novogradnja/kragujevac"),
        (8, "Novogradnja u Vrnjačkoj Banji", f"{ui_config.production_base_url}/novogradnja/vrnjacka-banja"),
        (9, "Novogradnja u Subotici", f"{ui_config.production_base_url}/novogradnja/subotica"),
        (10, "Novogradnja u Jagodini", f"{ui_config.production_base_url}/novogradnja/jagodina"),
        (11, "Novogradnja na Divčibarama",
         f"{ui_config.production_base_url}/novogradnja/divcibare-okolne-lokacije-valjevo"),
        (12, "Novogradnja u Valjevu", f"{ui_config.production_base_url}/novogradnja/valjevo"),
        (13, "Novogradnja u Velikom Gradištu", f"{ui_config.production_base_url}/novogradnja/veliko-gradiste"),
        (14, "Novogradnja na Tari", f"{ui_config.production_base_url}/novogradnja/tara"),
        (15, "Novogradnja u Zrenjaninu", f"{ui_config.production_base_url}/novogradnja/zrenjanin"),
        (16, "Novogradnja u Loznici", f"{ui_config.production_base_url}/novogradnja/loznica"),
        (17, "Novogradnja u Rumi", f"{ui_config.production_base_url}/novogradnja/ruma"),
        (18, "Novogradnja u Bečeju", f"{ui_config.production_base_url}/novogradnja/becej"),
        (19, "Novogradnja u Prokuplju", f"{ui_config.production_base_url}/novogradnja/prokuplje"),
        (20, "Novogradnja u Vršcu", f"{ui_config.production_base_url}/novogradnja/vrsac"),
        (21, "Novogradnja u Inđiji", f"{ui_config.production_base_url}/novogradnja/indjija"),
        (22, "Novogradnja u Sremskoj Mitrovici",
         f"{ui_config.production_base_url}/novogradnja/gradske-lokacije-sremska-mitrovica"),
        (23, "Novogradnja u Novim Banovcima",
         f"{ui_config.production_base_url}/novogradnja/novi-banovci-okolne-lokacije-stara-pazova"),
        (24, "Vodič za stambeni kredit", f"{ui_config.production_base_url}/blog/sta-mi-je-potrebno-za-stambeni-kredit"),
        (25, "Lista investitora", f"{ui_config.production_base_url}/investitori")
    ]
    SUB_MENU_ADVERTISEMENT = [
        (1, "Cenovnik oglašavanja", f"{ui_config.production_base_url}/cenovnik"),
        (2, "Cenovnik oglašavanja za vlasnike - fizička lica", f"{ui_config.production_base_url}/cenovnik-za-vlasnike"),
        (3, "Cenovnik oglašavanja za vlasnike - pravna lica",
         f"{ui_config.production_base_url}/cenovnik-za-pravna-lica"),
        (4, "Cenovnik oglašavanja za agencije", f"{ui_config.production_base_url}/cenovnik-za-agencije"),
        (5, "Cenovnik oglašavanja za novogradnju", f"{ui_config.production_base_url}/cenovnik-za-investitore"),
        (6, "Cenovnik promocije projekata i oglašivača putem banera", f"{ui_config.production_base_url}/baneri")
    ]
    HIGHLIGHTS = [
        (1, "Pitaj pravnika", f"{ui_config.production_base_url}/pitaj-pravnika"),
        (2, "Kretanje cena kvadrata u Srbiji", f"{ui_config.production_base_url}/prosecna-cena-kvadrata-nekretnine"),
        (3, "Procena vrednosti nekretnine", f"{ui_config.production_base_url}/izracunaj-vrednost-nekretnine"),
        (4, "Isplativost", f"{ui_config.production_base_url}/isplativost-kupovina-ili-iznajmljivanje"),
        (5, "Kalkulator kredita", f"{ui_config.production_base_url}/kalkulator-stambenih-i-kes-kredita"),
        (6, "Kalkulator kreditne sposobnosti", f"{ui_config.production_base_url}/kreditna-sposobnost")
    ]
    BLOG = [
        (1, "Blog", f"{ui_config.production_base_url}/blog/"),
    ]
