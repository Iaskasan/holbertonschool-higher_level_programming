import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, "r") as f:
        filename = json.load(f)
        return filename
