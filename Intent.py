from abc import ABCMeta, abstractmethod
class Intent(object):	
	def __init__(self, name, params, action, slots):
		self.name = name
		self.action = action
		self.params = []
		self.slots = slots
		for param in params:
			# print param['required']
			self.params += [Parameter(param)]

class Parameter():
	def __init__(self, info):
		self.name = info['name']
		self.placeholder = info['placeholder']
		self.prompts = info['prompts']
		self.required = info['required']
		self.context = info['context']
