import inspect
import importlib

# Transport modules to import
__all__ = ("websockets",)

# All transports should follow this protocol.a
class AbstractTransport(object):
    def __init__(self):
        pass

    def configure(self, parser, address, port):
        pass

    def listen(self):
        pass

modules = []

# All supported transports
module_suffix = "Transport"
all_transports = {}
Provider = None

for module_name in __all__:
    print(__name__ + "." + module_name)
    m = importlib.import_module(__name__ + "." + module_name)
    modules.append(m)
    transports = [obj for obj in m.__dict__.values() if inspect.isclass(obj)]
    for t in transports:
        transport = t()
        all_transports[t.__name__.lower()] = transport

def configure(provider, parser, address, port):
    """Configures and returns the specified transport.
    """
    global Provider
    transport = all_transports[provider.lower() + module_suffix.lower()]
    transport.configure(parser, address, port)
    Provider = transport

    return transport


