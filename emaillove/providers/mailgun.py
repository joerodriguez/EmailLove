import requests
from requests.auth import HTTPBasicAuth

from emaillove.providers.base_provider import BaseProvider
from emaillove.exceptions import EmailLoveException


class MailGunInitFailed(EmailLoveException):
    pass


class MailGun(BaseProvider):
    def __init__(self, api_key, domain):
        self.api_key = api_key
        self.domain = domain

    def send(self, message):
        if self.api_key is None or self.domain is None:
            raise MailGunInitFailed("Fail to set mailgun env variables?")

        attachments = None
        if 'attachments' in message:
            files = () 
            for filename, data in message['attachments'].items():
                files += ((filename, data))
            attachments = {'attachment': files}

        payload = {
            'from': message['from'],
            'to': ','.join(message['to']),
            'subject': message['subject'],
            'text': message.get('text', ''),
            'html': message.get('html', ''),
        }
        url = "https://api.mailgun.net/v2/%s/messages" % self.domain
        r = requests.post(url, params=payload, files=attachments,
                          auth=HTTPBasicAuth('api', self.api_key))

        self.response = r.text
        if r.status_code == requests.codes.ok:
            if 'id' in r.text:
                return True
        return False
