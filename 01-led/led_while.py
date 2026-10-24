# Utilizando como base o código anterior "led_sleep.py"

from machine import Pin
from time import sleep 

led_vermelho =  Pin(13, Pin.OUT)

contador = 0
while contador < 3:

    led_vermelho.value(1)
    sleep(2)
    led_vermelho.value(0)
    contador+=1