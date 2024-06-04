# This file is placed in the Public Domain.


"locate"


from objr.object import fmt


def fnd(event):
    if not event.args:
        event.reply("fnd <type>")
        return
    otype = event.args[0]
    clz = broker.long(otype)
    nmr = 0
    for fnm, obj in broker.find(event.gets, match=clz):
        event.reply(f"{nmr} {fmt(obj)}")
        nmr += 1
    if not nmr:
        event.reply("no result")
