import csv
import json
import os
from os.path import join
scriptDirectory = os.path.dirname(os.path.abspath(__file__))

with open(join(scriptDirectory,'catCFDI2021.csv'), encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    line_count_mal = 0
    cat_conceptos = {}
    for row in csv_reader:
        cat_conceptos[row[0]] = row[1]
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            try:
                print(row[1])
                line_count += 1
            except:
                print("no pude -------------------------------------------------------------")
                line_count_mal += 1
    print(f'Processed {line_count} lines. Con  {line_count_mal} malas')

    print(cat_conceptos["10151523"])


    with open (join(scriptDirectory,"conceptos.json"), "w") as outfile:
        json.dump (cat_conceptos,outfile)
