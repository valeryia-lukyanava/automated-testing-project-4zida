import time

import allure

from constants.titles.dropdown_subtypes import DropdownSubtypes
from constants.titles.dropdown_types import DropdownTypes
from constants.titles.titles import Titles
from constants.web_elements.attributes import Attributes
from locators.search_form_locators import SearchFormLocators
from pom.page_factory.button import Button
from pom.page_factory.component import Component
from pom.page_factory.form import Form
from pom.page_factory.input import Input
from pom.page_factory.option import Option
from pom.page_factory.select import Select
from pom.page_factory.text import Text
from pom.page_factory.title import Title
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
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_LAND,
            name="Search Form Dropdown Option 'Placevi'"
        )
        self.type_lot_option = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_LAND_OPTION,
            name="Search Form Select Option 'Placevi'"
        )
        self.type_vehiclespot = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_GARAGE,
            name="Search Form Dropdown Option 'Garaže/parking'"
        )
        self.type_vehiclespot_option = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_TYPE_GARAGE_OPTION,
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
        self.location_multiselect = Input(
            page, locator=SearchFormLocators.SEARCH_FORM_LOCATION_INPUT,
            name="Search Form 'Upiši lokaciju' Multiselect"
        )
        self.location_autocomplete_drawer = Component(
            page, locator=SearchFormLocators.SEARCH_FORM_LOCATION_AUTOCOMPLETE_DRAWER,
            name="Search Form 'Upiši lokaciju' AutoComplete Drawer"
        )
        self.location_autocomplete_drawer_option = Option(
            page, locator=SearchFormLocators.SEARCH_FORM_LOCATION_AUTOCOMPLETE_DRAWER_OPTION,
            name="Search Form 'Upiši lokaciju' AutoComplete Drawer Option"
        )
        self.location_selected_locations_number = Title(
            page, locator=SearchFormLocators.SEARCH_FORM_SELECTED_LOCATIONS_NUMBER,
            name="Search Form 'Upiši lokaciju' Selected Locations Number"
        )
        self.checkbox_label = Title(
            page, locator=SearchFormLocators.SEARCH_FORM_CHECKBOX_LABEL,
            name="Search Form Checkbox Label"
        )
        self.checkbox = Button(
            page, locator=SearchFormLocators.SEARCH_FORM_CHECKBOX_BUTTON,
            name="Search Form Checkbox"
        )
        self.type_options = {
            DropdownTypes.APARTMENT: (
                self.type_apartment,
                self.type_apartment_option,
                list(DropdownSubtypes.NUMBER_OF_ROOMS.keys())[0]
            ),
            DropdownTypes.HOUSE: (
                self.type_house,
                self.type_house_option,
                list(DropdownSubtypes.FLOORS.keys())[0]
            ),
            DropdownTypes.OFFICE: (
                self.type_office,
                self.type_office_option,
                list(DropdownSubtypes.PLACE_TYPE.keys())[0]
            ),
            DropdownTypes.LAND: (
                self.type_lot,
                self.type_lot_option,
                list(DropdownSubtypes.LAND_TYPE.keys())[0]
            ),
            DropdownTypes.GARAGE: (
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
    def select_type(self, value: str, subcategory: str = None):
        self.combobox_type.click()
        type_button = self.type_options[value][0]
        type_option = self.type_options[value][1]
        type_button.click()
        type_option.should_have_attribute(Attributes.SELECTED)
        if subcategory is not None:
            for option in self.page.find_xpath(SearchFormLocators.SEARCH_FORM_COMBOBOX_SUBTYPE_OPTION).list:
                if option.web_element.text == subcategory:
                    option.should().be_clickable()
                    option.click()
            self.combobox_subtype_input.click()

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
        self.select_type(property_type)
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
        with allure.step('Check Subcategory Options are opened automatically'):
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

    @allure.step('Check selecting locations: {locations}')
    def select_locations(self, input_values: list, locations: list):
        self.location_multiselect.should_be_visible()
        n = len(locations)
        for i in range(0, n):
            with allure.step(f'User input: {input_values[i]}'):
                self.location_multiselect.fill(input_values[i])
                self.location_autocomplete_drawer.should_be_visible()
                self.location_autocomplete_drawer_option.should_be_visible()
                location_option = self.page.get_xpath(
                    f'{SearchFormLocators.SEARCH_FORM_LOCATION_AUTOCOMPLETE_DRAWER_OPTION_BY_TEXT}="{locations[i]}"]')
                location_option.scroll_to_element()
                location_option.should().be_visible()
                location_option.click()
                self.location_multiselect.click()
                selected_location_title = self.page.get_xpath(
                    f'{SearchFormLocators.SEARCH_FORM_SELECTED_LOCATIONS_TITLE}="{locations[i]}"]')
                selected_location_title.should().be_visible()
                self.location_multiselect.click()
        self.location_selected_locations_number.should_be_visible()
        self.location_selected_locations_number.should_have_text(f"{Titles.SEARCH_FORM_SELECTED_LOCATIONS_TITLE}{n}")
        self.location_multiselect.should_have_attribute_value(Attributes.PLACEHOLDER, ", ".join(locations))
        self.form.click()
        self.search.should_be_visible()

    def check_checkbox_new_buildings_only(self, category, checkbox_is_available, subcategory):
        self.tab_sale.click()
        self.select_type(category, subcategory)
        self.checkbox_label.should_be_visible()
        self.checkbox_label.should_have_text(Titles.NEW_BUILDINGS_ONLY)
        if checkbox_is_available:
            self.checkbox.should_have_attribute_value(Attributes.DATA_STATE, Attributes.UNCHECKED)
            self.checkbox.click()
            self.checkbox.should_have_attribute_value(Attributes.DATA_STATE, Attributes.CHECKED)
        else:
            self.checkbox.should_have_attribute_value(Attributes.DATA_STATE, Attributes.CHECKED)
            self.checkbox.should_have_attribute(Attributes.DATA_DISABLED)
        self.search.click()
