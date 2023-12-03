import subprocess

def check_available_updates():
    try:
        updates = subprocess.run(['sudo', 'apt', 'list', '--upgradable'], capture_output=True, text=True)
        print("\n\nAvailable system updates:")
        print(updates.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error checking for updates: {e}")



def audit():
    check_available_updates()
   
