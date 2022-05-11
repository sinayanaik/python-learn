import sys

if len(sys.argv) == 1:
    print("No arguments")
    sys.exit()

for i in range(1, int(sys.argv[1])+1):
    print(f"{i}*{i} = {i**2}")