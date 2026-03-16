import smtplib
import ssl
from email.message import EmailMessage
import requests

class SendMessage:
    SMTP_SERVER = "smtp.gmail.com"
    PORT = 465
    SENDER_EMAIL = "riyanirtaza@gmail.com"
    SENDER_PASSWORD = "ynes mowe lllo vxru"
    RECEIVER_EMAIL = "martinirtaza@gmail.com"
    
    @staticmethod
    def shape_msg(message_data, link):
        title = message_data.get("job_title", "No Title")
        desc = message_data.get("description", "No Description")[:500] + "..."
        proposals = message_data.get("no_of_proposals", "N/A")

        return (
            f"🚀 New Job Found!\n\n"
            f"Title: {title}\n"
            f"Proposals: {proposals}\n\n"
            f"Description:\n{desc}"
            f"Link:{link}"
        )

    @staticmethod
    def send_email(message_data, body):
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = f"New Job: {message_data.get('job_title', 'Update')}"
        msg['From'] = SendMessage.SENDER_EMAIL
        msg['To'] = SendMessage.RECEIVER_EMAIL

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SendMessage.SMTP_SERVER, SendMessage.PORT, context=context) as server:
            server.login(SendMessage.SENDER_EMAIL, SendMessage.SENDER_PASSWORD)
            server.send_message(msg)

    @staticmethod
    def send_telegram_msg(message):
        TOKEN = "8790154670:AAFKoMjTHgopcns0CxdHwKByLSt1ht0GbjY"
        CHAT_ID = "7114121690"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
        return requests.post(url, data=payload).json()
    
    @staticmethod
    def send_notification(message_data, link):
        formatted_text = SendMessage.shape_msg(message_data, link)
        try:
            SendMessage.send_email(message_data, formatted_text)
        except Exception as e:
            SendMessage.send_email({'job_title': "error"}, e)



SendMessage.send_email({'job_title': "test"}, "Hello")