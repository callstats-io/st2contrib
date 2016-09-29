from lib import action
import json

class ConsulPutObjectAction(action.ConsulBaseAction):
    def run(self, key, value):
        return self.consul.kv.put(key, json.dumps(value))
