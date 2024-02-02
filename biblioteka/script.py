import random
# Wszystkie klasy
class LibraryItem:
    def __init__(self, title, release_year, genre, plays):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.plays = plays

    def play(self):
        self.plays += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Movie(LibraryItem):
    pass

class Series(LibraryItem):
    def __init__(self, title, release_year, genre, episode_number, season_number, plays):
        super().__init__(title, release_year, genre, plays)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"

class Library:
    def __init__(self):
        self.library_items = []

    def add_item(self, item):
        self.library_items.append(item)

    def get_movies(self):
        return sorted([item for item in self.library_items if isinstance(item, Movie)], key=lambda x: x.title)

    def get_series(self):
        return sorted([item for item in self.library_items if isinstance(item, Series)], key=lambda x: x.title)

    def search(self, title):
        return [item for item in self.library_items if title.lower() in item.title.lower()]

    def generate_views(self):
        item = random.choice(self.library_items)
        plays = random.randint(1, 100)
        item.plays += plays
        print(f"Generated {plays} views for: {item}")

    def generate_views_multiple_times(self, n):
        for _ in range(n):
            self.generate_views()

    def top_titles(self, n, content_type=None):
        filtered_items = self.library_items
        if content_type == 'movies':
            filtered_items = self.get_movies()
        elif content_type == 'series':
            filtered_items = self.get_series()

        return sorted(filtered_items, key=lambda x: x.plays, reverse=True)[:n]


library = Library()

# dodawnie filmow i serialow
library.add_item(Movie("Film1", 1994, "Crime", 0))
library.add_item(Series("Serial1", 1989, "Animation", 5, 1, 0))

# wyswietla wszystkie filmy
print("Movies:")
for movie in library.get_movies():
    print(movie)

# wyswietla seriale
print("\nSeries:")
for series in library.get_series():
    print(series)

# odtwarzanie
library.get_movies()[0].play()
library.get_series()[0].play()

# Wyszukiawrka
search_results = library.search(input(f"Wpisz tyluł{str}"))
print("\nSearch results: ")
for result in search_results:
    print(f"{result}\n")

# generuje odtworzenia
library.generate_views_multiple_times(10)

# najlepsze tytuly
top_movies = library.top_titles(2, content_type='movies')
print("\nTop Movies:")
for movie in top_movies:
    print(f"{movie} - Plays: {movie.plays}")

top_series = library.top_titles(2, content_type='series')
print("\nTop Series:")
for series in top_series:
    print(f"{series} - Plays: {series.plays}")
