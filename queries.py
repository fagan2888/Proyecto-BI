import psycopg2

conn = psycopg2.connect("host=172.24.41.228 dbname=conectate user=isis password=conectate")
cur = conn.cursor()

resp = cur.execute("SELECT * FROM RESPUESTAS WHERE CRN='CRN-16836'")
resp = cur.fetchall()
print(resp)