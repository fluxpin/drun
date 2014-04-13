import re
import shlex
import subprocess as sp

from drun.cfg import COMMANDS, DMENU

def run(cmd, **kwargs):
    return sp.Popen(shlex.split(cmd), **kwargs)

def read_cmd(cfg, menu):
    while True:
        dmenu = run(cfg[DMENU], stdin=sp.PIPE, stdout=sp.PIPE)
        cmd = dmenu.communicate(menu)[0][:-1] # trailing newline
        if dmenu.returncode:
            break
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
