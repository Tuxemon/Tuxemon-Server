import json
import logging
from tuxemon_server.core import parser
from tuxemon_server.core import event

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

class JSONParser(parser.AbstractParser):
    """JSONParser is used to encode/decode JSON into the appropriate event structure.
    """

    def parse(self, string, source):
        try:
            data = json.loads(string)
        except Exception as e:
            logger.warning("Error decoding JSON: {}".format(str(e)))
            logger.warning("  Data is not valid JSON: {}".format(str(string)))
            return event.Event(type="DECODING_ERROR", target=string, source=source)

        # Verify recieved data is an event.
        if "type" not in data or "target" not in data:
            logger.error("Parsed JSON is not an event: {}".format(str(data)))
            return event.Event(type="MALFORMED_EVENT", target=data, source=source)

        return event.Event(type=data['type'], target=data['target'], source=source)

    def encode(self, data):
        response = {"results": [], "errors": [], "warnings": []}

        try:
            encoded_data = json.dumps(data)
            return encoded_data
        except Exception as e:
            logger.error("Unable to encode data to JSON: {}".format(str(e)))
            logger.error("  Data: {}".format(str(data)))
            raise

