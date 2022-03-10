from flask import Flask
from flask import request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def main():
    return "Home"

@app.route("/", methods=["POST"])
def json_handler():
    while True:
        item_count = 0
        json_data = request.json
        if isinstance(json_data, dict):
            send_redis(json_data)

            item_count += 1
            return str(item_count)

        elif isinstance(json_data, list):
            for item in json_data:
                
                item_count += 1
                send_redis(item)
            
            return str(item_count)
        else:
            print("Yanlis JSON!")


def send_redis(json_data):

    result = r.xadd("mystream", json_data)
    print(result)
    return result

