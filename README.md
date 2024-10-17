# 🚀 Mi Proyecto de Automatización de WhatsApp con Selenium

![Banner](https://i.ibb.co/wdp0NvX/fffff.png)

Este repositorio contiene un script desarrollado en Python que automatiza el envío de mensajes e imágenes a través de WhatsApp utilizando Selenium. Es ideal para tareas de notificación recurrentes o actualizaciones automáticas.

## 📋 Características
- **Automatización de mensajes**: Envía mensajes y fotos a contactos específicos y grupos de WhatsApp.
- **Manejo de perfiles de usuario**: Carga un perfil de Chrome personalizado.
- **Programación flexible**: Personaliza el mensaje, destinatario y tiempo de envío.
  
## 🛠️ Tecnologías Utilizadas
- **Python**: Para la lógica principal del script.
- **Selenium**: Para la interacción con WhatsApp Web.
- **JSON**: Para programar envíos de mensajes y gestionar configuraciones.

## ⚙️ Configuración
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
Instala las dependencias necesarias:
bash
Copiar código
pip install -r requirements.txt
Configura tus rutas y preferencias en el archivo index.py y programa tus envíos en schedule.json.
🚀 Ejecución del Script
Asegúrate de tener chromedriver en tu PATH y ejecuta el script:
bash
Copiar código
python index.py
¡Listo! El script comenzará a enviar mensajes automáticamente según las configuraciones que hayas definido.
📂 Estructura del Repositorio
   ```bash
  Copiar código
  ├── imagenes/            # Carpeta de imágenes a enviar
  ├── schedule.json        # Programación de mensajes
  ├── index.py             # Script principal
  ├── README.md            # Este archivo
  └── requirements.txt     # Dependencias necesarias
  ```

🌐 Ejemplos de Uso
Envío de Reportes Automáticos

El script envía notificaciones y reportes automáticos a través de WhatsApp, lo cual es útil para actualizar a equipos de trabajo o enviar recordatorios periódicos.

📸 Agrega tus Imágenes
Puedes personalizar este repositorio agregando tus propias imágenes en la carpeta imagenes/ y modificando el schedule.json para ajustarse a tus necesidades.

