failed_logins = []
ip_count = {}

with open("sample.log", "r") as file:
    logs = file.readlines()

for line in logs:
    if "Failed login" in line:
        failed_logins.append(line)

for log in failed_logins:
    parts = log.split()
    ip = parts[-1]

    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

print("Failed Logins:")
for log in failed_logins:
    print(log)

print("\nSuspicious IPs:")
for ip, count in ip_count.items():
    if count > 2:
        print(f"{ip} has {count} failed attempts")