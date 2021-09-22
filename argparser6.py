"""
N: number
?: 0 or 1 argument
*: 0 or all argument
+: ALL and atleat one argument
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--three', nargs=3)

parser.add_argument('--optional', nargs='?')
parser.add_argument('--all', nargs='*', dest='all')
parser.add_argument('--one-or-more', nargs='+')

print(parser.parse_args())