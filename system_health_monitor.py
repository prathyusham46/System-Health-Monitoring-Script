import psutil
import time
import logging

# Setup logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU Usage: {cpu_usage}%")
    else:
        logging.info(f"CPU Usage: {cpu_usage}%")
    return cpu_usage

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory Usage: {memory_usage}%")
    else:
        logging.info(f"Memory Usage: {memory_usage}%")
    return memory_usage

def check_disk():
    disk = psutil.disk_usage("/")
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk Usage: {disk_usage}%")
    else:
        logging.info(f"Disk Usage: {disk_usage}%")
    return disk_usage

def check_processes():
    processes = len(psutil.pids())
    logging.info(f"Running Processes: {processes}")
    return processes

def system_health_monitor():
    while True:
        print("Monitoring system health...")
        cpu = check_cpu()
        memory = check_memory()
        disk = check_disk()
        processes = check_processes()

        print(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {processes}")
        print("Alerts are logged in 'system_health.log'")
        
        time.sleep(5)  # Monitor every 5 seconds

if __name__ == "__main__":
    system_health_monitor()
