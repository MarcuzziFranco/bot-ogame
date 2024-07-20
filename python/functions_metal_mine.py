from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants_path_html import *
import variables_globales as vg
import time

#FUNCTIONS INFO AND OPERATOR MINE METAL

def get_current_level_mine_metal_text(driver):
    try:
        current_level = driver.find_element(By.CSS_SELECTOR, CURRENT_LEVEL_MINE_METAL_SELECTOR).text
        return current_level;
    except Exception as e:
        print(f"Error al leer recursos: {e}")
        return "0"
    
def get_current_level_mine_metal_int(driver):
    try:
        current_level = driver.find_element(By.CSS_SELECTOR, CURRENT_LEVEL_MINE_METAL_SELECTOR).text
        return int(current_level);
    except Exception as e:
        print(f"Error al leer recursos: {e}")
        return 0

def click_metal_mine(driver):
    try:
        # Esperar a que el elemento sea clickeable
        metal_mine_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, BUTTON_MINE_METAL_SELECTOR))
        )
        # Hacer clic en el elemento
        metal_mine_element.click()
        time.sleep(2) 
        print("Elemento de la mina de metal clickeado con éxito.")
    except Exception as e:
        print(f"No se pudo hacer clic en el elemento de la mina de metal: {e}")

def get_metal_mine_upgrade_cost_int(driver):
    try:
        # Esperar a que el elemento que contiene el valor del metal esté presente
        metal_cost = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, METAL_COST_SELECTOR))
        )
        # Esperar a que el elemento que contiene el valor del cristal esté presente
        cristal_cost = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CRISTAL_COST_SELECTOR))
        )
        # Esperar a que el elemento que contiene el valor de energia este presente
        energy_cost = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ENERGY_COST_SELECTOR))
        )
        
        # Obtener el valor del metal , cristal energia
        metal_value = metal_cost.get_attribute("data-value")
        cristal_cost = cristal_cost.get_attribute("data-value")
        energy_cost = energy_cost.get_attribute("data-value")

        print(f"Valor del metal: {metal_value}")
        print(f"Valor del cristal: {cristal_cost}")
        print(f"Valor del energia: {energy_cost}")

        vg.metal_mine_cost_in_metal = metal_value
        vg.metal_mine_cost_in_cristal = cristal_cost
        vg.metal_mine_energy_need = energy_cost

        print("Get metal mine upgrade cost")
    except Exception as e:
        print(f"Error al obtener los datos de la mina de metal: {e}")
    