import smtplib
import ssl
from email.message import EmailMessage
import requests

class SendMessage:
    def __init__(self, message_data):
        self.msg_data = message_data
        self.msg = ""
        self.SMTP_SERVER = "smtp.gmail.com"
        self.PORT = 465
        self.SENDER_EMAIL = "riyanirtaza@gmail.com"
        self.SENDER_PASSWORD = "ynes mowe lllo vxru"
        self.RECEIVER_EMAIL = "martinirtaza@gmail.com"
    
    def shape_msg(self):
         msg_data_list = self.msg_data

    def send_email(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.SMTP_SERVER, self.PORT, context=context) as server:
                server.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
                server.send_message(self.msg)

    def send_telegram_msg(message):
        TOKEN = "8790154670:AAFKoMjTHgopcns0CxdHwKByLSt1ht0GbjY"
        CHAT_ID = "7114121690"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        
        response = requests.post(url, data=payload)
        return response.json()
    
    def send_notification(self):
        try:
            self.send_telegram_msg(self.msg)
        except Exception as e:
            self.send_telegram_msg(e)
