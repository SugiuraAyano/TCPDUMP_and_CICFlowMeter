from os import walk
import pandas as pd

file = []

for (dirpath, dirnames, filenames) in walk("./csv"):
    file.extend(filenames)


for filename in file:
    # print(filename)
    if filename.endswith(".csv"):
       continue
    else:
        file.remove(filename)

file.pop()

for filename in file:
    df = pd.read_csv("./csv/" + filename, header=None)
    df = df.drop_duplicates()
    df.to_csv("./csv/" + filename, index=False, header=False)