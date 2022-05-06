import csv
import json
import os, sys
 
 
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    csvfile = open(csvFilePath, 'r', encoding='utf-8')
    jsonfile = open(jsonFilePath, 'w', encoding='utf-8')

    fieldnames = ('TLX','TLY','BLX','BLY','BRX','BRY','TRX','TRY','content','p','as_cat','chunk','cat')

    reader = csv.DictReader(csvfile, fieldnames)
    out = json.dumps([row for row in reader])

    jsonfile.write(out)


def make_csv(jsonFilePath, csvFilePath):
    with open(jsonFilePath) as json_file:
        data = json.load(json_file)
    
    json_data = data['json']

    # now we will open a file for writing
    data_file = open(csvFilePath, 'w', newline='')

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for row in json_data:
        if count == 0:
            # Writing headers of CSV file
            header = row.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        else:
            csv_writer.writerow(row.values())   

    data_file.close()


def csv_to_dict_opt_only(csvFilePath):
    absPath = os.path.abspath(sys.argv[0])
    
    print('='*20,absPath[:-9])
    pwd = 'C:\\Users\\Tier1_Assassin\\Desktop\\CSDS395-Team-1\\back\\backend\\'
    reader = csv.DictReader(open(pwd + csvFilePath))
    result = {'ATT':[], 'CON':[]}
    for row in reader:
        result['ATT'].append(row['ATT'])
        result['CON'].append(row['CON'])

    return result