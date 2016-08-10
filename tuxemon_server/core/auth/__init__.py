import inspect
import importlib

# Database modules to import
__all__ = ("token",)

# Used to call the configured auth.
def ProviderAnonymousAccess(func):
    def wrapper(self, event):
        global AnonymousAccess
        func(self, AnonymousAccess(self, event))
    return wrapper

# Used to call the configured auth.
def ProviderAuthenticatedAccess(func):
    def wrapper(self, event):
        global AuthenticatedAccess
        func(self, AnonymousAccess(self, event))
    return wrapper


modules = []

# All supported databases
anonymous_suffix = "AnonymousAccess"
authenticated_suffix = "AuthenticatedAccess"
AnonymousAccess = ProviderAnonymousAccess
AuthenticatedAccess = ProviderAuthenticatedAccess
all_auth_methods = {}

for module_name in __all__:
    m = importlib.import_module(__name__ + "." + module_name)
    modules.append(m)
    functions = [func for func in m.__dict__.values() if inspect.isfunction(func)]
    for func in functions:
        all_auth_methods[func.__name__.lower()] = func

def configure(provider):
    """Configures and returns the specified database.
    """
    global AnonymousAccess
    global AuthenticatedAccess
    print("Using provider:", provider)
    AnonymousAccess = all_auth_methods[provider.lower() + anonymous_suffix.lower()]
    AuthenticatedAccess = all_auth_methods[provider.lower() + authenticated_suffix.lower()]

