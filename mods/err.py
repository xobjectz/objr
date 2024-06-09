# This file is placed in the Public Domain.


"deferred exception handling"


from objr import Errors


def err(event):
    "show errors."
    nmr = 0
    event.reply(f"status: {nmr} errors: {len(Errors.errors)}")
    for exc in Errors.errors:
        txt = Errors.formatexc(exc)
        for line in txt.split():
            event.reply(line)
