from enum import Enum


class HomePageLocators(str, Enum):
    META_ROBOTS = '//meta[@name="robots"]'
    LINK_CANONICAL = '//link[@rel="canonical"]'
    SEARCH_FORM = '//div[@test-data="search-form"]'
