NAME

::

    OBJR - objects runtime


SYNOPSIS

::

    >>> from objr import Object, read, write
    >>> o = Object()
    >>> path = write(o)
    >>> oo = Object()
    >>> read(oo, path)


DESCRIPTION

::

    OBJR has all you need to program a unix cli program, such as disk
    perisistence for configuration files, event handler to handle the
    client/server connection, code to introspect modules for
    commands, deferred exception handling to not crash on an error, a
    parser to parse commandline options and values, etc.

    OBJR is Public Domain.


FILES

::

    ~/.local/pipx/venvs/objr/

AUTHOR

::

    Bart Thate <objx@proton.mel>

COPYRIGHT

::

    OBJR is Public Domain.
