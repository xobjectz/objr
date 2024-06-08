# This file is placed in the Public Domain.


"disk"


import os
import pathlib
import _thread


from objx import Object, ident, read, write


from .run import broker
from .utils  import strip


lock = _thread.allocate_lock()


class Workdir(Object): # pylint: disable=R0903

    "Workdir"

    workdir = ""


def fetch(obj, pth):
    "read object from disk."
    with lock:
        pth2 = store(pth)
        read(obj, pth2)
        return strip(pth)


long = broker.long


def lsstore():
    "return types stored."
    return os.listdir(store())


def skel():
    "create directory,"
    pth  = os.path.join(Workdir.workdir, "store", "")
    path = pathlib.Path(pth)
    path.mkdir(parents=True, exist_ok=True)


def store(pth=""):
    "return objects directory."
    return os.path.join(Workdir.workdir, "store", pth)


def sync(obj, pth=None):
    "sync object to disk."
    with lock:
        if pth is None:
            pth = ident(obj)
        pth2 = store(pth)
        write(obj, pth2)
        return pth


def __dir__():
    return (
        'fetch',
        'long',
        'lsstore',
        'skel',
        'store',
        'sync'
    )
