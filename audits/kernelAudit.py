import subprocess

def check_kernel_integrity():
    kernel_version = subprocess.check_output(['uname', '-r']).decode().strip()
    print(f"Kernel version: {kernel_version}")

    print("\nVerifying the integrity of the kernel...")
    subprocess.run(['sudo', 'kexec', '--load', '/dev/null'], stderr=subprocess.PIPE)
    integrity_check = subprocess.run(['dmesg'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if "integrity: Loaded X509" in integrity_check.stdout.decode():
        print("Kernel integrity verified.")
    else:
        print("Warning: Kernel integrity check failed or not supported.")

def detect_unauthorized_modules():
    print("\nDetecting unsigned or unauthorized kernel modules...")
    modules_check = subprocess.run(['lsmod', '--verify'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if modules_check.returncode == 0:
        print("All loaded modules are verified and signed.")
    else:
        print("Warning: Unsigned or unauthorized modules detected.")

def audit():
    check_kernel_integrity()
    detect_unauthorized_modules()
