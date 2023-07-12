# Import the library
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
# with "--"
parser.add_argument('--name', type=str, required=True, help="Input your name")
parser.add_argument('--age', type=int, help="Inpurt your age")
# w/out "--"
# parser.add_argument('name', type=str, help="Input your name")
# parser.add_argument('age', type=int, help="Input your age")

# Parse the argument
args = parser.parse_args()

if args.age:
    # Print the user input argument
    print("Name: ", args.name)
    print("Age: ", args.age)
else:
    print("Hi " + args.name + ". Please input your age.")