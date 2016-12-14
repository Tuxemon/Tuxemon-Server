
# All transports should follow this protocol.
class AbstractTransport(object):
    def __init__(self):
        pass

    def configure(self, parser, address, port):
        pass

    def listen(self):
        pass


