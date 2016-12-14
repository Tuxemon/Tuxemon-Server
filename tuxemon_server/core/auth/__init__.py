import inspect
import importlib

modules = []

module_suffix = "Auth"
all_auth = {}
Provider = None

def import_module(module_name):
    """Imports an auth plugin module
    """
    print(__name__ + "." + module_name)
    m = importlib.import_module(__name__ + "." + module_name)
    modules.append(m)
    auths = [obj for obj in m.__dict__.values() if inspect.isclass(obj)]
    for a in auths:
        auth = a()
        all_auth[a.__name__.lower()] = auth

def configure(provider):
    """Configures and returns the specified transport.
    """
    global Provider
    import_module(provider.lower())
    auth = all_auth[provider.lower() + module_suffix.lower()]
    auth.configure()
    Provider = auth

    return auth


