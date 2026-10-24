# Utilizando como base o código anterior "led_sleep.py"

from machine import Pin
from time import sleep 

led_vermelho =  Pin(13, Pin.OUT)

contador = 0 # Contador será a minha variável "base"
while contador < 3: # O while é uma função que executa os comandos enquanto a condição dela não for satisfeita

    '''
      Aqui eu utilizo que o meu contador é igual a zero e o while só irá parar quando o contador > 2. Ao final de cada loop eu adiciono +1 ao meu contador, fazendo com que ele vá parar quando o meu contador == 3.
    '''

    led_vermelho.value(1)
    sleep(2)
    led_vermelho.value(0)
    sleep(2)
    contador+=1 #Soma +1 ao contador ao final de cada loop.