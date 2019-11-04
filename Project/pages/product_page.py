#!/usr/bin/python 
# -*- coding: utf-8 -*-

from .locators import *
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)
        
    def can_add_product_to_basket(self):
        self.open()                         # Переход на выбранную страницу
        self.go_to_basket_page()            # Найти и нажать кнопку ДОБАВИТЬ В КОРЗИНУ
        self.solve_quiz_and_get_code()      # Проверочный код
        self.check_basket_page(1)           # Проверка товара
        self.check_basket_page(2)           # Проверка цены товара

    def can_go_to_login_page(self):
        self.open()
        self.go_to_basket_page() 
        self.solve_quiz_and_get_code()  
        self.should_be_login_link()
        
    def should_see_login_link_on_product_page(self):
        self.open()
        self.should_be_login_link()
    