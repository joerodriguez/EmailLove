from emaillove.exceptions import MissingMethod


class BaseProvider:
    def __init__(self):
        raise MissingMethod("Provider failed to override init")

    def send(self, message):
        raise MissingMethod("Provider failed to override send")

    def unsubscribes(self, start_date=None, end_date=None):
        ''' Get the latest unsubscribes 
        '''
        return None 
