#!/usr/bin/python 
# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        
    def cant_see_success_message_after_adding_product_to_basket(self):
        self.open()
        self.go_to_basket_page() 
        self.solve_quiz_and_get_code()      # Проверочный код
        # по условию теста на странице элемент присутствует, тест ожидаемо валится без паузы
        assert self.is_not_element_present(*MainPageLocators.PROD_TMP), "Элемент есть"
        
    def cant_see_success_message(self):
        self.open()
        # по условию теста на странице элемента нет, тест ждет 4 сек и нормально проходит
        assert self.is_not_element_present(*MainPageLocators.PROD_TMP), "Элемент есть, но быть его не должно"
        
    def message_disappeared_after_adding_product_to_basket(self):
        self.open()
        self.go_to_basket_page()
        self.solve_quiz_and_get_code()      # Проверочный код
        # по условию теста на странице элемент присутствует, тест ждет 4 сек, элемент не исчезает, тест валится
        assert self.is_disappeared(*MainPageLocators.PROD_TMP), "элемент не исчезает"
        
    def should_see_login_link_on_product_page(self):
        page.open()
        page.should_be_login_link()

        

