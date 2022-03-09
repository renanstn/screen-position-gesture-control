import serial


end_character = "!"

with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as ser:
    ser.reset_input_buffer()
    word = ""
    while True:
        x = ser.read()
        if x.decode("utf-8") == "!":
            print(word)
            word = ""
        else:
            word += x.decode("utf-8")
