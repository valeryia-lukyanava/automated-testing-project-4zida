import time

import allure

from constants.titles.dropdown_subtypes import DropdownSubtypes
from constants.titles.dropdown_types import DropdownType
from constants.web_elements.attributes import Attributes
from constants.web_elements.tags import Tags
from locators.search_form_locators import SearchFormLocators
from pom.page_factory.button import Button
from pom.page_factory.component import Component
from pom.page_factory.form import Form
from pom.page_factory.input import Input
from pom.page_factory.option import Option
from pom.page_factory.select import Select
from pom.page_factory.text import Text
from pom.pages.base_page import BasePage
from pom.models.page import Page


class SearchForm(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.form = Form(
            page, locator=SearchFormLocators.SEARCH_FORM, name='Search Form'
        )
        self.tab_sale = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_TAB_SALE,
            name="Search Form Tab 'Prodaja'"
        )
        self.tab_rent = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_TAB_RENT,
            name="Search Form Tab 'Izdavanje'"
        )
        self.combobox_type = Select(
            page, locator=SearchFormLocators.SEARCH_FORM_COMBOBOX_TYPE,
            name="Search Form Dropdown 'Tip'"
        )
        self.combobox_type_input = Input(
            page, locator=SearchFormLocators.SEARCH_FORM_COMBOBOX_TYPE_INPUT,
            name="Search Form Dropdown 'Tip' Input"
        )
        self.type_apartment = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_APARTMENT,
            name="Search Form Dropdown Option 'Stanovi'"
        )
        self.type_apartment_option = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_APARTMENT_OPTION,
            name="Search Form Select Option 'Stanovi'"
        )
        self.type_house = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_HOUSE,
            name="Search Form Dropdown Option 'Kuće'"
        )
        self.type_house_option = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_HOUSE_OPTION,
            name="Search Form Select Option 'Kuće'"
        )
        self.type_office = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_OFFICE,
            name="Search Form Dropdown Option 'Poslovni prostori'"
        )
        self.type_office_option = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_OFFICE_OPTION,
            name="Search Form Select Option 'Poslovni prostori'"
        )
        self.type_lot = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_LOT,
            name="Search Form Dropdown Option 'Placevi'"
        )
        self.type_lot_option = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_LOT_OPTION,
            name="Search Form Select Option 'Placevi'"
        )
        self.type_vehiclespot = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_VEHICLESPOT,
            name="Search Form Dropdown Option 'Garaže/parking'"
        )
        self.type_vehiclespot_option = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_VEHICLESPOT_OPTION,
            name="Search Form Select Option 'Garaže/parking'"
        )
        self.price_to = Input(
            page, locator=SearchFormLocators.SEARCH_FORM_PRICE_TO_INPUT,
            name="Search Form Input 'Cena do'"
        )
        self.m2_from = Input(
            page, locator=SearchFormLocators.SEARCH_FORM_M2_FROM_INPUT,
            name="Search Form Input 'm2 od'"
        )
        self.search = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_SEARCH_BUTTON,
            name="Search Form Button 'Traži'"
        )
        self.combobox_subtype_title = Text(
            page, locator=SearchFormLocators.SEARCH_FORM_COMBOBOX_SUBTYPE_TITLE,
            name="Search Form Combobox Subcategory Title"
        )
        self.combobox_subtype_select = Select(
            page, locator=SearchFormLocators.SEARCH_FORM_COMBOBOX_SUBTYPE_SELECT,
            name="Search Form Combobox Subcategory Select"
        )
        self.combobox_subtype_options = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_COMBOBOX_SUBTYPE_OPTION,
            name="Search Form Combobox Subcategory Option"
        )
        self.combobox_subtype_input = Input(
            page, locator=SearchFormLocators.SEARCH_FORM_COMBOBOX_SUBTYPE_INPUT,
            name="Search Form Dropdown Subcategoty Input"
        )

        self.type_options = {
            DropdownType.APARTMENT: (
                self.type_apartment,
                self.type_apartment_option,
                list(DropdownSubtypes.NUMBER_OF_ROOMS.keys())[0]
            ),
            DropdownType.HOUSE: (
                self.type_house,
                self.type_house_option,
                list(DropdownSubtypes.FLOORS.keys())[0]
            ),
            DropdownType.OFFICE: (
                self.type_office,
                self.type_office_option,
                list(DropdownSubtypes.PLACE_TYPE.keys())[0]
            ),
            DropdownType.LOT: (
                self.type_lot,
                self.type_lot_option,
                list(DropdownSubtypes.LAND_TYPE.keys())[0]
            ),
            DropdownType.VEHICLESPOT: (
                self.type_vehiclespot,
                self.type_vehiclespot_option,
                list(DropdownSubtypes.GARAGE_PARKING_TYPE.keys())[0]
            ),
        }

    @allure.step('Click Tab "Izdavanje" and check it is selected while Tab "Prodaja" is deselected')
    def click_rent_tab_and_check_attributes(self):
        self.tab_rent.click()
        self.tab_rent.should_have_attribute_value(Attributes.ARIA_SELECTED, "true")
        self.tab_sale.should_have_attribute_value(Attributes.ARIA_SELECTED, "false")

    @allure.step('Click Tab "Prodaja" and check it is selected while Tab "Izdavanje" is deselected')
    def click_sale_tab_and_check_attributes(self):
        self.tab_sale.click()
        self.tab_sale.should_have_attribute_value(Attributes.ARIA_SELECTED, "true")
        self.tab_rent.should_have_attribute_value(Attributes.ARIA_SELECTED, "false")

    @allure.step('Select option "{value}" in dropdown "Tip"')
    def select_type(self, value: str):
        self.combobox_type.click()
        type_button = self.type_options[value][0]
        type_option = self.type_options[value][1]
        type_button.click()
        type_option.should_have_attribute(Tags.SELECTED)

    @allure.step('Check that dropdown "Tip" has the value {value}')
    def check_type_value(self, value: str):
        self.combobox_type_input.should_have_text(value)
        subtype_title = self.type_options[value][2]
        self.combobox_subtype_title.should_have_text(subtype_title)

    @allure.step('Check Dropdown "Tip" for all options')
    def check_combobox_type(self):
        for value in self.type_options:
            self.select_type(value)
            self.check_type_value(value)

    @allure.step('Fill in Search Form')
    def fill_in_search_form_and_click_search(self, property_type: str, price_to: str, m2_from: str):
        self.select_type(type_button=self.type_options[property_type][0],
                         type_option=self.type_options[property_type][1])
        self.price_to.should_be_visible()
        self.price_to.fill(price_to)
        self.m2_from.should_be_visible()
        self.m2_from.fill(m2_from)
        self.search.click()

    @allure.step('Check Combobox Subcategory for "Tip" = "{type_value}"')
    def check_combobox_subtype(self, type_value: str, subtype: str, subtype_values: tuple):
        self.combobox_subtype_title.should_be_visible()
        subtype_title = self.type_options[type_value][2]
        self.combobox_subtype_title.should_have_text(subtype_title)
        self.combobox_subtype_select.should_be_visible()
        self.check_subtype_options(subtype, subtype_values)

    @allure.step('Check selecting values in Combobox Subcategory "{subtype}"')
    def check_subtype_options(self, subtype: str, subtype_values: tuple):
        self.combobox_subtype_options.should_have_values(subtype_values)
        for option in self.page.find_xpath(SearchFormLocators.SEARCH_FORM_COMBOBOX_SUBTYPE_OPTION).list:
            option.should().be_clickable()
            option.click()
        self.combobox_subtype_input.click()
        self.combobox_subtype_input.should_have_text(', '.join([str(x) for x in subtype_values]))
