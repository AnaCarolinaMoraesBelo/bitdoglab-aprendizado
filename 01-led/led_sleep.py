from machine import Pin #importa a classe para que possa controlar os pinos
from time import sleep #importa a função de espera

led_vermelho = Pin(13, Pin.OUT) # Configura o GPIO 13 como sáida

led_vermelho.value(1) #liga o led
sleep(2) #espera dois segundos
led_vermelho.value(0) #desliga o led