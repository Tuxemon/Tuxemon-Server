import logging
import datetime
from tuxemon_server.core import auth
from tuxemon_server.core import database
from tuxemon_server.core import tools
from tuxemon_server.core.controllers import abstract_controller

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

class RegisterHandler(abstract_controller.AbstractHandler):
    def __init__(self):
        abstract_controller.AbstractHandler.__init__(self)
        self.event_type = "REGISTER"
        self.required_fields = [
            "username",
            "password",
            "email"
        ]

    def invoke(self, event):
        result = None
        warning = None
        error = None

        if not self._has_required_fields(event):
            error = "Event does not have the required fields."
            return result, warning, error

        # Check to see if username is taken.
        result = database.Provider.find_one("accounts", "username", event.target["username"])
        if result:
            error = "Username has already been taken."
            return result, warning, error

        # If username is not taken, create a new account.
        data = {
            "accountId": tools.generate_id(),
            "username": event.target["username"],
            "password": tools.hash_password(event.target["password"]),
            "email": event.target["email"],
        }
        result = database.Provider.save("accounts", data)

        return result, warning, error

class TokenLoginHandler(abstract_controller.AbstractHandler):
    def __init__(self):
        abstract_controller.AbstractHandler.__init__(self)
        self.event_type = "LOGIN"
        self.required_fields = [
            "accountId",
            "password"
        ]

    def invoke(self, event):
        result = None
        warning = None
        error = None

        if not self._has_required_fields(event):
            error = "Event does not have the required fields."
            return result, warning, error

        # Verify user credentials in database.
        result = database.Provider.find_one("accounts", "accountId", event.target["accountId"])
        if not result:
            error = "Incorrect username or password."
            return result, warning, error

        # Verify supplied password with password stored in the database.
        if not tools.verify_password(event.target["password"], result["password"]):
            error = "Incorrect username or password."
            return result, warning, error

        # If password is verified, generate and save a login token.
        token = tools.generate_id()
        expires = datetime.date.today() + datetime.timedelta(days=30)
        data = {
            "accountId": event.target["accountId"],
            "token": token,
            "expires": expires,
        }
        database.Provider.save("tokens", data)

        return data, warning, error

class DeleteAccountHandler(abstract_controller.AbstractHandler):
    def __init__(self):
        abstract_controller.AbstractHandler.__init__(self)
        self.event_type = "DELETE_ACCOUNT"
        self.required_fields = []

    def invoke(self, event):
        result = None
        warning = None
        error = None

        return result, warning, error
