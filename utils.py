import json

def write_list(file_name , list):
    print("Started wrinting into JSON.")
    with open(file_name, "w") as fp:
        json.dump(list, fp)
        print("Done writing JSON.")

def read_list(path:str) -> list:
    with open(path, "rb") as fp:
        list = json.load(fp)
        return list