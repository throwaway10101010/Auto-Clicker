import pynput
import time

from pynput.mouse import Button, Controller, Listener


class auto_clicker:
	def __init__(self, delay):
		self.mouse = Controller()
		self.time_delay = delay
		self.enable_clicker = False

	def click_mouse(self):
		self.mouse.press(Button.left)
		self.mouse.release(Button.left)


	def run_clicker(self):
		while self.enable_clicker:
			time.sleep(self.time_delay)
			self.click_mouse()

	def start_auto_clicker(self):
		self.enable_clicker = True
		self.run_clicker()

	def stop_auto_clicker(self):
		self.enable_clicker = False



delay_in_seconds = 0.1
auto = auto_clicker(delay_in_seconds)
auto.start_auto_clicker()

