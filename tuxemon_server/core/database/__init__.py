import inspect
import importlib

# Database modules to import
__all__ = ("mongodb", "sqlite")

# All database providers should follow this protocol.
class AbstractDatabase(object):
    def configure(self, host, port, username, password, ssl, db_name):
        pass

    def find_all(self, collection_name, field, value):
        """Find all entries from a collection using a query

        Args:
            colleciton_name: The collection from which you want to get all entries from
            query: A dictionary of keys and value for the query
        """
        pass


    def find_one(self, collection_name, field, value):
        """Find one and only one entry from a collection using a query

        Args:
            colleciton_name: The collection from which you want to get all entries from
            query: A dictionary of keys and value for the query
        """
        pass


    def count(self, collection_name, field, value):
        pass


    def drop(self, collection_name):
        pass

    def save(self, collection_name, data):
        pass


modules = []

# All supported databases
module_suffix = "Database"
all_databases = {}
Provider = None

for module_name in __all__:
    m = importlib.import_module(__name__ + "." + module_name)
    modules.append(m)
    dbs = [obj for obj in m.__dict__.values() if inspect.isclass(obj)]
    for d in dbs:
        db = d()
        all_databases[d.__name__.lower()] = db

def configure(provider, host, port, username, password, ssl, db_name):
    """Configures and returns the specified database.
    """
    global Provider
    database = all_databases[provider.lower() + module_suffix.lower()]
    database.configure(host, port, username, password, ssl, db_name)
    Provider = database

    return database



