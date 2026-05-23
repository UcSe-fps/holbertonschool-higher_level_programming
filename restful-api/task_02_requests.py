#!/usr/bin/python3
"""comment section"""
import csv
import requests
import json


def fetch_and_print_posts():
    """another comment section"""
    
    requ = requests.get("https://jsonplaceholder.typicode.com/posts")

    sc = requ.status_code
    r_json = requ.json()

    print(f"Status code: {sc}")

    for i in r_json:
        print(i['title'])


def fetch_and_save_posts():
    """another one"""

    requ = requests.get("https://jsonplaceholder.typicode.com/posts")
    sc = requ.status_code
    header = ('id', 'title', 'body')
    r_json = requ.json()

    if (sc == 200):
        with open ('posts.csv', "w") as f:
            write = csv.DictWriter(f, fieldnames=header)
            write.writeheader()

            for post in r_json:
                row= {}
                for field in header:
                    row[field] = post[field]
                writer.writerow(row)
