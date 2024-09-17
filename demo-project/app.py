# import time
# import logging

# # Logger konfigurieren
# logging.basicConfig(
#     level=logging.INFO,  # Log-Level auf INFO setzen
#     format="%(asctime)s [%(levelname)s] %(message)s",  # Format für Logs
#     handlers=[
#         logging.FileHandler("app.log"),  # Log-Datei
#         logging.StreamHandler()  # Ausgabe auf der Konsole
#     ]
# )

# while True:
#     logging.info("Hallo, Welt!")
#     time.sleep(1)  # Alle 30 Sekunden "Hallo, Welt!" loggen
    
    
    
import time
import logging
from influxdb_client import InfluxDBClient, Point, WriteOptions

# Logger konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# InfluxDB-Konfiguration
INFLUXDB_URL = "http://influxdb:8086"  # Hostname des Containers
INFLUXDB_TOKEN = "adminpassword"  # Token oder Admin-Passwort
INFLUXDB_ORG = "myorg"  # Organisation (kann auch eine statische Zeichenfolge sein)
INFLUXDB_BUCKET = "mydb"

# InfluxDB-Client initialisieren
client = InfluxDBClient(
    url=INFLUXDB_URL,
    token=INFLUXDB_TOKEN,
    org=INFLUXDB_ORG
)

write_api = client.write_api(write_options=WriteOptions(batch_size=1))

def send_data_to_influxdb():
    point = Point("temperature") \
        .tag("location", "office") \
        .field("value", 23.5)  # Beispiel-Daten, die gesendet werden
    write_api.write(bucket=INFLUXDB_BUCKET, record=point)
    logging.info("Daten an InfluxDB gesendet: Temperatur 23.5")

while True:
    send_data_to_influxdb()
    logging.info("Hallo, Welt!")
    time.sleep(30)