import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) == 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {len(sys.argv) - 1}")
count = 1
for args in sys.argv[1:]:
    print(f"Argument {count}: {args}")
    count += 1
print(f"Total arguments: {len(sys.argv)}")