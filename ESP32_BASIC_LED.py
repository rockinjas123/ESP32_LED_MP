#importing the required libraries
from machine import Pin, ADC, PWM 
from time import sleep

# defining the pin arrangement
led_red = Pin(39, Pin.OUT)
button_red= Pin(36, Pin.IN)

#Configure ADC for ESP32
pot_green = ADC(Pin(2))
pot_green.width(ADC.WIDTH_10BIT)
pot_green.atten(ADC.ATTN_11DB)

green_pwm = PWM(Pin(26),5000) #frequency=5000Hz

while True:
  button_state = button_red.value()
  led_red.value(button_state)

  pot_value = pot_green.read()
  green_pwm.duty(pot_value)

  sleep(0.1) #delay
