import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="enable verbose mode", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("verbose mode is on.")
else:
    print("verbose mode is off.")
