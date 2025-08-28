import os
import sys


def resource_path(*paths):
    # Em runtime do PyInstaller, sys._MEIPASS aponta p/ pasta temporária
    base = getattr(sys, "_MEIPASS", os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    return os.path.join(base, *paths)