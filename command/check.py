from time import sleep


class Check:
    def __init__(self, times):
        self.times = times

    def execute(self, ser):
        for i in range(self.times):
            ser.write("AT\r".encode("ascii"))
            ser.flush()
            sleep(5)
            response = ser.read(2)
            print(str(i + 1) + "/" + str(self.times) + " AT -> " + response.decode("ascii"))
