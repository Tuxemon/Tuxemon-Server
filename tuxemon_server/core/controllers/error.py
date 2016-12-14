import logging
import datetime
from tuxemon_server.core import auth
from tuxemon_server.core import database
from tuxemon_server.core import tools
from tuxemon_server.core.controllers import abstract_controller

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)


class DecodingErrorHandler(abstract_controller.AbstractHandler):
    def __init__(self):
        abstract_controller.AbstractHandler.__init__(self)
        self.event_type = "DECODING_ERROR"

    def invoke(self, event):
        result = None
        error = "Decoding error."
        warning = None

        return result, warning, error

class EncodingErrorHandler(abstract_controller.AbstractHandler):
    def __init__(self):
        abstract_controller.AbstractHandler.__init__(self)
        self.event_type = "ENCODING_ERROR"

    def invoke(self, event):
        result = None
        error = "Encoding error."
        warning = None

        return result, warning, error

class MalformedEventHandler(abstract_controller.AbstractHandler):
    def __init__(self):
        abstract_controller.AbstractHandler.__init__(self)
        self.event_type = "MALFORMED_EVENT"

    def invoke(self, event):
        result = None
        error = "Malformed event."
        warning = None

        return result, warning, error
