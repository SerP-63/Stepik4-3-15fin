#!/usr/bin/python 
# -*- coding: utf-8 -*-

from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert '/login/' in  self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"
        
    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.FIND_EMAIL), "field EMAIL not found"
        assert self.is_element_present(*LoginPageLocators.FIND_PSWD1), "field PSWD1 not found"
        assert self.is_element_present(*LoginPageLocators.FIND_PSWD2), "field PSWD2 not found"
        assert self.is_element_present(*LoginPageLocators.FIND_RSUBM), "button SUBMIT not found" 
        
        self.browser.find_element(*LoginPageLocators.FIND_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FIND_PSWD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIND_PSWD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIND_RSUBM).click()
        
    def cant_see_success_message(self):
        self.open()
        # по условию теста на странице элемента нет, тест ждет 4 сек и нормально проходит
        assert self.is_not_element_present(*MainPageLocators.PROD_TMP), "Элемент есть, но быть его не должно"

        