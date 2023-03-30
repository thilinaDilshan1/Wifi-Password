import subprocess

def get_wifi_profiles():
    meta_data = subprocess.check_output(['netsh','wlan','show','profiles'])
    data = meta_data.decode("utf-8")
    data = data.split("\n")
    names=[]
    for line in data:
        if "All User Profile     : " in line:
            name = line.split(":")[1]
            names.append(name[1:-1])
    return names

for name in get_wifi_profiles():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile',name,'key=clear'])
    data = meta_data.decode("utf-8",errors="backslashreplace")
    data = data.split("\n")
    names = []
    for line in data:
        if "Key Content" in line:
            password = line.split(":")[1]
            print(name," : ",password)