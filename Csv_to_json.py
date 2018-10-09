import csv
import json


csvfile = open('analysis_senti.csv', 'r')
jsonfile = open('analysis.json', 'w')

fieldNames = ("Tweet","Sentiment","Score")
reader = csv.DictReader(csvfile,fieldNames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')