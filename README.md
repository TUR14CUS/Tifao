# Keylogger README

This repository contains a simple keylogger implemented in Python, consisting of three main files: `class.py`, `execute_report.py`, and `keylogger.py`. The keylogger is designed to capture keyboard inputs and periodically send the logged data via email.

## Files

### 1. `class.py`

This file defines the `Keylogger` class, responsible for capturing keyboard inputs, logging them, and periodically sending the log via email. Key features include:

- **Initialization**: Takes time interval, email, and password as parameters.

- **Callback Function**: `callback_function` is called when a key is pressed, and it appends the pressed key to the log.

- **Reporting**: The `report` function is called every 4 hours, sending the log content via email.

- **Sending Mail**: `send_mail` is responsible for sending emails using the SMTP protocol.

- **Start Function**: The `start` function initiates the keylogger by creating a listener thread and starting the reporting function.

### 2. `execute_report.py`

This file executes a system command to retrieve Wi-Fi network information and sends the result via email. Key features include:

- **Sending Mail**: The `send_mail` function is used to send emails with the retrieved network information.

- **Command Execution**: Uses the `subprocess` module to execute a command and capture the output.

### 3. `keylogger.py`

This script creates an instance of the `Keylogger` class and starts the keylogger.

## Usage

1. **Configure Credentials:**
   - Open `class.py` and `execute_report.py`.
   - Replace `"username"` and `"password"` in `Keylogger` initialization with your Gmail username and password.
   - In `execute_report.py`, replace `"email"` and `"password"` with your Gmail credentials.

2. **Run Keylogger:**
   - Execute `keylogger.py` to start the keylogger.

3. **Send Network Information Report:**
   - Optionally, execute `execute_report.py` to retrieve Wi-Fi network information and send it via email.

## Important Notes

- **Use Responsibly:** Please be aware of the legal and ethical implications of deploying a keylogger. Misuse of this software may violate privacy and legal regulations.

- **Security:** Storing email credentials in code poses security risks. Use secure methods for handling credentials in a production environment.

- **Disclaimer:** This keylogger is for educational purposes only. The author is not responsible for any misuse or damage caused by this software.

## Dependencies

- [pynput](https://pynput.readthedocs.io/en/latest/) for keyboard monitoring.
- [smtplib](https://docs.python.org/3/library/smtplib.html) for email functionality.
- [subprocess](https://docs.python.org/3/library/subprocess.html) for executing system commands.
