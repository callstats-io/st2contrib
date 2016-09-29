import sys
import json
from st2actions.runners.pythonrunner import Action

class JsonEncodeAction(Action):
    def run(self, obj):
    	try:
    		return (True, json.dumps(obj))
    	except Exception as e:
        	return (False, e)
