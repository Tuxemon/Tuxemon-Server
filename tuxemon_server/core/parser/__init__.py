import inspect
import importlib

# Parser modules to import
__all__ = ("json",)

# All parsers should follow this protocol.
class AbstractParser(object):
    def __init__(self):
        pass

    def configure(self):
        pass

    def parse(self, data):
        pass

modules = []

# All supported parsers
module_suffix = "Parser"
all_parsers = {}
Provider = None

for module_name in __all__:
    m = importlib.import_module(__name__ + "." + module_name)
    modules.append(m)
    parsers = [obj for obj in m.__dict__.values() if inspect.isclass(obj)]
    for p in parsers:
        parser = p()
        all_parsers[p.__name__.lower()] = parser

def configure(provider):
    """Configures and returns the specified parser.
    """
    global Provider
    parser = all_parsers[provider.lower() + module_suffix.lower()]
    parser.configure()
    Provider = parser
    return parser
