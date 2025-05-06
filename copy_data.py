import os
from server.support.discord import DiscordAlert
from pymongo import MongoClient
import json
import time

with open("credentials.json", "r") as f:
    credentials = json.load(f)
    f.close()

url = f"mongodb://{credentials['db_username']}{':' if len(credentials['db_username']) != 0 else ''}{credentials['db_password']}{'@' if len(credentials['db_username']) != 0 else ''}{credentials['host_ip']}:27017/{credentials['database']}"
client = MongoClient(url)[credentials['database']]
# print(client.list_collection_names())
# print(list(client["SUBSCRIBERS"].find({}, {"_id": False})))
# print(client["SUBSCRIBERS"].count_documents({}))
# exit()
a = DiscordAlert()
webhook_url = "https://discord.com/api/webhooks/1336560666248745000/zrarOHGIQdlcr8F0a0qYka4M7lTUjvXqXo1eYH1xUc0WQPNtkfJ-frHHRSz261VuxSe6"

files = {
    "SUBSCRIBERS": "SUBSCRIBERS.json",
    "PAYMENT": "PAYMENT.json",
    "SUCCESS": "SUCCESS.json",
    "FAILED": "FAILED.json"
}

os.makedirs("data", exist_ok=True)

for coll, file in files.items():
    data = list(client[coll].find({}, {"_id": False}))
    print(len(data))
    with open(os.path.join("data", file), "w") as f:
        json.dump(data, f)
        f.close()
        time.sleep(len(data)/2)

    with open(os.path.join("data", file),"rb") as f:
        file_name = file
        a.send_file(webhook_url=webhook_url, file_to_send=f, file_name=file_name)
        f.close()
    time.sleep(2)





# NOTE Send file to discord channel using thread
