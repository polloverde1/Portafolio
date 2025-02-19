import requests
import time

nodemcu_ip = 'http://ip'

def mandar_com(com):
    url = f"{nodemcu_ip}/{com}"
    response = requests.get(url)
    print(response.text)

current_hour = time.localtime().tm_hour

if 15 <= current_hour < 18:
    mandar_com("on")
else:
    mandar_com("off")

