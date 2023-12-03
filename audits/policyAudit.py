import subprocess

def check_selinux_status():
    print("\n\nChecking SELinux status...")
    selinux_status = subprocess.run(['sestatus'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if selinux_status.returncode == 0:
        print(selinux_status.stdout.decode())
    else:
        print("SELinux is either not installed or not enabled.")

def check_apparmor_status():
    print("\n\nChecking AppArmor status...")
    apparmor_status = subprocess.run(['apparmor_status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if apparmor_status.returncode == 0:
        print(apparmor_status.stdout.decode())
    else:
        print("AppArmor is either not installed or not enabled.")

def review_system_hardening():
    print("\n\nReviewing system hardening measures...")
    firewall_status = subprocess.run(['sudo', 'iptables', '-L'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Firewall Status:")
    print(firewall_status.stdout.decode())

def audit():
    check_selinux_status()
    check_apparmor_status()
    review_system_hardening()
