# Utilizando como base o arquivo anterior "if_else.py"

from machine import Pin
from time import sleep

led_vermelho = Pin(13, Pin.OUT)


contador = 0

while contador < 10: # Utilizando o conceito de while do código passado
    if contador % 2 == 0: # O led acende se o resto do contador for == 0, ou seja, se o contador for par.
        led_vermelho.value(1)
        sleep(1)
    else: # O led apaga se o resto do contador for != (diferente) 0, ou seja, se o contador for ímpar.
        led_vermelho.value(0) 
        sleep(1)
    contador += 1
