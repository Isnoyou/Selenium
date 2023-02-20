import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

def click_and_clear_val_by_ID_(driver, id, val):
    Elem = driver.find_element(By.ID, id)
    Elem.clear()
    Elem = driver.find_element(By.ID, id).send_keys(val)

def getDateTime():
    return datetime.now().strftime("%H%M%S%f")

def create_random_mail():
    return getDateTime() + "@gmail.com"


############################################################################################################
# tests avec setup teardown
############################################################################################################

@pytest.mark.skip("test à ne pas exécuter")
class Test_Login():

    def setup_method(self, method):
        logging.info("Setup Method")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self, method):
        logging.info("TearDown method")
        #self.driver.quit()

    def test_Connexion(self):
        driver = self.driver
        logging.info("Test de connexion à un compte")
        driver.get('https://taq.uaestqb.ae/')
        Elem = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[2]')
        Elem.click()
        Elem = driver.find_element(By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a')
        Elem.click()

        click_and_clear_val_by_ID_(driver, "input-email", "eee@gmail.com")
        click_and_clear_val_by_ID_(driver, "input-password", "eeee")

        buttonloginElement = driver.find_element(By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')
        buttonloginElement.click()
        #time.sleep(5)

    def test_Deconnexion(self):
        driver = self.driver
        logging.info("Test de déconnexion à un compte")
        driver.get('https://taq.uaestqb.ae/')
        Elem = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[2]')
        Elem.click()
        # Elem = driver.find_element(By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a')
        # Elem.click()
        time.sleep(5)


############################################################################################################
# tests sans setup teardown
############################################################################################################

@pytest.mark.skip("test à ne pas exécuter")
def test_creation_compte():
    logging.info("Création du compte aaaa@gmail.com")
    driver = webdriver.Chrome()

    driver.get("https://taq.uaestqb.ae/")
    driver.maximize_window()

    Elem1 = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[2]')
    Elem1.click()
    Elem1 = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')
    Elem1.click()

    click_and_clear_val_by_ID_(driver, "input-firstname", "aaaa")
    click_and_clear_val_by_ID_(driver, "input-lastname", "aaaa")
    click_and_clear_val_by_ID_(driver, "input-email", create_random_mail())
    click_and_clear_val_by_ID_(driver, "input-telephone", "0212234556")
    click_and_clear_val_by_ID_(driver, "input-password", "aaaa")
    click_and_clear_val_by_ID_(driver, "input-confirm", "aaaa")

    Elem1 = driver.find_element(By.NAME, "agree").click()
    Elem1 = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input[2]')
    Elem1.click()

    assert 'Your Account Has Been Created!' in driver.page_source

    Elem1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/a').click()

    time.sleep(2)
    driver.quit()

@pytest.mark.skip("test à ne pas exécuter")
def test_deconnexion_compte():
    logging.info("deconnexion d'un compte")
    driver = webdriver.Chrome()
    driver.get("https://taq.uaestqb.ae/")
    driver.maximize_window()
    
    # début de connexion
    # # Uniquement pour tester le cas ou le bouton "logout" est présent ou pas
    Elem = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[2]')
    Elem.click()
    Elem = driver.find_element(By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a')
    Elem.click()
    click_and_clear_val_by_ID_(driver, "input-email", "eee@gmail.com")
    click_and_clear_val_by_ID_(driver, "input-password", "eeee")
    buttonloginElement = driver.find_element(By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')
    buttonloginElement.click()
    # fin de connexion       
        

    Elem1 = driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[2]')
    Elem1.click()
    
    # pourquoi  cela ne passe pas dans le else suivant si il n'y a pas de compte connecté
    # en commentant les lignes de 111 à 118.
    
    if EC.presence_of_element_located(driver.find_element(By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a')):
        logging.info("logout... trouvé")
        Elem = driver.find_element(By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a')
        Elem.click()
    else:
        logging.error("logout non trouvé")
        driver.quit()

    driver.quit()

############################################################################################################
# test avec un wait pour l'apparition du texte "Success: You have added iPhone to your shopping cart!"
############################################################################################################

@pytest.mark.skip("test à ne pas exécuter")
def test_ajout_iphone():
    logging.info("Ajout iphone au panier")
    driver = webdriver.Chrome()
    driver.get("https://taq.uaestqb.ae/")
    driver.maximize_window()

    Elem = driver.find_element(By.LINK_TEXT, "Phones & PDAs").click()
    Elem = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[2]/button[1]/span')
    Elem.click()

####################################################################################################################

    # Problème lors de la recherche du texte "Success: You have added iPhone to your shopping cart!"

    # Cela fonctionne avec le fullXPATH 
    # Elem1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]')
    
    # mais pas avec le XPATH
    # Elem1 = driver.find_element(By.XPATH, '//*[@id="common-home"]/div[1]')
     
    # Impossible de trouver le nom de la classe !
    # logging.info(Elem1.get_attribute("class"))

    # Cela ne fonctionne pas avec la classe non plus: POURQUOI ?
    # Element = driver.find_element(By.CLASS_NAME, "alert alert-success alert-dismissible")
    # logging.info(Element.get_attribute("class"))
    
    # Impossible de trouver le nom de la classe ! (avec le FULLXPATH) pourquoi ?
    # Elem1 = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]')
    # logging.info(Elem1.get_attribute("class"))
    
#####################################################################################################################

    wait = WebDriverWait(driver, 5)
    #Attente de 5 secondes pour l'apparition du message de réussite
    try:
        elem = wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[2]/div[1]'), "Success: You have added"))
        logging.info("Chaine Success... trouvée")
        
    except TimeoutException:
        logging.error("Chaîne Success... non trouvée")
        elem = None
        
    driver.quit()
