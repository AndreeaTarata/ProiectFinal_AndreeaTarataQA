import unittest

from selenium import webdriver

import locators


class TestArtelierRezervare(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://arteliervamaveche.ro/')
        self.driver.maximize_window()

    # se verifica daca numarul de camere afisate este 4
    def test_room_with_balcony_are_4(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        camere = len(self.driver.find_elements(*locators.IMAGINI))
        assert camere == 4

    # se verifica daca textul "Rezervarea mea este afisat"
    def test_text_rezervarea_mea_is_dispayed(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        rezervare = self.driver.find_element(*locators.REZERVAREA_MEA).text
        text_rezervare = 'Rezervarea mea'
        self.assertTrue(rezervare, text_rezervare)

    # negativ testing. Se verifica functionalitatea codului promotional cand nu este introdusa nicio valoare
    def test_insert_empty_cod_promotional(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        self.driver.find_element(*locators.COD_PROMOTIONAL_BTN).click()
        cod_gol = self.driver.find_element(*locators.COD_PROMO_ERROR).text
        self.assertEqual(cod_gol, 'Codul promotional nu a fost gasit!', 'Campul este obligatoriu')

    # se verifica functionalitatea login cand se introduc numar de rezervare si parola false
    def test_false_authentication(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        self.driver.find_element(*locators.AUTENTIFICARE).click()
        self.driver.find_element(*locators.NR_REZERVARE).send_keys('1')
        self.driver.find_element(*locators.PAROLA).send_keys('1')
        self.driver.find_element(*locators.IDENTIFICA).click()
        text_eroare_aut = self.driver.find_element(*locators.TEXT_AUTENT).text
        self.assertTrue(text_eroare_aut, 'Rezervarea nu a fost identificata.')

    # se verifica ca linkul pe care suntem este acelasi cu cel pe care trebuie sa fim cand accesam "Rezerva acum"
    def test_check_booking_link(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        expected_url = "https://artelier.pynbooking.direct/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, f'Expected URL: {expected_url}, Actual URL: {actual_url}')

    # itereaza prin valorile de la limbi pentru a verifica daca sunt toate afisate asa cum este cerut
    def test_all_languages_are_present(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        limbi_existente = self.driver.find_elements(*locators.LIMBI_DISPONIBILE)
        for limba in limbi_existente:
            limba.click()
            limba_selectata = self.driver.find_element(*locators.LIMBI_DISPONILE).get_attribute()
            self.assertIn(limba_selectata, ["ro", "en", "fr", "de", "it"])

    # Se verifica daca media notelor din review este afisata
    def test_nota_medie_review_is_dispayed(self):
        self.driver.find_element(*locators.REZERVA_ACUM).click()
        nota = self.driver.find_element(*locators.NOTA_REVIEW)
        assert nota.is_displayed(), "Nota review element is not displayed"

    def tearDown(self) -> None:
        self.driver.quit()