import argparse

parser = argparse.ArgumentParser(description="test")

parser.add_argument('count', action='store', type=int)
parser.add_argument('units', action='store')
parser.add_argument('name', action='store')
parser.add_argument('color', action='store')

print(parser.parse_args())