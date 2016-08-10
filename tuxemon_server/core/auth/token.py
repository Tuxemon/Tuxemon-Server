import logging
from tuxemon_server.core import auth
from tuxemon_server.core import database

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

def TokenAnonymousAccess(self, event):
    print("Anonymous authentication completed.")
    return event

def TokenAuthenticatedAccess(self, event):
    print("TODO: Check token in event and compare it against db.")
    return event
