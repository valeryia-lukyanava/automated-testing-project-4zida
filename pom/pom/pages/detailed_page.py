from pom.models.page import Page
from pom.pages.home_page import HomePage


class DetailedPage(HomePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
