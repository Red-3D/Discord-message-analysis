import json

user_ID = "___Discord ID Here___"
files = [

    "___Channel 1 Here___",
    "___Channel 2 Here___ ...",
]

output = open("___file path for export here___", "w")

for datei in files:
    data = json.load(open(datei, "r", encoding="utf8"))
    for message in data['messages']:
        if message['author']['discriminator'] == user_ID:
            output.write(message['timestamp'] + '\n')

output.close()