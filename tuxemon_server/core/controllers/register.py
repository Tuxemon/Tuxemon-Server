import logging
from tuxemon_server.core import auth
from tuxemon_server.core import controllers
from tuxemon_server.core import database

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

class RegisterHandler(controllers.AbstractHandler):
    def __init__(self):
        controllers.AbstractHandler.__init__(self)
        self.event_type = "REGISTER"
        self.required_fields = [
            "username",
            "password",
            "email"
        ]
        auth.AnonymousAccess = "woo"

    @auth.AnonymousAccess
    def invoke(self, event):
        if not self._has_required_fields(event):
            return "Event does not have the required fields: " + str(event.target)

        # Check to see if username is taken.
        result = database.Provider.find_one("accounts", "username", event.target["username"])
        print(result)
        if result:
            return "Username taken"

        # If username is not taken, create a new account.
        data = {
            "username": event.target["username"],
            "password": event.target["password"],
            "email": event.target["email"],
        }
        result = database.Provider.save("accounts", data)
