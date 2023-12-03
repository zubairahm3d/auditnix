import subprocess
import os



def list_user_accounts():
    users = subprocess.check_output(['cut', '-d', ':', '-f1', '/etc/passwd']).decode().splitlines()
    return users


def check_password_strength():
    weak_passwords = []
    expired_passwords = []


    passwd_file = open('/etc/passwd', 'r')
    for line in passwd_file:
        user_info = line.split(':')
        username = user_info[0]
        passwd_info = user_info[1]
        if passwd_info in ['x', '*', '!', '!!']:
            weak_passwords.append(username)


    shadow_file = open('/etc/shadow', 'r')
    for line in shadow_file:
        user_info = line.split(':')
        username = user_info[0]
        passwd_info = user_info[1]
        if passwd_info in ['!', '*']:
            expired_passwords.append(username)

    return weak_passwords, expired_passwords


def list_sudo_users():
    sudo_users = subprocess.check_output(['getent', 'group', 'sudo']).decode().split(':')[3].split(',')
    return sudo_users


def review_account_history():
    creation_history = subprocess.check_output(['lastlog']).decode().splitlines()[1:]
    return creation_history




def audit():
    users = list_user_accounts()
    weak_passwords, expired_passwords = check_password_strength()
    sudo_users = list_sudo_users()
    creation_history = review_account_history()

    print("User Accounts:", users)
    print("\n\nUsers with Weak Passwords:", weak_passwords)
    print("\n\nUsers with Expired Passwords:", expired_passwords)
    print("\n\nUsers with sudo Privileges:", sudo_users)
    print("\n\nUser Account Creation/Deletion History:")
    for entry in creation_history:
        print(entry)
