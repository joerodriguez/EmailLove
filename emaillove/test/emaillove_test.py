import unittest

from emaillove import EmailLove
from emaillove.exceptions import NoCurrentProvider
from emaillove.providers.dummy_provider import DummyProvider


class TestDummySend(unittest.TestCase):
    def setUp(self):
        self.email_lover = EmailLove()

    def test_sending_no_provider(self):
        with self.assertRaises(NoCurrentProvider):
              self.email_lover.send({'subject':"subject"})

    def test_dummy_send(self):
        dummy = DummyProvider()
        self.email_lover.providers.append(dummy)


if __name__ == '__main__':
    unittest.main()