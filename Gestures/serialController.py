import serial
import time
from pynput.mouse import Button, Controller as MouseController

from pynput.keyboard import Key, Controller as KeyboardController


MAX_BUFF_LEN = 255
SETUP 		 = False
port 		 = None

prev = time.time()
while(not SETUP):
	try:
		# 					 Serial port(windows-->COM), baud rate, timeout msg
		port = serial.Serial("COM6", 115200, timeout=1)

	except: # Bad way of writing excepts (always know your errors)
		if(time.time() - prev > 2): # Don't spam with msg
			print("No serial detected, please plug your uController")
			prev = time.time()

	if(port is not None): # We're connected
		SETUP = True


# read one char (default)
def read_ser(num_char = 1):
	string = port.read(num_char)
	return string.decode()

# Write whole strings
def write_ser(cmd):
	cmd = cmd + '\n'
	port.write(cmd.encode())

mouse = MouseController()
keyboard = KeyboardController()

# Super loop
while(1):
	string = read_ser(MAX_BUFF_LEN)
	if(len(string)):
		print(string)

		if "4-finger" in string:
			mouse.click(Button.left, 2)


		if "3-finger" in string:
			keyboard.press(Key.left)
			keyboard.release(Key.left)

		#if "Swipe Right" in string:
		if "2-finger" in string:
			keyboard.press(Key.right)
			keyboard.release(Key.right)


	# cmd = input() # Blocking, there're solutions for this ;)
	# if(cmd):
	# 	write_ser(cmd)
