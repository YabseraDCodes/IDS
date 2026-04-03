from datetime import datetime

def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            # Combine date + time
            time_str = parts[0] + " " + parts[1]
            timestamp = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            status = parts[2]
            ip = parts[3]

            log_entry = {
                "time": timestamp,
                "status": status,
                "ip": ip
            }

            logs.append(log_entry)
  
    return logs


# test it directly
if __name__ == "__main__":
    data = parse_logs("logs/auth.log")
    print(data)
    for entry in data:
        print("Entry type: ", type(entry))
        print(entry)
