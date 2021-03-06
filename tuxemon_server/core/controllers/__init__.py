import inspect
import importlib

# Controller modules to import
__all__ = ("error", "event", "input", "account")

# All controllers/handlers should implement this protocol.
class AbstractHandler(object):
    def __init__(self):
        self.event_type = "EVENT_TYPE"
        self.required_fields = []

    def _has_required_fields(self, event):
        """Verifies that the given event has the required fields for this handler.
        """
        has_fields = True
        for field in self.required_fields:
            if type(event.target) != dict:
                has_fields = False
                break
            if field not in event.target.keys():
                has_fields = False

        return has_fields


    def invoke(self, event):
        """Invoke should return a result, warning, and error response.
        """
        pass

modules = []
all_controllers = {}

for module_name in __all__:
    m = importlib.import_module(__name__ + "." + module_name)
    modules.append(m)
    handlers = [obj for obj in m.__dict__.values() if inspect.isclass(obj)]
    for h in handlers:
        handler = h()
        if "event_type" in handler.__dict__:
            all_controllers[handler.event_type] = handler

