import csv
import json
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    csvfile = open(csvFilePath, 'r', encoding='utf-8')
    jsonfile = open(jsonFilePath, 'w', encoding='utf-8')

    fieldnames = ('TLX','TLY','BLX','BLY','BRX','BRY','TRX','TRY','content','p','as_cat','chunk','cat')

    reader = csv.DictReader(csvfile, fieldnames)
    out = json.dumps([row for row in reader])

    jsonfile.write(out)