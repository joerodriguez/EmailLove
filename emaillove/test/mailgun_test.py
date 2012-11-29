import os
import unittest

from emaillove import EmailLove
from emaillove.providers.mailgun import MailGun 


class TestMailGun(unittest.TestCase):
    def setUp(self):
        self.email_lover = EmailLove()
        mailgun = MailGun(api_key=os.environ.get('MAILGUN_APIKEY'),
                          domain=os.environ.get('MAILGUN_DOMAIN'))
        self.email_lover.providers.append(mailgun)

        self.from_email = os.environ.get('EMAILLOVE_FROM')
        self.to_email = os.environ.get('EMAILLOVE_TO')
        if self.to_email is None or self.from_email is None:
            raise RuntimeError("Please set from/to env variables")

        self.subject = "EmailLove Mailgun Test"

    def test_send_html(self):
        result = self.email_lover.send({
            'subject': self.subject,
            'from': self.from_email, 
            'to': [self.to_email],
            'text': 'EmailLove mailgun text message',
            'html': '<b>EmailLove</b> mailgun html <em>message</em>',
        })
        self.assertTrue(result)

    def test_send_text(self):
        result = self.email_lover.send({
            'subject': self.subject,
            'from': self.from_email, 
            'to': [self.to_email],
            'text': 'EmailLove mailgun text message',
        })
        self.assertTrue(result)

    def test_send_attachment(self):
        f = open("/tmp/testdoc.txt", "w+")
        f.write("This is a test document for emaillove.")
        f.close()

        result = self.email_lover.send({
            'subject': self.subject,
            'from': self.from_email, 
            'to': [self.to_email],
            'text': 'EmailLove mailgun text message',
            'html': '<b>EmailLove</b> mailgun attachment <em>message</em>',
            'attachments':{
                'testdoc.txt': open('/tmp/testdoc.txt', 'rb')
            }
        })
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
