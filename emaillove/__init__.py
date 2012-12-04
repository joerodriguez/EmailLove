from emaillove.exceptions import NoCurrentProvider


class EmailLove:
    def __init__(self):
        self.providers = []
        self.current_provider = None

    def get_current_provider(self):
        if self.current_provider is None:
            if len(self.providers) > 0:
                self.current_provider = self.providers[0]
            else:
                raise NoCurrentProvider("No current provider selected")
        return self.current_provider

    def send(self, message):
        ''' Send this message from the current provider '''
        return self.get_current_provider().send(message)

    def unsubscribes(self, since=None):
        return self.get_current_provider().unsubscribes(since)
