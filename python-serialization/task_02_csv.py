#!/usr/bin/python3
import csv
import json


def convert_csv_to_json:
    """
    Reads data from a CSV file and converts it into a JSON file.

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        

        data_csv = []
        # 1. Open the CSV file for reading
        with open(csv_filename, mode ='r', encoding='utf-8') as csv_f:
            # Use DictReader to turn each row into a dictionary automatically
            data_reader = csv.DictReader(csv.f)
            for row in data_reader:
                data.append(row)

         # Write the list of dictionaries to data.json       
        with open('data_json', mode = 'w', encoding='utf-8') as json_f:
            json.dump(data, json_f, indent = 4)

        return True


    except (FileNotFoundError, Exception):
        # Return False if the file doesn't exist or any other error occurs
        return False
        
