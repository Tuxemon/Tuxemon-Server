import json
from tuxemon_server.core import parser
from tuxemon_server.core import event

class JSONParser(parser.AbstractParser):

    def parse(self, string):
        try:
            data = json.loads(string)
        except Exception as e:
            print(e)
            return None

        # Verify recieved data is an event.
        if "type" not in data or "target" not in data:
            print("Parsed JSON is not an event: " + str(data))
            return None

        return event.Event(type=data['type'], target=data['target'])
