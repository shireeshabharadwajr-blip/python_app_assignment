class MovieTicket:
    def __init__(self, movie_name, theatre, seat_number):
        self.movie_name = movie_name
        self.theatre = theatre
        self.seat_number = seat_number

    def __str__(self):
        return f"Movie: {self.movie_name} | Theatre: {self.theatre} | Seat: {self.seat_number}"

if __name__ == "__main__":
    ticket1 = MovieTicket("Avatar 2", "PVR Cinemas", "A12")
    ticket2 = MovieTicket("Inception", "INOX", "B5")
    ticket3 = MovieTicket("Interstellar", "IMAX", "F8")

    print(ticket1)
    print(ticket2)
    print(ticket3)
