import utime

from lib.app import App


def main():
    utime.sleep(30)
    app = App()
    app.run()
    utime.sleep(10)
    
    #test(app)
    interval = 10
    while True:
        t = app.temperature
        h = app.humidity
        a = app.co2
        if not None in [t, h, a]:
            print(t, h, a)
        utime.sleep(interval)
    
    
    
    
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
