#!/usr/bin/python 
# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math

from .locators import BasePageLocators
from .locators import MainPageLocators

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def cant_see_product_in_basket(self):
        # переход по страницам через Альпы ))
        self.open()                        
        assert self.is_element_present(*BasePageLocators.CHECK_BASKKET_LINK), "Ошибка 404"
        #Переходит в корзину по кнопке в шапке сайта
        self.browser.find_element(*BasePageLocators.CHECK_BASKKET_LINK).click()
        assert self.is_not_element_present(*BasePageLocators.CHECK_BASKKET_NOT_EMPTY), "Увы, проверка корзины не прошла"
        assert self.check_message_empty(), "В это корзинке что-то ееесть"
        assert self.is_element_present(*BasePageLocators.PRODUCT_GO_HOME), "Безвыходное состояние"
        #Гость открывает главную страницу 
        self.browser.find_element(*BasePageLocators.PRODUCT_GO_HOME).click()
        assert not self.is_not_element_present(*BasePageLocators.PRODUCT_HOME), "Что-то пошло не так. Потеряли WELCOME"
    
    def check_basket_page(self, kod):
        # анализ содержимого корзины
        if kod == 1:
            pr_rmp  = self.browser.find_element(*MainPageLocators.PROD_TMP).text
            print(f"   Наименование товара: {self.tovar}")
            print(f"   Корзина: {pr_rmp}")
            assert pr_rmp == self.tovar, f"Другой товар - {pr_rmp} != {self.tovar}"
        else:
            assert self.is_element_present(*MainPageLocators.PRICE_TMP), "Не найден элемент <strong>ЦЕНА</strong>"
            pr_rmp  = self.browser.find_element(*MainPageLocators.PRICE_TMP).text
            print(f"   Цена для продажи: {self.price}")
            print(f"   Корзина: {pr_rmp}")
            assert pr_rmp == self.price, f"Цена отличается от изначальной - {pr_rmp} != {self.price}" 
            
    def check_message_empty(self):
        # Проверка сообщения на содержание слова empty
        language = self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
        text_Basket = self.browser.find_element(*BasePageLocators.CHECK_BASKKET).text
        if language == "en":
            if  "empty" in text_Basket:
                print("BASKET is EMPTY")
                return True
            else:
                print("BASKET is't EMPTY")
        else:
            print ('Язык страницы отличен от EN')
        return False            
        
    def go_to_login_page(self):
    # логинимся
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        
    def go_to_basket_page(self):
        # Проверим наличие кнопки ДОБАВИТЬ В КОРЗИНУ
        assert self.is_element_present(*MainPageLocators.BASKET_BTN), "BASKET_BTN is not presented"
        basket_btn = self.browser.find_element(*MainPageLocators.BASKET_BTN)
        
        # Сохраним для сравнения имя выбранного товара
        self.tovar  = self.browser.find_element(*MainPageLocators.PROD_NAME).text
        # Сохраним для сравнения стоимость того же товара
        self.price = self.browser.find_element(*MainPageLocators.PROD_PRICE).text

        basket_btn.click()        

    def is_disappeared(self, how, what, timeout=4):
    # элемент должен исчезнуть через определенное время
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
        
    def is_element_present(self, how, what):
    # найти элемент на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
    # ожидаем, что елемента нет и в ближайшее время и не будет
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
    # переход на указанную страницу
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
    
    def should_be_login_link(self):
    # Login link is presented
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
    # вычислить проверочный код
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            pass