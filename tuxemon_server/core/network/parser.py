import json
from tuxemon_server.core.event import Event

def parse(string):
    try:
        data = json.loads(string)
    except Exception as e:
        print(e)
        return None

    # Verify recieved data is an event.
    if "type" not in data or "target" not in data:
        print("Parsed JSON is not an event: " + str(data))
        return None

    return Event(type=data['type'], target=data['target'])
