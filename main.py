from time import sleep
from threading import Thread
import schedule

from env_measurement_pico import EnvMeasurementPico as App


def main():
    app = App()
    if app.serial is None:

        app.show_ports()
        port = input()
        app.set_port(port)
        app.set_serial()
    
    thread = Thread(target=app.run)
    thread.start()
    sleep(3)
    
    schedule.every(60).seconds.do(app.save)
    
    try:
        while True:
            schedule.run_pending()
            sleep(1)
    except Exception as e:
        print(e)
        app.stop()


def test(app):
    ls = app.buffer
    print('buf', ls)
    app.clear()
    

if __name__ == '__main__':
    main()