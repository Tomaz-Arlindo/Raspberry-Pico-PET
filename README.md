# Projeto PET Freezer IoT


### Sumário:
  * [Componentes](#componentes)
  * [Protocolos](#protocolos) 
  * [Montagem](#montagem)
  * [Códigos](#códigos)
    * [MPU6050](#mpu6050-code)
    * [DS18B20](#ds18b20-code)
    * [ACS712](#acs712-code)
    * [ESP-01](#esp-01-code)

  
  
  ## Componentes:
  breve resumo e dattasheets
  * **[Raspberry pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#raspberry-pi-pico-and-pico-h)** *(RP2040 Controlador)* :
  
      testando descrição muito boa topzera melhor de todas
      > muito top mesmo  sempre uso é show
      
  * **ESP-01** *(ESP-8266 Conexão Wi-Fi)* :
  * **MPU6050** *(Módulo Acelerômetro 3 Eixos)* :
  * **DS18B20** *(Sensor de Temperatura)* :
  * **ACS712** *(Sensor de Corrente 20A max)* :
  
  
  ## Protocolos:
  protocolos de conexão utilizados
  
 [I2C](https://how2electronics.com/how-to-use-i2c-pins-in-raspberry-pi-pico-i2c-scanner/)
 
 
 [GPIO](https://www.oficinadanet.com.br/hardware/40552-o-que-e-gpio)
 
 
 [UART](https://www.rohde-schwarz.com/br/produtos/teste-e-medicao/osciloscopios/educational-content/compreender-uart_254524.html#:~:text=UART%20significa%20Transmissor%2Freceptor%20assíncrono,receber%20em%20ambas%20as%20direções.)
  
  
  ## Montagem:
  ![modelo-cad](image-link)
  
  ## Códigos:
  
  ##### MPU6050-CODE
  ~~~Python
  import os
  os.mkdir("teste")
  print("Hello world!!!")
  
  ~~~
  
 ##### DS18B20-CODE
  ~~~Python
  import machine
  x = machine.pin(8) 
  print("Hello world!!!")
  
  ~~~
  
 ##### ACS712-CODE
   ~~~Python
  import mchine
  y = machine.pin(10)
  print("Hello world!!!")
  
  ~~~
 
 ##### ESP-01-CODE
   ~~~Python
  import time
  time.daytime()
  print("Hello world!!!")
  
  ~~~
  
  ~~~python 
  print("hello")
  ~~~
  
  
  testando
