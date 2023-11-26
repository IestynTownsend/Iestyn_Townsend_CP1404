# band.py

class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Initialize a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        play_strings = [musician.play() for musician in self.musicians]
        return '\n'.join(play_strings)

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)
