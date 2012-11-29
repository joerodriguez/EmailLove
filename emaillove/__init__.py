class EmailLoveException(Exception):
    pass

class NoCurrentProvider(EmailLoveException):
    pass

class EmailLove:
    def __init__(self):
        print "Init Email Love"
        self.providers = []
        self.current_provider = None

    def add_provider(self, provider):
        # exists? override?
        self.providers.append(provider)

    def send(self, message):
        ''' Send this message from the current provider '''
        if self.current_provider is None:
            raise NoCurrentProvider("No current provider selected")
        if self.current_provider is not None:
            self.current_provider.send(message)
