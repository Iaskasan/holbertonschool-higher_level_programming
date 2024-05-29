import requests
import json
import csv
'''module to fetch and print posts from the API'''


def fetch_and_print_posts():
    '''function to fetch and print posts from the API'''
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        data = r.json()
        for element in data:
            print(element['title'])


def fetch_and_save_posts():
    '''function to fetch and save posts from the API to json and csv files'''
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        data = r.json()
        data_list = []
        for element in data:
            data_list.append(element)
        with open("posts.json", "w") as f:
            json.dump(data_list, f)
        with open("posts.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(data_list[0].keys())
            for element in data_list:
                writer.writerow(element.values())
