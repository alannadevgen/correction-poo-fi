# Definition of custom exceptions
class SeatCountError(Exception):
    """Exception raised when the number of requested seats exceeds the available seats."""
    pass


class SeatUnavailableError(Exception):
    """Exception raised when a requested seat is already reserved."""
    pass


class SeatDoesNotExistError(Exception):
    """Exception raised when a requested seat does not exist on the plane."""
    pass