import sys
args = sys.argv
print("Number of arguments: ", len(args), "arguments.")
for i, arg in enumerate(args):
    print("Argument #", i, ":", arg)
