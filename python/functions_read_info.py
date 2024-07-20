from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants_path_html import *

#METAL GET INFOMATION
def get_current_amount_metal_text(driver):
    try:
        metal = driver.find_element(By.CSS_SELECTOR, METAL_SELECTOR).text
        return metal;
    except Exception as e:
        print(f"Error al leer recursos: {e}")
        return "0"

def get_current_amount_metal_int(driver):
    try:
        metal = driver.find_element(By.CSS_SELECTOR, METAL_SELECTOR).text
        return int(metal.replace('.', ''));
    except Exception as e:
        return 0
#########################

#CRISTAL GET
def get_current_amount_cristal_text(driver):
    try:
        cristal = driver.find_element(By.CSS_SELECTOR, CRISTAL_SELECTOR).text
        return cristal;
    except Exception as e:
        print(f"Error al leer recursos: {e}")
        return "0"

def get_current_amount_cristal_int(driver):
    try:
        cristal = driver.find_element(By.CSS_SELECTOR, CRISTAL_SELECTOR).text
        return int(cristal.replace('.', ''));
    except Exception as e:
        return 0
#########################

#DEUTERIO GET 
def get_current_amount_deuterio_text(driver):
    try:
        deuterio = driver.find_element(By.CSS_SELECTOR, DEUTERIO_SELECTOR).text
        return deuterio;
    except Exception as e:
        print(f"Error al leer recursos: {e}")
        return "0"

def get_current_amount_deuterio_int(driver):
    try:
        deuterio = driver.find_element(By.CSS_SELECTOR, DEUTERIO_SELECTOR).text
        return int(deuterio.replace('.', ''));
    except Exception as e:
        return 0
#########################

#ENERGIA GET
def get_current_amount_energy_text(driver):
    try:
        energy = driver.find_element(By.CSS_SELECTOR, ENERGIA_SELECTOR).text
        return energy;
    except Exception as e:
        print(f"Error al leer recursos: {e}")
        return "0"

def get_current_amount_energy_int(driver):
    try:
        energy = driver.find_element(By.CSS_SELECTOR, ENERGIA_SELECTOR).text
        return int(energy.replace('.', ''));
    except Exception as e:
        return 0
#########################