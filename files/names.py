names = []

## WRITE

# name = input("What's your name? ")

# file = open("files/names.txt", "w")
# with open("files/names.txt", "a") as file:
#     file.write(f"{name}\n")


##  READ

with open("files/names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(name)
