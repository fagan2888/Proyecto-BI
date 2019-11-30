import psycopg2
import os
import csv
from tqdm import tqdm
conn = psycopg2.connect("host=172.24.41.228 dbname=conectate user=isis password=conectate")
cur = conn.cursor()
# cur. execute('DROP TABLE RESPUESTAS')
# cur.execute('CREATE TABLE RESPUESTAS(ID SERIAL PRIMARY KEY, CRN text,CONSULTANT_ID text,RESPONDANT_ID text, CREATE_DATE text,MODIFIED_DATE text, DURACION integer , QUESTION text, ANSWER integer );')
# conn.commit()
f = os.path.join('.','qmerged.csv')
with open(f, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    numero = 0
    for row in tqdm(spamreader):
        if row[6]!='':
            insert_query = "INSERT INTO RESPUESTAS VALUES {}".format(f"({numero},'{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}',{row[5]},'{row[6]}',{row[7] if ''!=row[7] else 'NULL'})")
            cur.execute(insert_query)
            numero += 1

conn.commit()
resp = cur.execute('SELECT * FROM RESPUESTAS')
resp = cur.fetchall()
print(resp)