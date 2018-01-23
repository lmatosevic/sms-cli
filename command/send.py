from time import sleep


class Send:
    def __init__(self, destination, message):
        self.destination = str(destination).strip()
        self.message = str(message)
        if not self.destination.startswith("+"):
            self.destination = "+" + self.destination

    def execute(self, ser):
        print("Sending started...")
        self.write(ser, "AT + CMGF = 1\r")
        self.write(ser, "AT + CMGS = \"" + self.destination + "\"\r")
        self.write(ser, self.message + "\r")
        self.write(ser, chr(26))
        self.write(ser, "\r")
        sleep(5)
        print("Message sent!")

    @staticmethod
    def write(ser, data):
        ser.write(data.encode("ascii"))
        sleep(0.5)
