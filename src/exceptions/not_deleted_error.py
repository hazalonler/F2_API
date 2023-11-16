class Error(Exception):
    """Base class for all types of exceptions in F2 API"""
    pass


class NotDeletedError(Error):
    """Raised when the task is not deleted"""
    pass
