from collections import namedtuple
from tuxemon_server.core import controllers
import logging

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

# Create an event object for parsed events.
Event = namedtuple("Event", ["type", "target"])

class EventPool(object):
    def __init__(self):
        self._event_handlers = {}

    def add_handler(self, event_type, handler):
        logger.debug("Adding event handler for event type: {}".format(event_type))
        if event_type not in self._event_handlers:
            self._event_handlers[event_type] = []
        self._event_handlers[event_type].append(handler)

    def dispatch(self, event):
        response = ""
        if event.type in self._event_handlers:
            response = self.invoke_handlers(event)
        else:
            response = "Event type not supported: " + event.type
            logger.error(response)
            print(response)

        return response

    def invoke_handlers(self, event):
        response = ""
        # TODO: We need to handle multiple responses from all handlers for an
        # event.
        for event_handler in self._event_handlers[event.type]:
            handler_response = event_handler.invoke(event)
            if handler_response:
                response += handler_response

        return response

# Shared instance of event pool.
event_pool = EventPool()

# Get all controllers and add them as a handler for the shared event pool.
for event_type, handler in controllers.all_controllers.items():
    event_pool.add_handler(event_type, handler)
