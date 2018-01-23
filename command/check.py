from time import sleep


class Check:
    def __init__(self, number):
        self.number = number

    def execute(self, ser):
        print("Checking started...")
        for i in range(self.number):
            ser.write("AT\r".encode("ascii"))
            sleep(2)
            _ = ser.readline()
            response = ser.readline().decode("ascii")
            print(str(i + 1) + "/" + str(self.number) + " AT -> " + response)
