import re
import shlex
import subprocess as sp

from drun.cfg import COMMANDS, DMENU, MENUS
from drun.menu import format_menu

def run(cmd, **kwargs):
    return sp.Popen(shlex.split(cmd), **kwargs)

def read_cmd(cfg, menu):
    while menu:
        dmenu = run(cfg[DMENU], stdin=sp.PIPE, stdout=sp.PIPE)
        cmd = dmenu.communicate(menu[-1])[0][:-1] # trailing newline
        if dmenu.returncode:
            menu.pop()
            continue
        for mcmd in cfg[MENUS]:
            if cmd == mcmd[0]:
                format_menu(menu, mcmd[1:])
                break
        else:
            yield cmd

def special_cmd(cfg, cmd):
    while True:
        for scmd in cfg[COMMANDS]:
            match = re.match(scmd[0], cmd)
            if match:
                cmd = scmd[1].format(match.group(0), *match.groups())
                break
        else:
            return cmd
