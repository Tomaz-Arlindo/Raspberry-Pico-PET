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
  * **[Raspberry Pi Pico](https://hackspace.raspberrypi.com/books/micropython-pico)** *(RP2040 Micro Controlador):* Um poderoso micro controlador que conta com diversas portas programaveis e compatíveis com diversos protocolos típicos de aplicações em automação e IoT (internet das coisas), geralmente programado em MicroPython uma versão do Python3 otimizada para microcontroladores deste porte, contando também com documentações e projetos afins na internet.
  
  
  * **[DS18B20](https://randomnerdtutorials.com/micropython-ds18b20-esp32-esp8266/)** *(Sensor de Temperatura):* Um sensor de temperatura digital que opera em ambientes secos, umidos e até submerso (no modelo tipo sonda), tem uma faixa de -55°C a 125°C e uma precisão de 0.5°C, cada sensor carrega um ID 64bits possibilitando associar multiplos sensores no mesmo barramento e fazendo a separação das coletas através do código do micro controlador.
  
  
  * **[MPU6050](https://microdigisoft.com/mpu6050-with-raspberry-pi-pico-using-micropython/)** *(Módulo Acelerômetro 3 Eixos):* Um MEMS (Micro-Electro-Mechanical Systems) que conta com um sensor de temperatura, um giroscópio de 3 eixos e um acelerômetro de 3 eixos (o foco deste projeto), entrega com grande precisão e velocidade seus dados de forma digital através do protocolo I2c.
  
  
  * **[ACS712](https://how2electronics.com/how-to-use-adc-in-raspberry-pi-pico-adc-example-code/)** *(Sensor de Corrente 20A max):* ---
  
  
  * **[ESP-01](https://www.filipeflop.com/blog/como-conectar-a-raspberry-pi-pico-ao-wifi-com-esp8266/)** *(ESP-8266 Conexão Wi-Fi):* Um módulo *Wireless*, compacto e de baixo custo que possibilita que um microcontrolador mais poderoso possa de conectar a uma rede WiFi podendo também hospedar aplicação própria respeitando suas limitações.
  
  
  ## Protocolos:
  protocolos de conexão utilizados
  
  
 [GPIO](https://www.oficinadanet.com.br/hardware/40552-o-que-e-gpio) *(General Purpose Input/Output)* - Portas programáveis de entrada e saída de dados que são utilizadas para prover uma interface entre os periféricos e os microcontroladores/microprocessadores.
 
  
  
 [I2C](https://how2electronics.com/how-to-use-i2c-pins-in-raspberry-pi-pico-i2c-scanner/) *(Inter-Integrated Circuit)* - Um barramento serial multimestre que é usado para conectar periféricos de baixa velocidade ao sistema embarcado num mesmo barramento (desde que estes tenham endereços diferentes).
 
 
 [ADC](https://www.circuitschools.com/how-to-use-adc-on-raspberry-pi-pico-in-detail-with-micropython-example/) *(Analog to Digital Converter)* - Gera uma codificação digital a partir de um nível de tensão ou intensidade de corrente analogica de um sensor.
 
 
 [UART](https://www.rohde-schwarz.com/br/produtos/teste-e-medicao/osciloscopios/educational-content/compreender-uart_254524.html) *(Universal Asynchronous Receiver/Transmitter)* - Como o próprio nome diz, é um protocolo assíncrono que possibilita a comunicação serial entre dois dispositivos de forma full-duplex.
  
  
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
#importação das bibliotecas
import machine, oneWire, ds18x20, time

pinoTemp = machine.Pin(6) #define o pino utilizado na montagem (GPIO6 - pino 9)
sensTemp = ds18x20.DS18X20(oneWire.OneWire(pinoTemp)) #define protocolo
idTemp = sensTemp.scan() #identifica endereço dos sensores conectados
print("Sensores encontrados:",idTemp)

while True:
    sensTemp.convert_temp() #realiza conversão de temperatura (min 750ms)
    time.sleep_ms(750)
    for i in idTemp:
        print(sensTemp.read_temp(i), "oC") #realiza leitura de cada sensor
        time.sleep(1)
  ~~~
  
  ##### MPU6050-CODE
  ~~~Python
#importação das bibliotecas
import machine, time, mpu6050

#define pinos i2c utilizados na montagem (GPIO21 - pino 27) (GPIO20 - pino 26) 
i2c = machine.I2C(0, scl= machine.Pin(21), sda= machine.Pin(20), freq=400000)
mpu6050.mpu6050_init(i2c) #inicia configurações do mpu6050 na porta i2c escolhida

#loop de leitura de dados
while True:
    print("Temperature:\t", mpu6050.mpu6050_get_temp(i2c), "°C") #temperatura
    print("Accelerometer:\t", mpu6050.mpu6050_get_accel(i2c), "g") #aceleração 3 eixos
    print("Gyroscope:\t", mpu6050.mpu6050_get_gyro(i2c), "°/s") #giroscópio 3 eixos
    time.sleep_ms(500)

  ~~~ 
  
 ##### ACS712-CODE
   ~~~python 
  print("Hello World !!!")
  ~~~
 
 ##### ESP-01-CODE
  ~~~python 
  print("Hello World !!!")
  ~~~
  
   > test!!!
      
  <p align="center"> README incompleto !!! <p>
