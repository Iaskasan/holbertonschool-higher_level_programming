import csv
import json
'''
module that converts data from a csv to json object
and write it to a .json file
'''


def convert_csv_to_json(filename):
    data = []
    try:
        with open(filename, "r", newline="") as f:
            obj = csv.DictReader(f)
            for row in obj:
                data.append(row)
        with open("data.json", "w") as j:
            json.dump(data, j)
            return True
    except FileNotFoundError:
        return False
