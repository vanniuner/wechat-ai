import threading, datetime
import am2302_ths

class Sensor(object):
    def __init__(self, pin):
        print "init"
        self.current_temp = None
        self.temp = None
        self.humid = None
        self.last_time = None
        self.INPUT = pin

        self.timer = threading.Timer(0, self._tick)
        self.timer.start()

    def _tick(self):
        try:
            print self.INPUT
            temp = am2302_ths.get_temperature(self.INPUT)
            print "tick_start"
            if temp:
                self.last_time = datetime.datetime.now()
                self.temp = temp
            self.timer = threading.Timer(10, self._tick)
            self.timer.start()
            print temp
        except:
            self.off()
            print("Error reading from sensor.")

    def get(self):
        return self.temp

    def get_last_time(self):
        return self.last_time

    def off(self):
        self.timer.cancel()

    def __del__(self):
        self.off()

s = Sensor(4)
print s.get()
