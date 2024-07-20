import subprocess

def get_wifi_profiles():
    # Run the command to get profiles
    command = "netsh wlan show profiles"
    networks = subprocess.check_output(command, shell=True).decode('utf-8').split('\n')

    profiles = []
    for line in networks:
        if "All User Profile" in line:
            # Extract the profile name
            profile = line.split(":")[1].strip()
            profiles.append(profile)
    return profiles

def get_wifi_password(profile):
    # Run the command to get profile details
    command = f'netsh wlan show profile name="{profile}" key=clear'
    result = subprocess.check_output(command, shell=True).decode('utf-8').split('\n')

    password = None
    for line in result:
        if "Key Content" in line:
            # Extract the password
            password = line.split(":")[1].strip()
            break
    return password

def main():
    profiles = get_wifi_profiles()
    for profile in profiles:
        password = get_wifi_password(profile)
        if password:
            print(f'Profile: {profile}\nPassword: {password}\n')
        else:
            print(f'Profile: {profile}\nPassword: Not found\n')

if __name__ == "__main__":
    main()
