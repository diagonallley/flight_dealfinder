from twilio.rest import Client
import smtplib
TWILIO_SID = ""
TWILIO_AUTH = ""
TWILIO_VIRTUAL_NUMBER = ""
TWILIo_VERIFIED_NUMBER = ""


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.client = Client(TWILIO_SID, TWILIO_AUTH)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message, from_=TWILIO_VIRTUAL_NUMBER, to=TWILIo_VERIFIED_NUMBER)

        print(message.sid)

    def send_mail(self, email_id, message):
        user = ""
        pwd = ""
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=user, password=pwd)
            connection.sendmail(
                from_addr=user, to_addrs=email_id, msg=message)
