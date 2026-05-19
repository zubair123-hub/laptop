import requests

IP = "192.168.1.5"
PASSWORD = "12345"

while True:

    cmd = input(
        "Enter command (open/close/restart): "
    )

    try:

        r = requests.post(
            f"http://{IP}:5000/cmd",
            data={
                "password": PASSWORD,
                "command": cmd
            }
        )

        print(r.json())

    except Exception as e:
        print("Error:", e)
