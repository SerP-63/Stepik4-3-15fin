#!/usr/bin/python 
# -*- coding: utf-8 -*-

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.main_page import MainPage

from .pages.locators import *

import pytest
import time


@pytest.mark.xfail
class TestFirstGroup:

    @staticmethod
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        # тест ожидаемо валится без паузы
        # XFAIL
        page = MainPage(browser, MainPageLocators.BASKET_PAGE_URL)
        page.cant_see_success_message_after_adding_product_to_basket()
        
    @staticmethod
    def test_guest_cant_see_success_message(browser):
        # тест ждет 4 сек и нормально проходит
        # XPASS
        page = MainPage(browser, MainPageLocators.BASKET_PAGE_URL)
        page.cant_see_success_message()

    @staticmethod
    def test_message_disappeared_after_adding_product_to_basket(browser):
        # тест ждет 4 сек, элемент не исчезает, тест валится
        # XFAIL
        page = MainPage(browser, MainPageLocators.BASKET_PAGE_URL)
        page.message_disappeared_after_adding_product_to_basket()

    @staticmethod
    def test_guest_should_see_login_link_on_product_page(browser):
        # Login link is presented
        # XPASS
        page = ProductPage(browser, MainPageLocators.PRODUCT_PAGE_URL)
        page.should_see_login_link_on_product_page()


# noinspection PyRedundantParentheses,PyRedundantParentheses,PyRedundantParentheses
@pytest.mark.need_review
class TestSecondGroup:

    @staticmethod
    def test_guest_can_go_to_login_page_from_product_page(browser):
        page = ProductPage(browser, MainPageLocators.BASKET_PAGE_URL)
        page.can_go_to_login_page()

    @staticmethod
    def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        page = ProductPage(browser, MainPageLocators.PRODUCT_PAGE_URL)
        page.cant_see_product_in_basket()

    @pytest.mark.xfail
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
                                     ,"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
                                     ,"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        # тест ожидоемо валится на 7 странице
        # XPASS, XFAIL, XPASS
        page = ProductPage(browser, link)
        page.can_add_product_to_basket()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        print('# 1. Открыть страницу регистрации')
        # noinspection PyPep8Naming
        loginPage = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_URL)
        loginPage.open()
        loginPage.should_be_login_page()

        print('# 2. Зарегистрировать нового пользователя')
        email = str(time.time()) + "@fakemail.org"
        password = "Pass" + str(time.time())[11:19] + "word"
        loginPage.register_new_user(email, password)
        
        print('# 3. Проверить, что пользователь залогинен')
        loginPage.should_be_authorized_user()

        yield

    # Тест отключен согласно требованиям п.4.3.14
    @staticmethod
    def _test_user_cant_see_success_message(browser):
        page = LoginPage(browser, MainPageLocators.BASKET_PAGE_URL)
        page.cant_see_success_message()

    @staticmethod
    def test_user_can_add_product_to_basket(browser):
        page = ProductPage(browser, MainPageLocators.BASKET_PAGE_URL)
        page.can_add_product_to_basket()
