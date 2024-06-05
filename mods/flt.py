# This file is placed in the Public Domain.


"fleet"


from ..handler import Handler
from ..run     import broker
from ..thread  import name


def flt(event):
    "list of bots."
    bots = []
    for obj in broker.all():
        if not isinstance(obj, Handler):
            continue
        bots.append(obj)
    try:
        event.reply(bots[int(event.args[0])])
    except (IndexError, ValueError):
        event.reply(",".join([name(x).split(".")[-1] for x in bots]))
