import serial
import keyboard


with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as serial_:
    serial_.reset_input_buffer()

    while True:
        bytes_word = serial_.readline()
        word = bytes_word.decode("utf-8")
        word = word.replace("\n", "")
        print(word)
        print(word=="left")
