def isInteger(numeric_string: str) -> bool:
    try:
        if not(float(numeric_string).is_integer()):
            return False
        return True
    except ValueError:
        return False


def get_integer_from_specified_range(prompt: str, start_range: float = float("-inf"), end_range: float = float("inf")) -> int:
    
    while not (isInteger(user_input := input(prompt)) 
            and (start_range <= int(float(user_input)) <= end_range)):  
        print("Invalid input!")
    
    return int(float(user_input))


def display_projections_information(projections: list[dict[str, str | int]]) -> None:
    
    print("{:<5}{:<20}{:<10}{:<15}{:<5}".format("N°", "Title", "Time", "Theater", "Available seats"))
    print("-" * 70)
    
    for projection_number, projection in enumerate(projections, start = 1):
        print("{:<5}{:<20}{:<10}{:<15}{:<5}".format(
            projection_number,
            projection["movie_title"],
            projection["time"],
            projection["theater"],
            projection["available_seats"]
        ))


def book_a_reservation(projection_number: int, seats_to_book: int, projections: list[dict[str, str | int]]) -> dict[str, str | int]:

    selected_projection: dict[str, str | int]
    selected_projection = projections[projection_number-1]
    
    reservation: dict[str, str | int]
    reservation=selected_projection.copy()
    
    reservation.pop("available_seats")

    reservation["reserved_seats"] = seats_to_book
    
    available_seats: int
    available_seats = selected_projection["available_seats"] - seats_to_book
    
    selected_projection.update({"available_seats": available_seats})
    
    return reservation

# Creates a dictionary mapping each projection number to a list of reservations.
# The user is prompted to choose a projection and enter how many seats to reserve.
# If the request is valid (within available seats), the reservation is saved
# under the corresponding projection key.
def create_reservations_for_projection(projections: list[dict[str, str | int]]) -> dict[int, list[dict[str, str | int]]]:

    reservations_for_projection: dict[int, list[dict[str, str | int]]] = {}

    number_of_reservations: int = get_integer_from_specified_range("How many reservations do you want to make? ", 0)

    for _ in range(number_of_reservations):

        projection_number: int = get_integer_from_specified_range("Enter the projection number: ", 1, len(projections))
        seats_to_book: int = get_integer_from_specified_range("How many seats do you want to reserve: ", 1)

        if seats_to_book <= projections[projection_number-1]["available_seats"]:

            reservation: dict[str, str | int]
            reservation = book_a_reservation(projection_number, seats_to_book, projections)
            
            reservations_for_projection.setdefault(projection_number, []).append(reservation)
            
        else:
            print(f"The number of seats you want to book exceeds the available seats for screening number {projection_number}!")

    return reservations_for_projection


def display_reservations_for_projection(reservations_for_projection: dict[int, list[dict[str, str | int]]]) -> None:

    for projection_number, reservations_list in reservations_for_projection.items():
        
        print(f"\n\nReservations for projection number {projection_number}:")
        print()

        print("{:<5}{:<20}{:<10}{:<15}{:<5}".format("N°", "Title", "Time", "Theater", "Reserved seats"))
        print("-" * 70)

        for reservation_number, reservation in enumerate(reservations_list, start=1):
            print("{:<5}{:<20}{:<10}{:<15}{:<5}".format(
                reservation_number, 
                reservation['movie_title'], 
                reservation['time'], 
                reservation['theater'], 
                reservation['reserved_seats'])
            )
        print("-" * 70)


def change_reservation(projections: list[dict[str, str | int]], reservations_for_projection: dict[int, list[dict[str, str | int]]]) -> None:

    projection_number: int = get_integer_from_specified_range("Enter the projection number: ", 1, len(projections))

    if projection_number in reservations_for_projection:
        
        reservation_number: int = get_integer_from_specified_range("Enter the reservation number: ", 1, len(reservations_for_projection[projection_number]))

        selected_reservation: dict[str, str | int] = reservations_for_projection[projection_number][reservation_number-1]
        
        seats_to_book: int = get_integer_from_specified_range("How many seats do you want to reserve: ", 1)
        
        
        # Restore available seats by adding back the reserved seats from the selected reservation.
        # This avoids issues when modifying a reservation — it's like temporarily canceling it,
        # so those seats become available again before applying the new change.
        available_seats = projections[projection_number-1]["available_seats"] + selected_reservation["reserved_seats"]
        
        if seats_to_book <= available_seats:
            
            selected_reservation.update({"reserved_seats": seats_to_book})
            
            available_seats-= seats_to_book
            
            projections[projection_number-1].update({"available_seats": available_seats})
            
        else:
            print(f"The number of seats you want to book exceeds the available seats for screening number {projection_number}!")
        
    else: 
        print(f"There are no reservations for screening number {projection_number}!") 


def delete_reservation(projections: list[dict[str, str | int]], reservations_for_projection: dict[int, list[dict[str, str | int]]]) -> None:

    projection_number: int = get_integer_from_specified_range("Enter the projection number: ", 1, len(projections))

    if projection_number in reservations_for_projection and reservations_for_projection[projection_number]:
        
        reservation_number: int = get_integer_from_specified_range("Enter the reservation number: ", 1, len(reservations_for_projection[projection_number]))
        
        selected_reservation: dict[str, str | int] = reservations_for_projection[projection_number][reservation_number-1]
        
        available_seats = projections[projection_number-1]["available_seats"] + selected_reservation["reserved_seats"]
        projections[projection_number-1].update({"available_seats": available_seats})
            
        reservations_for_projection[projection_number].pop(reservation_number-1) 
   
    else:
        print(f"There are no reservations for screening number {projection_number}!")


projections: list[dict[str, str | int]]
projections = [ 
    {
        "movie_title": "The Lion King",
        "time": "21:00",
        "theater": "Theater 1",
        "available_seats": 20       
    },
    
    {
        "movie_title": "Jurassic Park",
        "time": "18:00",
        "theater": "Theater 2",
        "available_seats": 25          
    },
    
    {
        "movie_title": "Forrest Gump",
        "time": "21:00",
        "theater": "Theater 2",
        "available_seats": 30       
    },
    
    {
        "movie_title": "Titanic",
        "time": "20:00",
        "theater": "Theater 3",
        "available_seats": 15   
    },
    
    {
        "movie_title": "Shrek",
        "time": "21:00",
        "theater": "Theater 4",
        "available_seats": 10   
    },
    
    {
        "movie_title": "Interstellar",
        "time": "18:00",
        "theater": "Theater 1",
        "available_seats": 55    
    }    
]


def main():
    print("List of projections: ")
    display_projections_information(projections)

    reservations_for_projection=create_reservations_for_projection(projections)   

    if reservations_for_projection: 
        display_reservations_for_projection(reservations_for_projection)
            
        num_reservations_to_change: int = get_integer_from_specified_range("How many reservations do you want to change? ", 0)
        for _ in range(num_reservations_to_change):  
            
            change_reservation(projections, reservations_for_projection)
        
        print()
        
        num_reservations_to_delete: int = get_integer_from_specified_range("How many reservations do you want to delete? ", 0)
        for _ in range(num_reservations_to_delete):
            if reservations_for_projection:
                delete_reservation(projections, reservations_for_projection)
                   
    else:
        print("No reservations have been made!")


if __name__=="__main__":
    main()