# This file is placed in the Public Domain.
# pylint: disable=W0212,W0718,E0401


"main"


import getpass
import os
import pathlib
import pwd
import readline
import sys
import termios
import time


from .cli      import CLI
from .commands import Commands, command
from .console  import Console
from .errors   import Errors, errors, later
from .event    import Event
from .help     import TXT
from .log      import Logging
from .parse    import parse
from .persist  import Persist, skel
from .run      import Cfg
from .utils    import spl


from . import modules
from . import user


if os.path.exists("mods"):
    import mods as MODS
else:
    MODS = None


def cmnd(txt, outer=print):
    "do a command using the provided output function."
    cli = CLI()
    cli.out = outer
    evn = Event()
    evn.txt = txt
    command(cli, evn)
    evn.wait()
    return evn


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


def modnames():
    "list all modules."
    return sorted({x for x in dir(modules) + dir(user) + dir(MODS) if not x.startswith("__")})


def __dir__():
    return (
        'cmnd',
        'init',
        'scan',
        'modnames'
    )
