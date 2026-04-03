from parser import parse_logs

sus_ip = {}

data = parse_logs("logs/auth.log")


for entry in data:
    if entry["status"] == "FAIL":
        x = entry["ip"]
        if x in sus_ip:
            if sus_ip[x] >= 4:
                print("Intrustion being performed")
            else:
                print(sus_ip[x])
                sus_ip[x] = sus_ip[x] + 1
        else:
            sus_ip[x] = 1
            print("Nothing weird so far")