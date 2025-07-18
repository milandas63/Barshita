name = "Barshita Pattnaik"
for i in name:
    print(i, end='-')

print()

# print in reverse
for i in range(len(name)-1, -1, -1):
    print(name[i], end='')

print()

# string slicing
print(name[8::])
print(name[8:13:])
print(name[::-1])
print(name[0::2])