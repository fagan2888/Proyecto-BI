import glob
import pandas as pd
import os
import time
import csv
import pdb

path = os.path.join('.','Data','EncuestasCCA-2018')

files = [f for f in glob.glob(os.path.join(path, "*.csv"), recursive=True)]

baseDF = pd.DataFrame()
firstRow=['respondent_id','collector_id','date_created','date_modified','question','answer']
for f in files:
    num=0
    questions=[]
    rows=[]
    with open(f, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            newRow=[]
            num+=1
            if num == 6:
                questions=row
            if num>6:
                numero=11
                while numero<len(questions):
                    newRow=[]
                    newRow.append(row[0])
                    newRow.append(row[1])
                    newRow.append(row[2])
                    newRow.append(row[3])
                    newRow.append(questions[numero])
                    newRow.append(row[numero])
                    rows.append(newRow)
                    numero+=1
    with open(f.replace('EncuestasCCA-2018','EncuestasFormateadas'), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            spamwriter.writerow(row)
            