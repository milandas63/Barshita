handle = open("story.txt", "r")

for e in iter(lambda: handle.read(1), ""):
    print(e)

handle.close()
