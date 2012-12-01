import os
import unittest

from emaillove import EmailLove
from emaillove.providers.sendgrid_provider import SendGrid


class TestSendGrid(unittest.TestCase):
    def setUp(self):
        self.email_lover = EmailLove()
        sendgrid = SendGrid(username=os.environ.get('SENDGRID_USER'),
                            password=os.environ.get('SENDGRID_PASS'))
        self.email_lover.providers.append(sendgrid)

        self.from_email = os.environ.get('EMAILLOVE_FROM')
        self.to_email = os.environ.get('EMAILLOVE_TO')
        if self.to_email is None or self.from_email is None:
            raise RuntimeError("Please set from/to env variables")

        self.subject = "EmailLove SendGrid Test"

    def test_unsubscribes(self):
        results = self.email_lover.unsubscribes()
        self.assertNotEqual(len(results), 0)

    def test_send_html(self):
        result = self.email_lover.send({
            'subject': self.subject,
            'from': self.from_email, 
            'to': [(self.to_email,'')],
            'text': 'EmailLove sendgrid text message',
            'html': '<b>EmailLove</b> sendgrid html <em>message</em>',
        })
        self.assertTrue(result)

    def test_send_text(self):
        result = self.email_lover.send({
            'subject': self.subject,
            'from': self.from_email, 
            'to': [(self.to_email,'')],
            'text': 'EmailLove sendgrid text message',
        })
        self.assertTrue(result)

    def test_send_attachment(self):
        f = open("/tmp/testdoc.txt", "w+")
        f.write("This is a test document for emaillove.")
        f.close()

        result = self.email_lover.send({
            'subject': self.subject,
            'from': self.from_email, 
            'to': [(self.to_email, '')],
            'text': 'EmailLove sendgrid text message',
            'html': '<b>EmailLove</b> sendgrid attachment <em>message</em>',
            'attachments':{
                'testdoc2.txt': '/tmp/testdoc.txt',
            }
        })
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
