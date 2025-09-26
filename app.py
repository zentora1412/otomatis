import time
import random   # simulasi sensor
from datetime import datetime

# Simulasi sensor DHT22
def read_dht22():
    temperature = random.uniform(22, 30)  # simulasi suhu
    humidity = random.uniform(70, 100)    # simulasi kelembapan
    return round(temperature, 2), round(humidity, 2)

# Simulasi relay kontrol
def control_fan(on):
    if on:
        print("[FAN] ON")
    else:
        print("[FAN] OFF")

def control_pump(on):
    if on:
        print("[PUMP] ON")
    else:
        print("[PUMP] OFF")

# Main loop
fan_on = False
pump_on = False

print("=== Mushroom Automation System Started ===")

while True:
    temp, hum = read_dht22()
    print(f"[{datetime.now()}] Temp: {temp} °C | Humidity: {hum} %")

    # Logic kipas
    if temp > 27 and not fan_on:
        control_fan(True)
        fan_on = True
    elif temp < 23 and fan_on:
        control_fan(False)
        fan_on = False

    # Logic pompa
    if hum < 80 and not pump_on:
        control_pump(True)
        pump_on = True
    elif hum > 95 and pump_on:
        control_pump(False)
        pump_on = False

    time.sleep(2)
