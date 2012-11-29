class EmailLoveException(RuntimeError):
    pass

class NoCurrentProvider(EmailLoveException):
    pass

class MissingMethod(EmailLoveException):
    pass
