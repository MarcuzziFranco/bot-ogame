import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functions_ogame_login import *
from functions_ogame_menu import *  
from functions_read_info import * 
from functions_metal_mine import *

import variables_globales as vg

# Configura el path al archivo del controlador
service = Service('C:\\Users\\Franco\\projects\\bot-og\\chromedriver.exe')

# Configura opciones para el navegador (opcional)
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Ejecutar en modo headless (opcional)

# Inicializa el navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navega a la URL
driver.get(URL_LOGIN_OGAME)  # Cambia esto a la URL real
time.sleep(5) 
try:

    click_tab_log_in(driver)

    load_input_email(driver)

    load_input_password(driver)

    click_button_log_in(driver)

    click_button_join_the_game(driver)
    time.sleep(2)
    click_button_join_the_server(driver)
    # Espera a que se abra la nueva pestaña
    time.sleep(5)  # Ajusta el tiempo según sea necesario

    # Cambia el foco a la nueva pestaña
    driver.switch_to.window(driver.window_handles[1])

    click_tab_recursos(driver)
    click_metal_mine(driver)

    get_metal_mine_upgrade_cost_int(driver)
    print(vg.metal_mine_cost_in_metal)
    print(vg.metal_mine_cost_in_cristal)
    print(vg.metal_mine_energy_need)

    # Función para leer los recursos y ejecutar tareas basadas en sus valores
    def read_resources_and_act():
        try:
            vg.current_metal_amount = get_current_amount_metal_text(driver)
            vg.current_crital_amount = get_current_amount_cristal_text(driver)
            vg.current_deuterio_amount = get_current_amount_deuterio_text(driver)
            vg.current_energy_amount =  get_current_amount_energy_text(driver)
            


            #print(f"Metal: {metal}")
            #print(f"Cristal: {cristal}")
            #print(f"Deuterio: {deuterio}")
            #print(f"Energia: {energia}")
            #print(f"-------------------------")

            
            
            #print(f"Level Mina Metal:{level_metal}")

            # Aquí puedes agregar la lógica para realizar tareas según los valores de los recursos
            #if int(metal.replace('.', '')) > 100000:  # Ejemplo de condición
            #    print("Tienes mucho metal. Considera construir algo.")
            #if int(cristal.replace('.', '')) < 50000:  # Ejemplo de condición
            #    print("Tienes poco cristal. Considera buscar más.")

        except Exception as e:
            print(f"Error al leer recursos: {e}")

    def update_level_mine_metal():
        if(vg.current_energy_amount >= vg.metal_mine_energy_need
           and vg.current_metal_amount > vg.metal_mine_cost_in_metal
           and vg.current_crital_amount > vg.metal_mine_cost_in_cristal):
            print("update mine metal action")
        


    # Lee los recursos cada 10 segundos
    while True:
        read_resources_and_act()
        update_level_mine_metal()
        time.sleep(10)  # Ajusta el intervalo según sea necesario
        print("run...")


    # Espera unos segundos para ver el resultado
    time.sleep(5)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Mantén el navegador abierto
    print("El navegador permanecerá abierto. Ciérralo manualmente cuando hayas terminado.")
    input("Presiona Enter para cerrar el navegador y terminar el script...")

    # Cierra el navegador
    driver.quit()
