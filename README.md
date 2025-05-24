# Cinema Booking Manager

## Description:
The present project consists in the development of a reservation manager for a cinema, a tool that allows users to reserve and manage seats for film screenings. The manager will capture showing information, such as movie title, time, theater, and available seats, and provide features to view, book, edit, and delete seat reservations.

## Objective:
The goal of the project is to provide users with a practical tool for managing seat reservations for cinema screenings. Using variables, strings, mathematical calculations, conditional operators, loops, functions, arrays and JSON objects, the manager will allow users to make reservations, check seat availability and manage existing reservations.

## Main features:

### Viewing Projection Information:

- Using an array of JSON objects, store showing information, such as movie title, time, theater, and available seats.
- Use a for loop to iterate through the array and print a list of projections to the screen, showing key information about each projection.

### Seat reservations for a screening:

- Using a function, allow the user to select a screening and enter information for the reservation, such as the number of seats required.
- Check the availability of seats for the selected screening and, if available, update the JSON object corresponding to the screening with the booking details.

### Change of reservations:

- Using a for loop, display the list of reservations for a specific projection and allow the user to select a reservation to edit.
- Using a function, allow the user to edit reservation information, such as number of seats, and update the JSON object corresponding to the reservation.

### Deleting reservations:

- Using a for loop, display the list of reservations for a specific projection and allow the user to select a reservation to delete.
- Remove the JSON object corresponding to the selected reservation from the reservations array.
