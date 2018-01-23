from time import sleep


class Check:
    def __init__(self, iterations):
        self.iterations = iterations

    def execute(self, ser):
        print("Checking started...")
        for i in range(self.iterations):
            ser.write("AT\r".encode("ascii"))
            sleep(4)
            response = ser.read(100).decode("ascii")
            print(str(i + 1) + "/" + str(self.iterations) + " AT -> " + response)
