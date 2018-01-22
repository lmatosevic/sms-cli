from time import sleep


class Check:
    def __init__(self, times):
        self.times = times

    def execute(self, ser):
        for i in range(self.times):
            ser.write("AT".encode())
            ser.flush()
            sleep(1)
            response = ser.read_all()
            print(str(i + 1) + "/" + str(self.times) + " AT -> " + response.decode())
