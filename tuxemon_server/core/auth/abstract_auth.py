
# All auth methods should follow this protocol.
class AbstractAuth(object):
    def __init__(self):
        pass

    def is_authenticated(self, event):
        pass

    def configure(self, options=""):
        pass
