from exceptions import SeatCountError, SeatUnavailableError, SeatDoesNotExistError


# Definition of the PlaneSeats class
class PlaneSeats:
    def __init__(self, capacity, available_seats):
        """
        Initializes the class with the total capacity and the available seats.

        Parameters
        ----------
        capacity : int
            Total number of seats on the plane.
        available_seats : list
            A list of available seats on the plane.
        """
        self.capacity = capacity
        self.available_seats = set(available_seats)
        self.reserved_seats = set()

    def reserve_seats(self, seats):
        """
        Reserves a list of seats if all conditions are met.

        Parameters
        ----------
        seats : list
            A list of seat numbers to reserve.

        Raises
        ------
        SeatCountError
            If the number of requested seats exceeds the available seats.
        SeatUnavailableError
            If a seat is already reserved.
        SeatDoesNotExistError
            If a seat does not exist on the plane.
        """
        # Check the number of available seats
        if len(seats) > self.capacity - len(self.reserved_seats):
            raise SeatCountError(
                "Not enough available seats for the requested reservation."
            )

        # Check the availability and existence of the seats
        for seat in seats:
            if seat in self.reserved_seats:
                raise SeatUnavailableError(f"Seat {seat} is already reserved.")
            if seat not in self.available_seats:
                raise SeatDoesNotExistError(f"Seat {seat} does not exist on the plane.")

        # If all checks pass, add the seats to the list of reserved seats
        self.reserved_seats.update(seats)
        print(f"Reservation successful for seats: {seats}")


# Creating an instance and test scenarios
if __name__ == "__main__":
    # Initializing the plane
    plane = PlaneSeats(capacity=10, available_seats=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Nominal case: successful reservation
    try:
        plane.reserve_seats([1, 2])
    except Exception as e:
        print(e)

    # Error: seat already reserved
    try:
        plane.reserve_seats([2])
    except Exception as e:
        print(e)

    # Error: seat does not exist
    try:
        plane.reserve_seats([11])
    except Exception as e:
        print(e)

    # Error: too many seats requested
    try:
        plane.reserve_seats([3, 4, 5, 6, 7, 8, 9, 10])
    except Exception as e:
        print(e)

    # Combined successful reservation
    try:
        plane.reserve_seats([3, 4])
    except Exception as e:
        print(e)

    # Display reserved seats
    print(f"Reserved seats: {plane.reserved_seats}")
