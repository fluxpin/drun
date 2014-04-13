import contextlib as ctx
import itertools as it
import operator as op
import os

from drun.cfg import MENUS

def format_menu(menu, *entries):
    menu.append('\n'.join(it.chain(*entries)) + '\n')
    return menu

def list_menus(cfg):
    return it.imap(op.itemgetter(0), cfg[MENUS])

@ctx.contextmanager
def working_dir(path):
    cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(cwd)

def is_exec(path):
    return os.path.isfile(path) and os.access(path, os.X_OK)

def listdir_exec(path):
    try:
        with working_dir(path):
            # Lazy evaluation interacts badly with global state
            return list(it.ifilter(is_exec, os.listdir(os.curdir)))
    except OSError:
        return []

def list_path():
    path = os.getenv('PATH').split(os.pathsep)
    return sorted(it.chain(*it.imap(listdir_exec, path)))
