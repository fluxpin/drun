import os
import sys

SYSCFG = 'share/drun/drunrc'
USRCFG = '~/.drunrc'

def prefix(relpath):
    return os.path.join(os.path.dirname(sys.path[0]), relpath)

def init_cfg():
    syscfg = prefix(SYSCFG)
    usrcfg = os.path.expanduser(USRCFG)
    while True:
        try:
            with open(usrcfg, 'rU') as u:
                return eval(u.read())
        except IOError:
            with open(syscfg, 'rU') as s, open(usrcfg, 'w') as u:
                u.write(s.read())
