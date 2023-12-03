import subprocess

def read_syslog():
    syslog_data = subprocess.run(['cat', '/var/log/syslog'], capture_output=True, text=True)
    return syslog_data.stdout

def read_auth_logs():
    auth_data = subprocess.run(['cat', '/var/log/auth.log'], capture_output=True, text=True)
    return auth_data.stdout

def identify_login_logout_events(data):
    login_events = [line for line in data.split('\n') if 'login' in line or 'logout' in line]
    return login_events

def identify_failed_login_attempts(data):
    failed_login_attempts = [line for line in data.split('\n') if 'authentication failure' in line.lower()]
    return failed_login_attempts

def check_critical_events(data):
    critical_events = [line for line in data.split('\n') if 'system reboot' in line.lower() or 'service failure' in line.lower()]
    return critical_events


def read_syslog():
    syslog_path = '/var/log/syslog'
    try:
        with open(syslog_path, 'r') as syslog_file:
            syslog_data = syslog_file.read()
            return syslog_data
    except FileNotFoundError:
        print(f"Error: {syslog_path} not found.")
        return ""

def read_auth_logs():
    auth_path = '/var/log/auth.log'
    try:
        with open(auth_path, 'r') as auth_file:
            auth_data = auth_file.read()
            return auth_data
    except FileNotFoundError:
        print(f"Error: {auth_path} not found.")
        return ""
        
def audit():
    syslog = read_syslog()
    login_logout_events = identify_login_logout_events(syslog)
    failed_logins = identify_failed_login_attempts(syslog)
    critical_syslog_events = check_critical_events(syslog)


    auth_logs = read_auth_logs()
    failed_authentications = identify_failed_login_attempts(auth_logs)
    critical_auth_events = check_critical_events(auth_logs)


    print("\n\nLogin/Logout Events:")
    for event in login_logout_events:
        print(event)

    print("\n\nFailed Login Attempts:")
    for attempt in failed_logins:
        print(attempt)

    print("\n\nCritical Syslog Events:")
    for critical_event in critical_syslog_events:
        print(critical_event)

    print("\n\nFailed Authentications:")
    for failed_auth in failed_authentications:
        print(failed_auth)

    print("\n\nCritical Auth Events:")
    for critical_auth_event in critical_auth_events:
        print(critical_auth_event)
