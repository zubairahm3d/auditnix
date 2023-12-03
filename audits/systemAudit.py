import subprocess

def monitor_resource_usage():
    print("\nMonitoring CPU usage...")
    cpu_usage = subprocess.run(['top', '-n', '1', '-b'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if cpu_usage.returncode == 0:
        print("CPU Usage:")
        print(cpu_usage.stdout.decode())
    else:
        print("Error occurred while monitoring CPU usage.")

    print("\nMonitoring Memory usage...")
    memory_usage = subprocess.run(['free', '-m'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if memory_usage.returncode == 0:
        print("Memory Usage:")
        print(memory_usage.stdout.decode())
    else:
        print("Error occurred while monitoring Memory usage.")

    print("\nMonitoring Disk usage...")
    disk_usage = subprocess.run(['df', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if disk_usage.returncode == 0:
        print("Disk Usage:")
        print(disk_usage.stdout.decode())
    else:
        print("Error occurred while monitoring Disk usage.")

def identify_resource_bottlenecks():
    print("\nIdentifying resource bottlenecks...")
    ps_output = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if ps_output.returncode == 0:
        print("Process Status (PS):")
        print(ps_output.stdout.decode())
    else:
        print("Error occurred while identifying resource bottlenecks.")

def setup_resource_exhaustion_alerts():
    print("\nSetting up alerts for resource exhaustion...")

def audit():
    monitor_resource_usage()
    identify_resource_bottlenecks()
    setup_resource_exhaustion_alerts()
