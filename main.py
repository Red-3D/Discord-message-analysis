import json
import glob
from matplotlib import pyplot as plt

user_ID = "3062"
display_name = "Red_3D"
path = "C:/.../"


files = glob.glob((path+"*.json"))
print(files)

output = []
for file in files:
    data = json.load(open(file, "r", encoding="utf8"))
    for message in data['messages']:
        if message['author']['discriminator'] == user_ID:
            output.append((message['timestamp'])[11:][:2] + '\n')

h = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
h_msg = []
count = 0

for x in h:
    for n in output:
        if(x == n.replace("\n","")):
            count += 1
    h_msg.append(count)
    count = 0

plt.bar(h, h_msg)
plt.title("Messages from " + display_name + " by hour")
plt.show()
