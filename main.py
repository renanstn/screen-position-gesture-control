import serial
import pyautogui


with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as serial_:
    serial_.reset_input_buffer()

    while True:
        bytes_signal = serial_.readline()
        signal = bytes_signal.decode("utf-8")
        signal = signal.replace("\n", "")

        if signal == "left":
            print("left")
            pyautogui.hotkey("winleft", "left")
        elif signal == "right":
            print("right")
            pyautogui.hotkey("winleft", "right")
        elif signal == "up":
            print("up")
            pyautogui.hotkey("winleft", "up")
        elif signal == "down":
            print("down")
            pyautogui.hotkey("winleft", "down")
