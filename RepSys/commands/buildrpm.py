from RepSys.command import do_command
from RepSys.rpmutil import build_rpm
from optparse import *

HELP = """\
Usage: repsys buildrpm [OPTIONS]

Builds the binary RPM(s) (.rpm) file(s) of a given package.

Options:
    -bX        Build stage option, where X is stage, default is -bb
    -I         Don't automatically try install missing build dependencies
    -L         Disable rpmlint check of packages built
    -P USER    Define the RPM packager information to USER
    -d         Use DNF
    -q         Quiet build output
    -s         Jump to specific build stage (--short-circuit)
    -l         Use subversion log to build rpm %changelog
    -F         Do not use full name & email for packagers in %changelog
    --         Options and arguments following will be passed to rpmbuild

"""

def parse_options():
    parser = OptionParser(HELP)
    parser.add_option("-b", dest="build_cmd", default="a")
    parser.add_option("-I", dest="installdeps", action="store_false", default=True)
    parser.add_option("-L", dest="rpmlint", action="store_false", default=True)
    parser.add_option("-P", dest="packager", default="")
    parser.add_option("-d", "--dnf", dest="use_dnf", action="store_true", default=False)
    parser.add_option("-q", "--quiet", dest="verbose", action="store_false", default=True)
    parser.add_option("-s", "--short-circuit", dest="short_circuit", action="store_true", default=False)
    parser.add_option("-l", dest="svnlog", action="store_true", default=False)
    parser.add_option("-F", dest="fullnames", default=True,
            action="store_false")
    opts, args = parser.parse_args()
    opts.rpmargs = parser.rargs
    return opts

def main():
    do_command(parse_options, build_rpm)

# vim:et:ts=4:sw=4
