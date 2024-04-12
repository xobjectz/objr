README
######


NAME

::

    objr - object runtime


SYNOPSIS

::

    objr <cmd> [key=val] [key==val]
    objr [-a] [-c] [-d] [-h] [-v]

    options are:

    -a     load all modules
    -c     start console
    -d     start daemon
    -h     display help
    -v     use verbose


DESCRIPTION

::

    OBJR has all you need to program a unix cli program, such as disk
    perisistence for configuration files, event handler to handle the
    client/server connection, code to introspect modules for
    commands, deferred exception handling to not crash on an error, a
    parser to parse commandline options and values, etc.

    OBJR uses OBJX, all the python3 code to program objects in a functional
    way. It provides a base Object class that has only dunder methods, all
    methods are factored out into functions with the objects as the first
    argument. It is called Object Programming (OP), OOP without the
    oriented.

    OBJX  allows for easy json save//load to/from disk of objects. It
    provides an "clean namespace" Object class that only has dunder
    methods, so the namespace is not cluttered with method names. This
    makes storing and reading to/from json possible.

    OBJR has a demo bot, it can connect to IRC, fetch and display RSS
    feeds, take todo notes, keep a shopping list and log text. You can
    also copy/paste the service file and run it under systemd for 24/7
    presence in a IRC channel.

    OBJX/OBJR is Public Domain.

USAGE

::

    without any argument the program does nothing

    $ objr
    $

    see list of commands

    $ objr cmd
    cmd,err,mod,req,thr,ver

    list of modules

    $ objr mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr

    use -c to start a console

    $ objr -c

    use mod=<name1,name2> to load additional modules

    $ objr -c mod=irc,rss
    >

    use -v for verbose

    $ objr -cv mod=irc
    OBJR started CV started Sat Dec 2 17:53:24 2023
    >


CONFIGURATION

::

    $ objr cfg 
    channel=#objr commands=True nick=objr port=6667 server=localhost

    irc

    $ objr cfg server=<server>
    $ objr cfg channel=<channel>
    $ objr cfg nick=<nick>

    sasl

    $ objr pwd <nsvnick> <nspass>
    $ objr cfg password=<frompwd>

    rss

    $ objr rss <url>
    $ objr dpl <url> <item1,item2>
    $ objr rem <url>
    $ objr nme <url> <name>


COMMANDS

::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    thr - show the running threads

SYSTEMD

::

    save the following it in /etc/systemd/system/objr.service and
    replace "<user>" with the user running pipx

    [Unit]
    Description=runtime
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.objr
    ExecStart=/home/<user>/.local/pipx/venvs/objr/bin/objr -d
    RemainAfterExit=yes

    [Install]
    WantedBy=default.target

    then run this

    $ pipx ensurepath
    $ mkdir ~/.objr
    $ sudo systemctl enable objr --now

    default channel/server is #objr on localhost

FILES

::

    ~/.objr
    ~/.local/bin/objr
    ~/.local/pipx/venvs/objr/

AUTHOR

::

    Bart Thate <bthate@dds.nl>

COPYRIGHT

::

    OBJR is Public Domain.
