import subprocess

def enforce_password_policies(username):
    print("\n\nEnforcing password policies...")
    #subprocess.run(['sudo', 'passwd', '-l', username], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def check_password_complexity():
    print("\n\nChecking password complexity...")
    pwquality_conf = subprocess.run(['sudo', 'cat', '/etc/security/pwquality.conf'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if pwquality_conf.returncode == 0:
        print("Password complexity settings:")
        print(pwquality_conf.stdout.decode())
    else:
        print("Error occurred while checking password complexity settings.")

def check_password_expiration(username):
    print("\n\nChecking password expiration...")
    chage_output = subprocess.run(['sudo', 'chage', '-l', username], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if chage_output.returncode == 0:
        print("Password expiration settings:")
        print(chage_output.stdout.decode())
    else:
        print("Error occurred while checking password expiration settings.")

def audit_password_history_reuse():
    print("\n\nAuditing password history and reuse...")
    passwd_history_file = '/etc/security/opasswd'
    try:
        with open(passwd_history_file, 'r') as file:
            history = file.read()
            print("Password history:")
            print(history)
    except FileNotFoundError:
        print(f"Password history file '{passwd_history_file}' not found.")

def audit(username):
    enforce_password_policies(username)
    check_password_complexity()
    check_password_expiration(username)
    audit_password_history_reuse()
