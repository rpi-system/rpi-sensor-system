import time
import logging

# Logger konfigurieren
logging.basicConfig(
    level=logging.INFO,  # Log-Level auf INFO setzen
    format="%(asctime)s [%(levelname)s] %(message)s",  # Format für Logs
    handlers=[
        logging.FileHandler("app.log"),  # Log-Datei
        logging.StreamHandler()  # Ausgabe auf der Konsole
    ]
)

while True:
    logging.info("Hallo, Welt!")
    time.sleep(1)  # Alle 30 Sekunden "Hallo, Welt!" loggen