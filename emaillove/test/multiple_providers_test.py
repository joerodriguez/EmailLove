import unittest

from emaillove import EmailLove
from emaillove.exceptions import NoCurrentProvider
from emaillove.providers.dummy_provider import DummyProvider
from emaillove.providers.mailgun_provider import MailGun 


class TestDummySend(unittest.TestCase):
    def setUp(self):
        self.email_lover = EmailLove()
        self.test_message = {'subject': 'subject'}

    def test_dummy_send(self):
        dummy = DummyProvider()
        mailgun = MailGun()
        self.email_lover.providers.append(dummy)
        self.email_lover.providers.append(mailgun)
        self.email_lover.send(self.test_message)


if __name__ == '__main__':
    unittest.main()

