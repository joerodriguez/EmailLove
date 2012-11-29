
from emaillove.providers.base_provider import BaseProvider
from emaillove.exceptions import EmailLoveException
import sendgrid


class SendGridInitFailed(EmailLoveException):
    pass


class SendGrid(BaseProvider):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send(self, message):
        if self.username is None or self.password is None:
            raise SendGridInitFailed("Fail to set sendgrid env variables?")

        s = sendgrid.Sendgrid(self.username, self.password, secure=True)
        sendgrid_message = sendgrid.Message(
            message['from'],
            message['subject'],
            message.get('text', ''),
            message.get('html', '')
        )

        for to in message['to']:
            sendgrid_message.add_to(to[0], to[1])

        if 'attachments' in message:
            for filename, file_on_disk in message['attachments'].items():
                sendgrid_message.add_attachment(filename, file_on_disk)

        ## smtp doesn't send attachments correctly but web wont send cc
        return s.web.send(sendgrid_message)
