#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file.
    """
    try:
        data_list = []
        # 1. Open the CSV file for reading
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            # Use DictReader to turn each row into a dictionary
            data_reader = csv.DictReader(csv_f) # Fixed: changed csv.f to csv_f
            for row in data_reader:
                data_list.append(row) # Fixed: consistent naming

        # 2. Write the list of dictionaries to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_f: # Fixed: added .json
            json.dump(data_list, json_f, indent=4)

        return True

    except (FileNotFoundError, Exception):
        return False
