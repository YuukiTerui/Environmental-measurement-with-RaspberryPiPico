from machine import Pin, Timer, UART
import utime

from lib.dht import DHT11, InvalidChecksum


class App:
    def __init__(self):
        self.dht = DHT11(Pin(22, Pin.OUT, Pin.PULL_DOWN))
        
        self.baudrate = 9600
        self.mhz19c = UART(0, self.baudrate, tx=Pin(0), rx=Pin(1))
        self.mhz19c.init(self.baudrate, bits=8, parity=None, stop=1)
        
        self._temperature = None
        self._humidity = None
        self._co2 = None
        
        self.start_time = utime.ticks_ms()
        self.timer = None
    
    @property
    def board_temperature(self):
        pin = machine.ADC(4)
        v = pin.read_u16() * (3.3 / (2 ** 16 - 1))
        temp = 27 - (v - 0.706) / 0.001721
        return temp
    
    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity
    
    @property
    def co2(self):
        return self._co2

    def measure_temperature(self):
        t = None
        try:
          t = self.dht.temperature
        except Exception as e:
            # print(e)
            pass
        return t
        
    def measure_humidity(self):
        h = None
        try:
            h = self.dht.humidity
        except Exception as e:
            # print(e)
            pass
        return h
        
    def measure_co2(self):
        data = bytearray([0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])
        self.mhz19c.write(data)
        self.mhz19c.readinto(data, len(data))
        co2 = data[2] * 256 + data[3]
        temp = data[4] - 48
        return co2
    
    def update(self, timer=None):
        self._temperature = self.measure_temperature()
        self._humidity = self.measure_humidity()
        self._co2 = self.measure_co2()
        
    
    def __str__(self):
        print(f">time:{(utime.ticks_ms() - self.start_time)//1000}")
        print("board_tmp: ", self.board_temperature)
        print("temperature: ", self.temperature)
        print("humidity: ", self.humidity)
        print("co2: ", self.co2)
        print("<")
    
    def run(self):
        self.start_time = utime.ticks_ms()
        self.timer = Timer()
        self.timer.init(
            mode=Timer.PERIODIC,
            period=4000,
            callback=self.update
        )


