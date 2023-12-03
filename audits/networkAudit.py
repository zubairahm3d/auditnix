import socket
import subprocess
import os


def check_open_ports():
    open_ports = []
    for port in range(1, 1025):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                result = sock.connect_ex(('127.0.0.1', port))
                if result == 0:
                    open_ports.append(port)
        except socket.error:
            pass
    return open_ports


def detect_unauthorized_connections():
    unauthorized_connections = []
    try:
        output = subprocess.check_output(['netstat', '-tuln'])
        output = output.decode('utf-8').split('\n')
        for line in output[2:]:
            if line.strip():
                parts = line.split()
                if parts[0] not in ['tcp', 'udp']:
                    unauthorized_connections.append(line)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    return unauthorized_connections


def monitor_firewall_rules():
    try:
        output = subprocess.check_output(['iptables', '-L'])
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

def audit():
    print("\n\nChecking open ports...")
    open_ports = check_open_ports()
    if open_ports:
        print("Open ports found:", open_ports)
    else:
        print("No open ports found.")

    print("\n\nDetecting unauthorized connections...")
    unauthorized_connections = detect_unauthorized_connections()
    if unauthorized_connections:
        print("Unauthorized connections found:")
        for conn in unauthorized_connections:
            print(conn)
    else:
        print("No unauthorized connections found.")

    print("\n\nMonitoring firewall rules and configurations...")
    firewall_rules = monitor_firewall_rules()
    if firewall_rules:
        print("Firewall rules:\n", firewall_rules)
    else:
        print("Failed to fetch firewall rules.")
