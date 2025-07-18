import argparse

parser = argparse.ArgumentParser(description="greet the user")
parser.add_argument("name", help="name of the user")
args = parser.parse_args()

print(f"hello, {args.name}!")
