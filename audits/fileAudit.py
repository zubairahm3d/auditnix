import os
import subprocess

def scan_sensitive_files():
    sensitive_paths = ['/etc/shadow', '/etc/passwd', '/etc/sudoers']
    sensitive_files = [path for path in sensitive_paths if os.path.exists(path)]
    return sensitive_files

def detect_critical_file_changes():
    critical_files = ['/etc/passwd', '/etc/shadow']
    changed_files = []
    for file_path in critical_files:
        try:
            stat_info = os.stat(file_path)
            
            known_time = 1640995200  #replace timestamp later
            if stat_info.st_mtime > known_time:
                changed_files.append(file_path)
        except FileNotFoundError:
            pass
    return changed_files

def find_setuid_files(start_path='/'):
    setuid_files = []

    for dirpath, _, filenames in os.walk(start_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                mode = os.stat(file_path).st_mode
                if mode & 0o4000:  #check if setuid bit is set
                    setuid_files.append(file_path)
            except (OSError, PermissionError):
                pass

    return setuid_files

def audit():
    print("\n\nScanning for sensitive files:")
    print(scan_sensitive_files())

    print("\n\nDetecting changes to critical system files:")
    print(detect_critical_file_changes())

    print("\n\nSearching for files with setuid bit...")
    setuid_files = find_setuid_files('/')
    
    if setuid_files:
        print("Setuid files found:")
        for file in setuid_files:
            print(file)
    else:
        print("No files with setuid bit found.")