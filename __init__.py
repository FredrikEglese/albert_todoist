# -*- coding: utf-8 -*-

"""Extension to create todoist events via ifttt"""

import requests
import os

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Todoist"
__version__ = "0.1"
__trigger__ = "td "
__author__ = "Fredrik Eglese"
__dependencies__ = []

def handleQuery(query):
  if query.isTriggered and query.string.strip():
   	return [
		Item(
    		id=__prettyname__,
     		text=__prettyname__,
      		subtext="Submit task today",
			completion=query.rawString,
			actions = [
				FuncAction(
					"Submit task today",
					lambda: sendRequest(query.string.strip(), "today"),
				) 
			]
		), Item(
    		id=__prettyname__,
     		text=__prettyname__,
      		subtext="Submit task tomorrow",
			completion=query.rawString,
			actions = [
				FuncAction(
					"Submit task today",
					lambda: sendRequest(query.string.strip(), "tomorrow"),
				)
			],
		)
	]
		

def sendRequest(inpstr, date):
	# TODO: Get this block to work therefore allowing a config file
	# with open("accesskey.txt", "r") as f:
	# 	accessKey = f.read().splitlines()[0]
	# 	f.close()

	accessKey = ""

	baseurl = "https://maker.ifttt.com/trigger/todoist_new_event/with/key/%s" % accessKey
	myobj = {'value1':inpstr,'value2':date}
	return requests.post(baseurl, data = myobj)
	
