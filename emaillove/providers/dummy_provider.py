from emaillove.providers.base_provider import BaseProvider


class DummyProvider(BaseProvider):
    def __init__(self):
        print "Init dummy"

    def send(message):
        print "Dummy send"
