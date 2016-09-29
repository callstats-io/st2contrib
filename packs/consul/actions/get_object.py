from lib import action
import json

class ConsulGetObjectAction(action.ConsulBaseAction):
    def run(self, key):
        list, value = self.consul.kv.get(key)
        value['Value'] = json.loads(value['Value'])
        return value
