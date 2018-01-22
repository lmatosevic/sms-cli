from time import sleep


class Check:
    def __init__(self, times):
        self.times = times

    def execute(self, ser):
        for i in self.times:
            ser.write("AT")
            ser.flush()
            sleep(1)
            response = ser.read_all()
            print(str(i) + "/" + str(self.times) + "request: AT -> response: " + response)
