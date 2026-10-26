from machine import Pin, SoftI2C # Aqui estou importando tanto a classe Pin quanto o SoftI2C do módulo machine, permitindo que o MicroPython interaja com o hardware.

'''
I2C é um protocolo que permite que o microcontrolador converse com outros componentes, como o OLED.
O SoftI2C implementa a comunicação pelo software, utilizando o SDA para transportar os dados e o SCL fornece o sinal de sincronização (clock)
'''

from ssd1306 import SSD1306_I2C # Aqui estamos importando uma classe que permite controlar o display com controlador SSD1306 usando I2C

'''
Uma diferença importante entre o machine e o ssd1306 é que o machine permite controlar os recursos do microcontrolador, enquanto o ssd1306 fornece comandos para desenhar textos e imagens no OLED
'''

i2c = SoftI2C (sda = Pin(14), scl = Pin(15)) 


oled = SSD1306_I2C (128, 64, i2c)