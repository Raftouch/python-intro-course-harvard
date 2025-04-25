import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(name=sys.argv[1])