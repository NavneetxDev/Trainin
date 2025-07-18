import argparse

parser = argparse.ArgumentParser(description="greet the user")
parser.add_argument("name", help="user's name")
parser.add_argument("--age", type=int, help="user's age")
parser.add_argument("--shout", action="store_true", help="shout the greeting")

args = parser.parse_args()

greet = f"hello {args.name}!"

if args.age:
    greet += f" you are {args.age} years old."

if args.shout:
    greet = greet.upper()

print(greet)
