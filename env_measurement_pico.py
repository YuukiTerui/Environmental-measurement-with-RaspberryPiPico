import time, csv
from datetime import datetime
import serial
from serial.tools import list_ports


class EnvMeasurementPico:
    def __init__(self, ):
        self.port = '/dev/ttyACM0'
        self.baudrate = 9600
        self.timeout = 3
        self.serial = None
        self.buffer = []
        self.interval = 1
        self.is_running = False

        self.set_serial()
    
    def set_serial(self, port=None):
        if port is None:
            port = self.port
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        except serial.serialutil.SerialException:
            print(f'could not open port {port}')
            self.serial = None

    def set_port(self, port):
        self.port = port
    
    def set_timeout(self, timeout):
        self.timeout = timeout

    def init(self):
        while True:
            line = self.measure()
            print(line)
            if  line == []:
                break

    def run(self):
        if self.serial is None:
            print('serial is None')
            return
        self.init()
        print(f'running at {self.port}')
        self.is_running = True
        while self.is_running:
            line = self.measure()
            if line == []:
                continue
            t = datetime.now().strftime('%H:%M:%S')
            self.buffer.append([t, *line])
            print(self.buffer[-1])
            time.sleep(self.interval)
    
    def stop(self):
        self.is_running = False
        
    def measure(self):
        line = self.serial.readline()
        try:
            line = line.decode('utf-8').replace('\r\n', '').split()
        except Exception as e:
            print(e)
            line = None
        return line
    
    def clear(self):
        self.buffer = []

    def save(self):
        fname = datetime.now().strftime("%Y%m%d")
        with open(f'./data/{fname}.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerows(self.buffer)
        self.clear()

    @classmethod
    def show_ports(cls):
        devices = [info for info in list_ports.comports()]
        for i, device in enumerate(devices):
            print(f'{i}: {device}')


def main():
    app = EnvMeasurementPico()
    if app.serial is None:
        app.show_ports()
        port = input()
        app.set_port(port)
        app.set_serial()
    app.run()

if __name__ == '__main__':
    main()
    
