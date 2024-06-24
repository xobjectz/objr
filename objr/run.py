# This file is placed in the Public Domain.


"runtime"


import os


from .broker   import Broker
from .commands import Commands
from .config   import Config
from .errors   import later
from .persist  import Persist


Cfg         = Config()
Cfg.dis     = ""
Cfg.mod     = "cmd,err,mod,thr"
Cfg.opts    = ""
Cfg.name    = __file__.split(os.sep)[-2]
Cfg.wdr     = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.moddir  = os.path.join(Cfg.wdr, "mods")
Cfg.pidfile = os.path.join(Cfg.wdr, f"{Cfg.name}.pid")


Persist.workdir = Cfg.wdr


broker = Broker()


def init(pkg, modstr, disable=None):
    "scan modules for commands and classes"
    mds = []
    for mod in spl(modstr):
        if disable and mod in spl(disable):
            continue
        module = getattr(pkg, mod, None)
        if not module:
            continue
        if "init" not in dir(module):
            continue
        try:
            module.init()
        except Exception as ex:
            later(ex)
    return mds


def scan(pkg, modstr, disable=None):
    "scan modules for commands and classes"
    mds = []
    dirr = sorted([x for x in dir(pkg) if not x.startswith("__")])
    for modname in spl(modstr):
        if modname not in dirr:
            continue
        if disable and modname in spl(disable):
            continue
        module = getattr(pkg, modname, None)
        if not module:
            continue
        Commands.scan(module)
        Persist.scan(module)
    return mds



def __dir__():
    return (
        'Cfg',
        'broker'
    )
