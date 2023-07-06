import csv
import pandas as pd
import os

def csvConv():
    with open('1759.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        with open('output1.csv', 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            row_one = 0
            for row in reader:
                row_one_diff = 0
                if row_one !=0:
                    row_one_diff = int(row[0]) - row_one
                diff = int(row[1]) - int(row[0])
                new_row = [row_one_diff] + [diff] + row[2:]
                writer.writerow(new_row)
                row_one = int(row[0])
def csvPog():
    with open('data/1727.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        with open('1759re.csv', 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            for row in reader:
                diff = int(row[3]) - 1
                new_row = row[:3] + [diff] + row[4:]
                writer.writerow(new_row)

def csvConv2():
    folder_path = 'data'

    for filename in os.listdir(folder_path):
        with open(f"{folder_path}/{filename}", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            with open('outputV3.csv', 'a', newline='') as outfile:
                writer = csv.writer(outfile)
                row_one = 0
                for row in reader:
                    row_one_diff = 0
                    if row_one !=0:
                        row_one_diff = int(row[0]) - row_one
                    diff = int(row[1]) - int(row[0])
                    new_row = [row_one_diff] + [diff] + row[2:]
                    writer.writerow(new_row)
                    row_one = int(row[0])

csvPog()