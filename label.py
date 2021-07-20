from os import walk
import pandas as pd
import socket

file = []

# from https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    
    # print(IP)
    return IP

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
    df = pd.read_csv("./csv/" + filename)
    for i in range(0, df.shape[0]):
        if df.loc[i, "Src IP"] == get_ip():
            df.loc[i, "Label"] = "From My Computer"
        else:
            df.loc[i, "Label"] = "From Others Computer"
    
    df.to_csv("./csv/" + filename, index=False)
    df.to_json("./json/" + filename[:-4] + ".json")
