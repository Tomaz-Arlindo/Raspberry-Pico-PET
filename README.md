# Projeto PET Freezer IoT
  <p align="center"> README incompleto !!! <p>

### Sumário:
  * [Componentes](#componentes)
  * [Protocolos](#protocolos) 
  * [Montagem](#montagem)
  * [Códigos](#códigos)
    * [DS18B20](#ds18b20-code)
    * [MPU6050](#mpu6050-code)
    * [ACS712](#acs712-code)
    * [ESP-01](#esp-01-code)

  
  
  ## Componentes:
  breve resumo e dattasheets
  * **[Raspberry Pi Pico](https://hackspace.raspberrypi.com/books/micropython-pico)** *(RP2040 Controlador):*
  * **[DS18B20]()** *(Sensor de Temperatura):*
  * **[MPU6050]()** *(Módulo Acelerômetro 3 Eixos):*
  * **[ACS712]()** *(Sensor de Corrente 20A max):*
  * **[ESP-01]()** *(ESP-8266 Conexão Wi-Fi):*
  
  
  ## Protocolos:
  protocolos de conexão utilizados
  
  
 [GPIO](https://www.oficinadanet.com.br/hardware/40552-o-que-e-gpio)
  
  
 [I2C](https://how2electronics.com/how-to-use-i2c-pins-in-raspberry-pi-pico-i2c-scanner/)
 
 
 [UART](https://www.rohde-schwarz.com/br/produtos/teste-e-medicao/osciloscopios/educational-content/compreender-uart_254524.html)
  
  
  ## Montagem:
  
  pinagem Raspberry Pi Pico
  ![pico-pinout](https://github.com/Tomaz-Arlindo/Raspberry-Pico-PET/blob/main/images/pico-pinout.png)
  <p align="center">(Pinagem da placa Raspberry Pi Pico)</p>
  
  
  ds18b20
  ![pico-ds18b20](https://github.com/Tomaz-Arlindo/Raspberry-Pico-PET/blob/main/images/pico-ds18b20.png)
  <p align="center">(montagem do ds18b20)</p>
  
  
  mpu6050
  ![pico-mpu6050](https://github.com/Tomaz-Arlindo/Raspberry-Pico-PET/blob/main/images/pico-mpu6050.png)
  <p align="center">(montagem do mpu6050)</p>
  
  
  acs712
  ![pico-acs712](https://github.com/Tomaz-Arlindo/Raspberry-Pico-PET/blob/main/images/pico-acs712.png)
  <p align="center">(montagem do acs712)</p>
  
  
  esp-01
  ![pico-esp01](https://github.com/Tomaz-Arlindo/Raspberry-Pico-PET/blob/main/images/pico-esp01.png)
  <p align="center">(montagem do esp-01)</p>
  
  
  ## Códigos:
  
  ##### DS18B20-CODE
  ~~~Python
    #importação das bibliotecas para pinos, protocolo, sensor e tempo 
    import machine, oneWire, ds18x20, time 

    pinoTemp = machine.Pin(6) #define o pino utilizado na montagem
    sensTemp = ds18x20.DS18X20(onewire.OneWire(pinoTemp)) #define protocolo
    idTemp = sensTemp.scan() #identifica endereço dos sensores conectados
    print("Sensores encontrados:",idTemp)

    while True:
        sensTemp.convert_temp() #realiza conversão de temperatura (min 750ms)
        time.sleep_ms(750)
        for i in idTemp:
            print(sensTemp.read_temp(i), "oC", end = ";") #realiza leitura de cada sensor
            time.sleep(3)
        print("\n")
  ~~~
  
  ##### MPU6050-CODE
  ~~~Python
  from mpu6050 import mpu6050
  os.mkdir("teste")
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
  
  
   testando descrição muito boa topzera melhor de todas
   > muito top mesmo  sempre uso é show
      
  <p align="center"> README incompleto !!! <p>
