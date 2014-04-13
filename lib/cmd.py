import shlex
import subprocess as sp

def run(cmd, **kwargs):
    return sp.Popen(shlex.split(cmd), **kwargs)

def read_cmd(cfg, menu):
    while True:
        dmenu = run(cfg, stdin=sp.PIPE, stdout=sp.PIPE)
        cmd = dmenu.communicate(menu)[0][:-1] # trailing newline
        if dmenu.returncode:
            break
        yield cmd
