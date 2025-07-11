# circus-client-micropython

A simple MicroPython client for interacting with the [Circus of Things](https://circusofthings.com/) API.  
Supports reading and writing values via HTTP with optional position (latitude, longitude, altitude) metadata.

## 📦 Features

- ✅ Write values to Circus of Things
- ✅ Read values from Circus of Things
- ✅ Optional GPS/position data support
- ✅ Lightweight and easy to use in MicroPython projects (e.g., ESP32, Raspberry Pi Pico W)

## 🚀 Installation

Just copy `circus.py` to your MicroPython project.

> Make sure your device is connected to the internet and has the `urequests` module.

## 🧠 Usage

```python
from circus import Circus

API_KEY = "your_circus_token"
POSITION = (13.7563, 100.5018, 0.0)  # Optional (latitude, longitude, altitude)

cot = Circus(API_KEY, POSITION)

# Write value
result = cot.post_value("your_public_key", 42)
print("Write result:", result)

# Read value
value = cot.get_value("your_public_key")
print("Read value:", value)
