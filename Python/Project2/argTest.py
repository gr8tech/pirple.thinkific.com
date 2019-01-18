import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
	'--hints', dest='hints',  action='store_true',  default=False, help='display hints')
parser.add_argument(
	'--single', dest='single',  action='store_true',  default=False, help='play single game')

args = parser.parse_args()

print("args")
print(args.hints)
print(args.single)

