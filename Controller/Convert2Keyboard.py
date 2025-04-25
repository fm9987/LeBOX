import serial
import pyautogui

# Replace with your actual port (like 'COM3' or '/dev/ttyACM0')
ser = serial.Serial('COM3', 9600, timeout=1)

print("Listening for button presses...")

while True:
    line = ser.readline().decode('utf-8').strip()
    if "Button Pressed" in line:
        print("Detected: Button Pressed")
        pyautogui.press('z')