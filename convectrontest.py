#!/usr/bin/python3

"""
initialize Isotemp water bath, then provide user with an interactive console for debugging
"""

import convectron475 as convectron
import traceback

gauge = convectron.ConvectronController(port="/dev/cu.usbserial-ftE17ZWN")

while True:
	cmd = input("gauge.")
	try:
		ret = eval("gauge.{}".format(cmd))
		print(ret)
	except:
		traceback.print_exc()
		gauge.disconnect()