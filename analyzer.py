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

print("\n===== SOC SUMMARY =====")

total_failed = len(failed_logins)
print(f"Total Failed Logins: {total_failed}")

print("\nTop Attacker IP:")

top_ip = max(ip_count, key=ip_count.get)
print(f"{top_ip} ({ip_count[top_ip]} attempts)")

high = sum(1 for c in ip_count.values() if c >= 3)
medium = sum(1 for c in ip_count.values() if c == 2)
low = sum(1 for c in ip_count.values() if c == 1)

print("\nAlert Breakdown:")
print(f"High Risk IPs: {high}")
print(f"Medium Risk IPs: {medium}")
print(f"Low Risk IPs: {low}")

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