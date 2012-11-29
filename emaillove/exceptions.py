class EmailLoveException(RuntimeError):
    pass

class NoCurrentProvider(EmailLoveException):
    pass

