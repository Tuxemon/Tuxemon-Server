import inspect
import importlib

modules = []

# All supported transports
module_suffix = "Transport"
all_transports = {}
Provider = None

def import_module(module_name):
    """Imports a transport plugin module
    """
    print(__name__ + "." + module_name)
    m = importlib.import_module(__name__ + ".plugin_" + module_name)
    modules.append(m)
    transports = [obj for obj in m.__dict__.values() if inspect.isclass(obj)]
    for t in transports:
        transport = t()
        all_transports[t.__name__.lower()] = transport

def configure(provider, parser, address, port):
    """Configures and returns the specified transport.
    """
    global Provider
    if "plugin_" in provider:
        provider = provider.replace("_plugin", "")
    import_module(provider.lower())
    transport = all_transports[provider.lower() + module_suffix.lower()]
    transport.configure(parser, address, port)
    Provider = transport

    return transport


