import pytest

from pom.pages.home_page import HomePage
from pom.models.page import Page


@pytest.fixture(scope="function")
def home_page(page: Page) -> HomePage:
    return HomePage(page=page)
