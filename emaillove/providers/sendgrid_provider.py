import sendgrid
import requests
import simplejson as json
from time import gmtime, strftime

from emaillove.providers.base_provider import BaseProvider
from emaillove.exceptions import EmailLoveException


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

    def unsubscribes(self, start_date=None, end_date=None):
        if not end_date and start_date:
            end_date = strftime("%Y-%m-%d", gmtime())
        args = ['api_user=%s' % self.username, 'api_key=%s' % self.password,
                'date=1']
        if start_date:
            args.append('start_date=%s' % start_date)
            args.append('end_date=%s' % end_date)
        url = ("https://sendgrid.com/api/unsubscribes.get.json?%s" % 
               '&'.join(args))

        r = requests.get(url)
        r.response = r.text

        if r.status_code == requests.codes.ok:
            return json.loads(r.text)
        return None
