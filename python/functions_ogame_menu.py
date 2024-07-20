# funciones_ogame_menu.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants_path_html import *
import time

def click_tab_recursos(driver):
    try:
        # Espera hasta que el elemento de la solapa de recursos esté presente y sea clickeable
        recursos_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, TAB_RECURSOS_SELECTOR))
        )
        # Haz clic en el elemento de la solapa de recursos
        recursos_tab.click()
        print("Click recursos_tab");
        time.sleep(2) 
    except Exception as e:
        print(f"No se pudo encontrar el elemento de la solapa de recursos: {e}")

