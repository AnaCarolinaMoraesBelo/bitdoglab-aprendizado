from machine import Pin #Importa a classe, permitindo que haja o controle sobre os pinos da placa.

led_vermelho = Pin(13, Pin.OUT) # Aqui ele configura que o GPIO 13 será a saída digital

led_vermelho.value(1) # Quando o value estiver em 1 (um), significa que está em nível lógico alto (=~ 3.3V) e quando está em 0 (zero) significa que está em nível lógico baico (0V)