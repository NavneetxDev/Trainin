import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a", type=int, help="first number")
parser.add_argument("b", type=int, help="second number")
parser.add_argument("--operation", choices=["add", "subtract"], default="add")

args = parser.parse_args()

if args.operation == "add":
    print(args.a + args.b)
else:
    print(args.a - args.b)
