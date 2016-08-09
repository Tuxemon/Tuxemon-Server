from tuxemon_server.core.service import db

class RegisterHandler(object):
    def __init__(self):
        self.name = "REGISTER"

    def invoke(self, event):
        # TODO: Verify event data fields.
        # Check to see if username is taken.
        result = db.client.find_one("users", {"username": event.target["username"]})
        print(result)
        if result:
            return "Username taken"

