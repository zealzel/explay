import os
import sys
import shutil
import random
import hashlib
import importlib
import threading
from contextlib import suppress
from collections import defaultdict
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from explay.post_func import common_funcs


def is_buildin(func_str):
    try:
        eval(func_str)
        return True
    except NameError as ex:
        return False


def replace_str(my_string, spans, replaced_words):
    cursor = 0
    new_string = ""
    for span, word in zip(spans, replaced_words):
        prev_str = my_string[cursor : span[0]]
        next_str = my_string[span[0] : span[1]]
        new_string += prev_str + str(word)
        cursor = span[1]
    new_string += my_string[cursor:]
    return new_string


def resource_path(relative_path, cwd=None):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    if cwd:
        base_path = getattr(sys, "_MEIPASS", cwd)
    return os.path.join(base_path, relative_path)


def register_custom_func(name, func):
    global common_funcs
    common_funcs[name] = func


def register_func(workdir):

    exe_location = os.path.dirname(shutil.which("pip"))
    # The location of pip is the same as the executable
    # Find the location of pip first
    if not exe_location:
        print("Please install pip first.")
        return

    cwd = os.getcwd()
    print("cwd", cwd)
    print("workdir", workdir)

    func_temp_name = "func_temp"
    func_temp_py = f"{func_temp_name}.py"
    path1 = resource_path(func_temp_py)
    path2 = resource_path(func_temp_py, cwd)
    path3 = os.path.join(exe_location, func_temp_py)

    print("__file__", __file__)
    print("func_temp_name", func_temp_name)
    print("func_temp_py", func_temp_py)
    print("path1", path1)
    print("path2", path2)
    print("path3", path3)
    print("exe_location", exe_location)

    if not os.path.isfile(os.path.join(workdir, "func.py")):
        return

    shutil.copy(os.path.join(workdir, "func.py"), path1)
    shutil.copy(os.path.join(workdir, "func.py"), path2)
    shutil.copy(os.path.join(workdir, "func.py"), path3)
    if func_temp_name in sys.modules:
        del sys.modules[func_temp_name]

    print("sys.path", sys.path)
    sys.path.append(exe_location)
    func_module = importlib.import_module("func_temp")
    print(func_module)

    print("dir", dir(func_module))
    funcs = [f for f in dir(func_module) if f.startswith("exp")]
    print("\nRegister customed functions defined in func.py")
    for func_name in funcs:
        print(f"func {func_name} registered.")
        func_name_in_yml = func_name[4:]
        register_custom_func(func_name_in_yml, getattr(func_module, func_name))

    with suppress(FileNotFoundError):
        os.remove(path1)
        os.remove(path2)
        os.remove(path3)


def pd_set_option(max_colwidth, max_columns, precision=1):
    import pandas as pd

    pd.set_option("display.expand_frame_repr", False)
    pd.set_option("display.max.colwidth", max_colwidth)
    pd.set_option("display.max_columns", max_columns)
    pd.set_option("display.precision", precision)
    pd.set_option("display.float_format", "{:20,.1f}".format)
    pd.set_option("display.unicode.east_asian_width", True)


def get_local_variables(dir):
    print(globals().keys())
    var_excludes = ["In", "Out", "exit", "quit"]
    v = sorted(filter(lambda s: not s.startswith("_"), dir))
    v = list(filter(lambda x: x not in var_excludes, v))
    return v
