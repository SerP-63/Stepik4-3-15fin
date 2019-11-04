#!/usr/bin/python 
# -*- coding: utf-8 -*-

import pytest
from .pages.main_page import MainPage
from .pages.locators import *


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):     
        page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
        page.cant_see_product_in_basket()
