import redis
import psycopg2
import os

POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

r = redis.Redis(host='redis', port=6379, decode_responses=True)

conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="pg1234")

cur = conn.cursor()



lastSeenMessage = "0-0"
rowcount = 0


while True:

    data = r.xread({"mystream":lastSeenMessage}, None, 0)
    get = data[0][1][0][1] 

    query = """ INSERT INTO public.users(user_id, first_name, last_name, email, gender, ip_address, user_name, agent, country)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    insert = (get['id'], get['first_name'], get['last_name'], get['email'], get['gender'], get['ip_address'], get['user_name'], get['agent'], get['country'])

    cur.execute(query, insert)


    conn.commit()
    rowcount += 1
    print(rowcount, "Record inserted successfully into users table")


    lastSeenMessage = data[0][1][0][0]
