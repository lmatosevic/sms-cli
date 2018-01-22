import argparse
import serial

from command.check import Check
from command.send import Send


def main():
    parser = argparse.ArgumentParser(prog='sms-core',
                                     description="execute AT commands on GSM shield module via serial port")
    parser.add_argument("-v", "--version", help="print version number", action='version', version='%(prog)s 1.0.0')
    parser.add_argument("-b", "--baud", help="specify baud rate", required=False, default=19200)
    parser.add_argument("-c", "--com", help="specify communication device", required=False, default="/dev/ttyAMA0")
    sub_parser = parser.add_subparsers()

    send_parser = sub_parser.add_parser('send', help='send SMS message to destination')
    send_parser.add_argument("-d", "--dest",
                             help="destination MSISDN in full format (e.g. +38591234567)", required=True)
    send_parser.add_argument("-m", "--message",
                             help="SMS message text with maximum of 160 characters (e.g. \"Some message text.\")",
                             required=True)

    check_parser = sub_parser.add_parser('check', help="check connectivity with GSM shield module")
    check_parser.add_argument("-t", "--times", help="how many times to check connection", required=False, default=4)
    args = parser.parse_args()

    ser = None

    try:
        ser = serial.Serial(args.com, args.baud, timeout=1)
        ser.open()
        command = create_command(args)
        command.execute(ser)
    except serial.SerialException:
        print("Unable to open port " + str(args.com))
    finally:
        if ser is not None:
            ser.close()


def create_command(args):
    if hasattr(args, 'times'):
        return Check(args.times)
    else:
        return Send(args.dest, args.message)


if __name__ == "__main__":
    main()
