import inspect
import importlib

# Controller modules to import
__all__ = ("event", "input")

modules = []

# All functions: {'test_event': <function test_event at 0x7ffa60d0da28>,
#                 'move_player': <function move_player at 0x7ffa60d0daa0>}
all_functions = {}

for module_name in __all__:
    m = importlib.import_module(__name__ + "." + module_name)
    modules.append(m)
    functions = [func for func in m.__dict__.itervalues() if inspect.isfunction(func)]
    for func in functions:
        all_functions[func.__name__] = func

