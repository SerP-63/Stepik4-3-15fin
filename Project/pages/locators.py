#!/usr/bin/python 
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class MainPageLocators:
    BASKET_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"
    PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PROD_NAME  = (By.CSS_SELECTOR, ".product_main h1")
    PROD_PRICE = (By.CSS_SELECTOR, "p.price_color")
    FIND_NAME = (By.CSS_SELECTOR, ".alert-success div strong")
    PROD_TMP  = (By.XPATH, './/*[@id="messages"]/div[1]/div/strong')
    PRICE_TMP = (By.XPATH, './/*[@id="messages"]/div[3]/div/p[1]/strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    CHECK_BASKKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    CHECK_BASKKET = (By.CSS_SELECTOR, "#content_inner>p")
    CHECK_BASKKET_NOT_EMPTY = (By.CSS_SELECTOR, ".table")
    PRODUCT_GO_HOME = (By.CSS_SELECTOR, ".breadcrumb>li>a")
    PRODUCT_HOME = (By.CSS_SELECTOR, ".sub-header")
    

class LoginPageLocators:
    LOGIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    FIND_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    FIND_PSWD1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    FIND_PSWD2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    FIND_RSUBM = (By.CSS_SELECTOR, "button[name='registration_submit']")
