import subprocess

meta_data = subprocess.check_output(['netsh','wlan','show','profiles'])
data = meta_data.decode("utf-8")
data = data.split("\n")
names=[]
for line in data:
    if "All User Profile    : " in line:
        name = line.split(":")[1]
        names.append(name[1:-1])