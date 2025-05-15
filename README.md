# PyShell
A lightweight Python script that creates a reverse shell from a Windows machine to Kali Linux, allowing remote CMD command execution over the same network. For educational and authorized testing use only.
# 🔁 Windows CMD Remote Shell over Network (Python)

## 📌 Description

This project provides a lightweight Python script that creates a **reverse shell** from a Windows machine to a **Kali Linux controller**, allowing the Kali user to execute **CMD commands** remotely on the Windows machine. 

It mimics a basic command prompt (`cmd.exe`) interface, where the controller can:

- Send commands like `cd`, `dir`, `ipconfig`, `whoami`, etc.
- Get back the output in real-time
- See the current working directory as a command prompt

> ⚠️ **WARNING**: This script is for **educational purposes** and use in **authorized testing environments** (e.g. personal lab setups). Unauthorized access to systems is **illegal**.

---

## 🎯 Features

- CMD-like remote shell
- Support for directory navigation (`cd`)
- Real-time output of commands
- Displays current working directory as prompt
- Silent execution when compiled (`--noconsole`)

---

## 🖥️ Kali Listener Setup

On the **Kali Linux machine**, start a Netcat listener:

```bash
nc -lvnp 4445
