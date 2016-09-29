import json
from st2actions.runners.pythonrunner import Action

class JsonEncodeAction(Action):
    def run(self, jsonstr):
        try:
            return (True, json.loads(jsonstr))
        except Exception as e:
            return (False, e)

