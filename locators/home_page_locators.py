from constants.titles.navigation_menu import NavigationMenu


class HomePageLocators(str):
    HEADER_H1 = '//h1'
    HEADER_H2 = '//h2'
    HEADER_H3 = '//h3'
    LOGO = '//header/a/img'
    HEADER_H3_QUICK_LINK = '//div[@test-data="premium-ads"]//h3'
    HEADER_H3_WIDGET = '//section[@test-data="blog-posts"]//h3'
    META_DESCRIPTION = '//meta[@name="description"]'
    META_ROBOTS = '//meta[@name="robots"]'
    LINK_CANONICAL = '//link[@rel="canonical"]'
    FOOTER_LINKS = '//footer//a'
    MAIN_MENU_BUTTON = '//header/button'
    MENU_SALE = f'//header//nav//div[text()="{NavigationMenu.MENU_SALE}"]'
    MENU_RENT = f'//header//nav//div[text()="{NavigationMenu.MENU_RENT}"]'
    MENU_NEW = f'//header//nav//div[text()="{NavigationMenu.MENU_NEW}"]'
    MENU_ADVERTISEMENT = f'//header//nav//div[text()="{NavigationMenu.MENU_ADVERTISEMENT}"]'
    SUB_MENU = '//header//nav/a[text()='
    LOGIN = '//header/a[@href="?modal=prijava"]'
    LOGIN_DIALOG = '//div[@role="dialog"]'