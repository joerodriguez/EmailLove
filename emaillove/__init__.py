from emaillove.exceptions import NoCurrentProvider


class EmailLove:
    def __init__(self):
        self.providers = []
        self.current_provider = None

    def send(self, message):
        ''' Send this message from the current provider '''
        if self.current_provider is None:
            if len(self.providers) == 1:
                self.current_provider = self.providers[0]
            else:
                raise NoCurrentProvider("No current provider selected")
        return self.current_provider.send(message)
