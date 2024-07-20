from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants_path_html import *
import credentials

def click_tab_log_in(driver):
    try:
        # Espera hasta que el elemento de login esté presente y sea clickeable
        login_tab = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_TAB_SELECTOR)))
        # Haz clic en el elemento de login
        login_tab.click()
        print("Click tab init account...")
    except Exception as e:
        print(f"No se pudo encontrar el tab de iniciar seccion {e}")

def load_input_email(driver):
    try:
        # Espera hasta que el campo de email esté presente
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, EMAIL_INPUT_SELECTOR)))
        # Introduce el email
        email_input.send_keys(credentials.EMAIL_USER)  # Cambia esto por el email real
        print("Load email")
    except Exception as e:
        print(f"No se pudo encontrar el input text para el campo email {e}")

def load_input_password(driver):
    try:
        # Espera hasta que el campo de contraseña esté presente
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR)))
        # Introduce la contraseña
        password_input.send_keys(credentials.PASSWORD)  # Cambia esto por la contraseña real
    except Exception as e:
        print(f"No se pudo encontrar el input text para el campo password {e}")

def click_button_log_in(driver):
    try:
        # Espera hasta que el botón de iniciar sesión esté presente y sea clickeable
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR))
        )
        login_button.click()
        print("init seccion in ogame")
    except Exception as e:
        print(f"No se pudo encontrar el button iniciar seccion {e}")

def click_button_join_the_game(driver):
    try:
        # Espera hasta que el botón de iniciar sesión esté presente y sea clickeable
        login_play_one = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_BUTTON_JOIN_GAME_SELECTOR))
            )
            # Haz clic en el botón de iniciar sesión
        login_play_one.click()
        print("Click button join the game") 
    except Exception as e:
        print(f"No se pudo encontrar el button jugar uno {e}")

def click_button_join_the_server(driver):
    try:
        # Espera hasta que el botón en el juego esté presente y sea clickeable
        login_play_two = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_BUTTON_JOIN_THE_SERVER_SELECTOR))
        )
        # Haz clic en el botón en el juego
        login_play_two.click()
        print("click init game")
    except Exception as e:
        print(f"No se pudo encontrar el button jugar dos {e}")