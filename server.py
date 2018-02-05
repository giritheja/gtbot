"""
Author: Giritheja
Email: s.giritheja@gmail.com

A basic server script to leverage rasa's NLU.
"""

#!/usr/bin/env python
import web #easy_install web.py
import sys
import json
import os

from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

port = 8080

urls = ('/ask', 'ask')
model_directory = './default/model_20180204-142356'
interpreter = Interpreter.load(model_directory, RasaNLUConfig("./config_spacy.json"))

class MyApplication(web.application): 
    def run(self, port=8080, *middleware): 
        func = self.wsgifunc(*middleware) 
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

app = MyApplication(urls, globals())

class ask:
	# print interpreter.parse(u"hello")
	def GET(self):
		print "hello"
		i = web.input(_unicode=True)
		return interpreter.parse(i.q)

if __name__ == '__main__':
    app.run(port=port)