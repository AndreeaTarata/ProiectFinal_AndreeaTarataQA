import unittest
from selenium import webdriver
from selenium.webdriver import Keys
import locators


class TestArtelierHomePage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://arteliervamaveche.ro/')
        self.driver.maximize_window()

    # se verifica toate elementele din meniu. Codul face click pe fiecare in parte si se intoarce inapoi la homepage.
    def test_menu_is_functional(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        self.driver.find_element(*locators.HOME_REZERVA).click()
        self.driver.find_element(*locators.MENIU_RESTAURANT).click()
        self.driver.find_element(*locators.LOGO).click()
        self.driver.find_element(*locators.GALERIE_FOTO).click()
        self.driver.find_element(*locators.LOGO).click()
        self.driver.find_element(*locators.DESPRE_NOI).click()
        self.driver.find_element(*locators.LOGO).send_keys(Keys.CONTROL + Keys.HOME)
        self.driver.find_element(*locators.CONTACT).click()
        self.driver.find_element(*locators.CONTACT).send_keys(Keys.CONTROL + Keys.HOME)
        expected_url = "https://arteliervamaveche.ro/#contact"
        actual_url = self.driver.current_url
        self.assertTrue(expected_url, actual_url)

    # cerifica daca datele de contact sunt afisate
    def test_contact_info_is_displayed(self):
        date = self.driver.find_element(*locators.CONTACT_TEL)
        self.assertTrue(date.is_displayed(), 'CONTACT nu este afisat')

    # verifica daca linkul de facebook este corect
    def test_facebook_link(self):
        self.driver.find_element(*locators.FACEBOOK).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_facebook_url = "https://www.facebook.com/arteliervama"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_facebook_url)

    def tearDown(self) -> None:
        self.driver.quit()
