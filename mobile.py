import requests

SERVER_IP = "192.168.1.5"

url = f"https://{SERVER_IP}:5000/command"

command = input("Enter command (open/close): ")

data = {
    "key": "12345",
    "command": command
}

response = requests.post(
    url,
    json=data,
    verify=False
)

print(response.json())
