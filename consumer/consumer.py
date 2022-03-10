import redis
import psycopg2
import os

name = os.getenv('HOSTNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

r = redis.Redis(host='redis', port=6379, decode_responses=True)

conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password=POSTGRES_PASSWORD)

cur = conn.cursor()

count = 0

while True:
    try:
        data = r.xreadgroup("groupname", name, streams={"mystream" : ">"}, count=1, block=0)
        print("Type ______________________________________ : ",type(data))
        exit("STOP!!" ,data)
        get = data[0][1][0][1]

        query = """ INSERT INTO public.users(user_id, first_name, last_name, email, gender, ip_address, user_name, agent, country)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        insert = (get['id'], get['first_name'], get['last_name'], get['email'], get['gender'], get['ip_address'], get['user_name'], get['agent'], get['country'])

        cur.execute(query, insert)
        conn.commit()

        count += 1
        print(count,"-",os.getenv('HOSTNAME'))
    except:
        print("EXCEPT!!!")
        exit()
        r.xgroup_create("mystream", "groupname", "$", mkstream=True)