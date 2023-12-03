import psutil

def monitor_running_processes():
    print("\n\nRunning Processes:")
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        print(f"PID: {proc.info['pid']} - Name: {proc.info['name']}")

def detect_suspicious_processes():
    print("\n\nDetecting Suspicious Processes:")
    suspicious = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == "suspicious_process_name": #replace process name here.
            suspicious.append(proc.info['pid'])
    if suspicious:
        print(f"Suspicious Processes Found: {suspicious}")
    else:
        print("No suspicious processes detected.")

def analyze_resource_utilization():
    print("\n\nAnalyzing Resource Utilization:")
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_percent']):
        print(f"PID: {proc.info['pid']} - Name: {proc.info['name']} - CPU %: {proc.info['cpu_percent']} - Memory %: {proc.info['memory_percent']}")

def audit():
    monitor_running_processes()
    detect_suspicious_processes()
    analyze_resource_utilization()
