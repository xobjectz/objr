# This file is placed in the Public Domain.


"runtime"


from .broker   import Broker
from .config   import Config
from .object   import pjoin
from .persist  import Persist


SEP = "/"


Cfg         = Config()
Cfg.dis     = ""
Cfg.mod     = "cmd,err,mod,thr"
Cfg.opts    = ""
Cfg.name    = __file__.split(SEP)[-2]
Cfg.wdr     = __file__.split(Cfg.name)[0] + f".{Cfg.name}"
Cfg.pidfile = pjoin(Cfg.wdr, f"{Cfg.name}.pid")


Persist.workdir = Cfg.wdr


broker = Broker()


def __dir__():
    return (
        'Cfg',
        'broker'
    )
