import os

root = "H:\HAIRCUT REPES"
for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        print("*"*40)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f[:-4].split(" - ")
            print(song_details)
