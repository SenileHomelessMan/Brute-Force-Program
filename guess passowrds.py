from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(5) #gives 5 seconds to tab into text box

filepath = ("passwords.txt") #requires propper text file
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		keyboard.type("{}".format(line.strip()))
		line = fp.readline()
		cnt += 1
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(0.01) #waits for windows to respond to the keyboard input, can be modified