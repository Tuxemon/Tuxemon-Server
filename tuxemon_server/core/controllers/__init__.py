import inspect
import importlib

# Controller modules to import
__all__ = ("event", "input", "register")

modules = []

# All functions: {'test_event': <function test_event at 0x7ffa60d0da28>,
#                 'move_player': <function move_player at 0x7ffa60d0daa0>}
all_controllers = {}

for module_name in __all__:
    m = importlib.import_module(__name__ + "." + module_name)
    modules.append(m)
    handlers = [obj for obj in m.__dict__.values() if inspect.isclass(obj)]
    for h in handlers:
        handler = h()
        all_controllers[handler.name] = handler

class AbstractHandler(object):
    def __init__(self):
        self.name = "EVENT_TYPE"

    def invoke(self, event):
        pass
