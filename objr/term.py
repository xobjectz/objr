# This file is placed in the Public Domain.


"console"


from .cli   import CLI
from .event import Event
from .run   import fleet


class Console(CLI):

    "Console"

    def __init__(self, outer, inner, prompt="> "):
        CLI.__init__(self, outer)
        self.inner = inner
        self.prompt = prompt
        fleet.register(self)

    def announce(self, txt):
        "echo text"

    def callback(self, evt):
        "wait for callback."
        CLI.callback(self, evt)
        evt.wait()

    def poll(self):
        "poll console and create event."
        evt = Event()
        evt.txt = self.inner(self.prompt)
        evt.type = "command"
        return evt
