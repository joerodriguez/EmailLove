import unittest

from emaillove import EmailLove
from emaillove.exceptions import NoCurrentProvider
from emaillove.providers.dummy_provider import DummyProvider


class TestDummySend(unittest.TestCase):
    def setUp(self):
        self.email_lover = EmailLove()
        self.test_message = {'subject': 'subject'}

    def test_sending_no_provider(self):
        with self.assertRaises(NoCurrentProvider):
              self.email_lover.send(self.test_message)

    def test_dummy_send(self):
        dummy = DummyProvider()
        self.email_lover.providers.append(dummy)
        self.email_lover.send(self.test_message)


if __name__ == '__main__':
    unittest.main()
