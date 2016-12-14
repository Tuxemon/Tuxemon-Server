import logging
from tuxemon_server.core.auth import abstract_auth

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

class TokenAuth(abstract_auth.AbstractAuth):
    def __init__(self):
        pass

    def is_authenticated(self, event):
        pass

