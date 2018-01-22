from time import sleep


class Send:
    def __init__(self, destination, message):
        self.destination = destination
        self.message = message

    def execute(self, ser):
        self.write(ser, "AT+CMGF=1\r")
        self.write(ser, "AT + CMGS = \"" + str(self.destination) + "\"")
        self.write(ser, self.message)
        self.write(ser, chr(26))
        self.write(ser, "")
        sleep(2.9)

    @staticmethod
    def write(ser, data):
        ser.write(data)
        ser.flush()
        sleep(0.1)
