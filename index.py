from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

# Rutas para Chrome y ChromeDriver
chrome_profile_path = "C:/Users/bryan/AppData/Local/Google/Chrome/User Data/Default"
chrome_driver_path = "C:/Users/bryan/OneDrive - SENATI/Pictures/Desktop/whatsapp-automatico/chromedriver.exe"

# Configura Chrome Options para usar el perfil específico
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")  # Carga el perfil de usuario

# Crea el servicio de ChromeDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define el número de teléfono, el nombre del grupo y el mensaje base
numero = '51901064562'  # Número de teléfono para enviar el mensaje
nombre_grupo = 'chat2'  # Nombre exacto del grupo

# Abre WhatsApp Web
driver.get('https://web.whatsapp.com/')
sleep(15)  # Espera a que se abra y se cargue la página de WhatsApp Web

# Contador de reportes
contador = 1

# Bucle para enviar la imagen y el mensaje cada minuto
while True:
    try:
        # Configuración de la imagen y mensajes específicos para cada envío
        image_path = os.path.join(os.getcwd(), 'imagenes', f'{contador}.jpeg')
        mensaje_contacto = f'Reporte {contador}'
        mensaje_grupo = f'Reporte {contador} grupo'

        # Parte 1: Enviar al número de teléfono
        driver.get(f'https://web.whatsapp.com/send?phone={numero}')
        sleep(10)  # Espera que el chat se cargue

        # Localiza y haz clic en el botón de adjuntar archivo
        attach_button = driver.find_element(By.XPATH, '//div[@title="Adjuntar"]')
        attach_button.click()
        sleep(2)

        # Haz clic en el botón de selección de fotos
        photo_button = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        photo_button.send_keys(image_path)
        sleep(5)  # Espera a que se cargue la imagen

        # Escribe el mensaje para el contacto
        message_box = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
        message_box.send_keys(mensaje_contacto)
        sleep(1)

        # Envía el mensaje con la imagen
        message_box.send_keys(Keys.ENTER)

        # Parte 2: Enviar al grupo
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.clear()  # Asegura que esté vacío antes de escribir
        search_box.send_keys(nombre_grupo)
        search_box.send_keys(Keys.ENTER)
        sleep(5)  # Espera a que el grupo se abra

        # Repite los pasos para enviar la imagen en el grupo
        attach_button = driver.find_element(By.XPATH, '//div[@title="Adjuntar"]')
        attach_button.click()
        sleep(2)

        # Haz clic en el botón de selección de fotos
        photo_button = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        photo_button.send_keys(image_path)
        sleep(5)  # Espera a que se cargue la imagen

        # Escribe el mensaje para el grupo
        message_box = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
        message_box.send_keys(mensaje_grupo)
        sleep(1)

        # Envía el mensaje con la imagen
        message_box.send_keys(Keys.ENTER)

        # Incrementa el contador para el próximo envío y espera 1 minuto
        contador += 1
        sleep(60)

    except Exception as e:
        print("Ocurrió un error:", e)
        sleep(60)  # Espera antes de intentar de nuevo en caso de error
