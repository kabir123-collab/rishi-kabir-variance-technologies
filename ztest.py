

# import json
# import pandas as pd
# import requests
# import threading


# df = pd.read_csv("testing.csv")
# done_usernames  = []
# def main(st, en):
#     for i in range(st, en):
#         row = df.iloc[i]
#         url = "http://143.110.251.143/subscriber/subscribe"
#         # url = "http://143.110.251.143/subscriber/unsubscribe"

#         if row["tv_id"] in done_usernames:
#             continue

#         data = { 
#                 "fullname": row["fullname"], 
#                 "user_email": row["email"],
#                 "user_phone": str(row["phone"]),
#                 "username": row["tv_id"], 
#                 "strategy_name": "testing", 
#                 "duration": "10D",
#                 "admin_token": "3bea7648-1529-499b-b13c-faf0522a3f88" }
#         resp = requests.post(url=url, json=data)
#         print(resp.text)
#         done_usernames.append(row["tv_id"])
#         # break


# thread1 = threading.Thread(target=main, args=(0,5), name="thread1")
# thread2 = threading.Thread(target=main, args=(5,10), name="thread2")
# thread3 = threading.Thread(target=main, args=(10,15), name="thread3")
# thread4 = threading.Thread(target=main, args=(15,20), name="thread4")
# thread5 = threading.Thread(target=main, args=(20,25), name="thread5")

# thread1.start()
# thread5.start()
# thread2.start()
# thread3.start()
# thread4.start()



# """
# Timestamp,fullname,phone,email,tv_id
# 29/08/2024 11:09:14,Harjit Hundal,7896541230,singhundal91@gmail.com,harjit91
# 29/08/2024 11:07:10,Hasneet kohli,9910254680,Hasneetkohli@gmail.com,hasneetkohli
# 29/08/2024 11:07:20,Ashutosh Honrao,8080735034,ashutoshhonrao7903@gmail.com,Ashutoshscalp4323
# 29/08/2024 11:07:46,Parth Doshi,9769293340,parthd93@gmail.com,Parthd93
# 29/08/2024 11:07:49,Madan Mohan ,8908128540,madanmohansenapati90@gmail.com,madanmohansenapati90
# """

# import requests
# url = "https://api.zeptomail.in/v1.1/email/template"

# payload = '''
# {\n\"mail_template_key\":\"2518b.3f7383f614a9277.k1.da22b321-68f8-11ef-84cb-525400674725.191b187bf50\",
# \n\"from\": { \"address\": \"noreply@financetalkwithrishabh.com\", \"name\": \"noreply\"},
# \n\"to\": [{\"email_address\": {\"address\": \"mbilalsheikh2001@gmail.com\",\"name\": \"Rishabh\"}}],
# \n\"merge_info\": {"expiration":"expiration_value","fullname":"fullname_value","username":"username_value"}
# }'''

# headers = {
# 'accept': "application/json",
# 'content-type': "application/json",
# 'authorization': "Zoho-enczapikey PHtE6r0NSuju2DQs8xEF4vHpH8PyPI0pq+JlLQZBuIpAAvNQS01Woo8ilzWxrx4uU6VFEvKend065OnN5r+Ed27tY2lNX2qyqK3sx/VYSPOZsbq6x00fuV0ZcEHVUILue9Bp0ifSvdnaNA==",
# }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)

from datetime import datetime
import json
import os
import pytz
import requests
from server.support.discord import DiscordAlert
from pymongo import MongoClient

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NzlhNWJjOTUyOWUzM2NhMDEyOGU3NTMiLCJhdWQiOlsiZmFzdGFwaS11c2VyczphdXRoIl0sImV4cCI6MTczODgxOTgxOH0.y2Xo2iNtAoQTkuwewGs9CPZ3mwQhQr1y3q37P9eSF34"
a = DiscordAlert()
webhookurl = "https://discord.com/api/webhooks/1336560666248745000/zrarOHGIQdlcr8F0a0qYka4M7lTUjvXqXo1eYH1xUc0WQPNtkfJ-frHHRSz261VuxSe6"

with open("credentials.json", "r") as f:
    credentials = json.load(f)
    f.close()

url = f"mongodb://{credentials['db_username']}{':' if len(credentials['db_username']) != 0 else ''}{credentials['db_password']}{'@' if len(credentials['db_username']) != 0 else ''}{credentials['host_ip']}:27017/{credentials['database']}"
client = MongoClient(url)[credentials['database']]

subscribers = list(client["SUBSCRIBERS"].find({}, {"_id": False}))

to_update = []
for i in subscribers:
    success_data = client["SUCCESS"].find_one({"subid": i["subid"]}, {"_id": 0})
    if success_data is None:
        print("no success", i["username"])
        continue
    now_timestamp = datetime.now(tz=pytz.timezone("UTC")).timestamp()
    days_to_expire = success_data["expiration_timestamp"] - now_timestamp
    # print(success_data["expiration_timestamp"]/86400, now_timestamp/86400)
    if (int(days_to_expire/86400) >= 0 and int(days_to_expire/86400) <= 2) or (int(days_to_expire/86400) > -3):
        i["days_to_expire"] = int(days_to_expire / 86400)
        to_update.append(i)
        print(i["username"], i["days_to_expire"])
    
print(len(to_update))
with open(os.path.join("data", "extra.json"), "w") as f:
    json.dump(to_update, f)
    f.close()

with open(os.path.join("data", "extra.json"),"rb") as f:
    file_name = "extra.json"
    a.send_file(webhook_url=webhookurl, file_to_send=f, file_name=file_name)
    f.close()