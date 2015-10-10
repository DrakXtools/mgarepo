#!/usr/bin/python
#
# This program will try to patch a spec file from a given package url.
#
from MgaRepo import Error
from MgaRepo.rpmutil import patch_spec
from MgaRepo.command import *
from MgaRepo.layout import package_url
import getopt
import sys

HELP = """\
Usage: mgarepo patchspec [OPTIONS] REPPKGURL PATCHFILE

It will try to patch a spec file from a given package url.

Options:
    -l LOG  Use LOG as log message
    -h      Show this message

Examples:
    mgarepo patchspec http://repos/svn/cnc/snapshot/foo
"""

def parse_options():
    parser = OptionParser(help=HELP)
    parser.add_option("-l", dest="log", default="")
    opts, args = parser.parse_args()
    if len(args) != 2:
        raise Error("invalid arguments")
    opts.pkgdirurl = package_url(args[0], mirrored=False)
    opts.patchfile = args[1]
    return opts

def main():
    do_command(parse_options, patch_spec)

# vim:et:ts=4:sw=4
