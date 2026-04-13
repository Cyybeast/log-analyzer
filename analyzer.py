import sys

# Check if user provided a file
if len(sys.argv) < 2:
    print("Usage: python analyzer.py <logfile>")
    sys.exit()

log_file = sys.argv[1]

failed_logins = []
ip_count = {}

# Read log file
with open(log_file, "r") as file:
    logs = file.readlines()

# Find failed logins
for line in logs:
    if "Failed login" in line:
        failed_logins.append(line)

# Count IP attempts
for log in failed_logins:
    parts = log.split()
    ip = parts[-1]

    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

# Output results
print("\nSECURITY ALERT REPORT\n")

with open("report.txt", "w", encoding="utf-8") as report:
    report.write("SECURITY ALERT REPORT\n\n")

    for ip, count in ip_count.items():
        if count >= 3:
            message = f"HIGH ALERT: {ip} has {count} failed login attempts"
        elif count == 2:
            message = f"MEDIUM ALERT: {ip} has {count} failed login attempts"
        else:
            message = f"LOW ALERT: {ip} has {count} failed login attempt"

        print(message)
        report.write(message + "\n")