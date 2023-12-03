import subprocess
import os

def track_user_logins_logouts():
    print("\nTracking user logins and logouts...")
    last_logins = subprocess.run(['last', '-i'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if last_logins.returncode == 0:
        print("User login/logout history:")
        print(last_logins.stdout.decode())
    else:
        print("Error occurred while tracking user logins and logouts.")

def record_user_command_execution():
    print("\nRecording user command execution (auditd required)...")
    if os.path.exists('/var/log/audit/audit.log'):
        audit_log = subprocess.run(['sudo', 'ausearch', '-i', '-k', 'cmd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if audit_log.returncode == 0:
            print("Recent user command execution:")
            print(audit_log.stdout.decode())
        else:
            print("Error occurred while recording user command execution.")
    else:
        print("Audit logs not found. Please ensure auditd is installed and configured.")

def review_user_shell_history():
    print("\nReviewing user shell history files...")
    users = subprocess.run(['ls', '/home'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if users.returncode == 0:
        users_list = users.stdout.decode().split()
        for user in users_list:
            history_file = f"/home/{user}/.bash_history"
            if os.path.exists(history_file):
                print(f"User: {user}")
                with open(history_file, 'r') as file:
                    history = file.read()
                    print(history)
            else:
                print(f"No shell history found for user: {user}")
    else:
        print("Error occurred while reviewing user shell history.")

def audit():
    track_user_logins_logouts()
    record_user_command_execution()
    review_user_shell_history()
