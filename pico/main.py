import utime

from lib.app import App


def main():
    utime.sleep(30)
    app = App()
    app.run()
    utime.sleep(10)
    
    #test_tmp_humid(app)
    
    interval = 10
    while True:
        t = app.temperature
        h = app.humidity
        a = app.co2
        if not None in [t, h, a]:
            print(t, h, a)
        utime.sleep(interval)
    
    
def test_tmp_humid(app):
    while True:
        t = app.temperature
        h = app.humidity
        t2 = app.board_temperature
        print(t, t2, h)
        utime.sleep(2)
    
def test(app):
    while True:
        t = app.temperature
        h = app.humidity
        a = app.co2
        if not None in [t, h, a]:
            print(t, h, a)
        utime.sleep(2)
    


if __name__ == "__main__":
    main()
