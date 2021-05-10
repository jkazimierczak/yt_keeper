import sys

from .keeper import Keeper


try:
    Keeper.keep_all()
except KeyboardInterrupt:
    print('Terminating process...')
    sys.exit(0)
