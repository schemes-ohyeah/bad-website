import requests
from secret import MG_API_KEY


class Mailgun:
    @staticmethod
    def send(self, sender, receiver, subject, message):
        return requests.post(
            "https://api.mailgun.net/v3/schemes.me/messages",
            auth=("api", MG_API_KEY),
            data={
                "from": sender,
                "to": receiver,
                "subject": subject,
                "text": message
            }
        )