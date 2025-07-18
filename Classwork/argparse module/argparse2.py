import argparse

parser = argparse.ArgumentParser(description="add two numbers")
parser.add_argument("num1", type=int, help="first number")
parser.add_argument("num2", type=int, help="second number")

args = parser.parse_args()

total = args.num1 + args.num2
print("sum =", total)
