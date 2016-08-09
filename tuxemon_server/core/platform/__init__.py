"""
Put platform specific fixes here
"""
__all__ = ('init')

from os.path import expanduser

def init():
    pass

def get_config_path():
    return expanduser("~")

