# The script checks your computer's CPU, memory, and disk usage, and logs it to a file.
#  If any usage is too high, it adds a warning.

import psutil         # lets us check cpu, memory , and disk
from datetime import datetime  # giver us current date and time

# setting threshold

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

#  We’re setting warning limits here.
# If any of these values exceed the threshold, we’ll add a warning to the log file.

# Get system stats
cpu = psutil.cpu_percent(interval=1)   # interval 1 waits for 1 sec to get the data 
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

#These lines get the current usage:
# cpu: current CPU usage (%)
# memory: current RAM usage (%)

# disk: how full your C: drive (or / on Linux) is (%)

# Timestamp
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log message
log = f"[{now}] CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"

# Check thresholds
if cpu > CPU_THRESHOLD or memory > MEMORY_THRESHOLD or disk > DISK_THRESHOLD:
    log += " ⚠️ WARNING: High usage!"

# Write to log file
with open("health_log.txt", "a") as f:
    f.write(log + "\n")                        # This saves the message into a file called health_log.txt.

                                                 #    The "a" means append (don’t erase old logs).

print(log)
