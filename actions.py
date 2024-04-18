# Author: Bruno Ferraz

import re


def add_movie(movies):
    """ Adds a new movie to a list """
    while True:
        try:
            title = input("Title (max 32 characters): ")
            if not title or len(title) > 32:
                raise ValueError("Title must be non-empty and up to 32 characters.")

            # Check if the title is unique
            if any(movie["title"] == title for movie in movies):
                raise ValueError("Title must be unique.")

            genre = input("Genre: ")
            if not genre or re.search(r"^[A-Za-z ]+$", genre) is None:
                raise ValueError("Genre is invalid.")

            running_length = input("Running Length (HH:MM): ")
            if not running_length or re.search(r"^(?:[0-9]{1,2}):[0-5][0-9]$", running_length) is None:
                raise ValueError("Running Length must be in the format HH:MM.")

            year = input("Year (greater than 1920): ")
            if not year or len(year) != 4 or not year.isdigit() or int(year) <= 1920:
                raise ValueError("Year must be four digits and greater than 1920.")

            rating = input("Rating (1 to 5): ")
            if not rating or not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
                raise ValueError("Rating must be a number from 1 to 5.")

            description = input("Description (max 128 characters): ")
            if not description or len(description) > 128:
                raise ValueError("Description must be non-empty and up to 128 characters.")

            # If all validations pass, add the movie to the list
            movie = {
                "title": title,
                "genre": genre,
                "running_length": running_length,
                "year": int(year),
                "rating": int(rating),
                "description": description
            }
            movies.append(movie)

            print("Movie added successfully!")
            return movie  # Return the added movie

        except ValueError as e:
            print("Error:", e)


def delete_movie(title, movies):
    """ Delete movie from the list """
    for movie in movies:
        if movie["title"] == title:
            movies.remove(movie)
            print("Movie deleted successfully.\n")
            return

    print("No matching movies found\n")


def movie_summary(movies):
    """ Display summary of movies in the list"""
    for movie in movies:
        if len(movie["description"]) > 30:
            short_descr = movie["description"][:30]
        else:
            short_descr = movie["description"]
        print(f"Title: {movie['title']}, "
              f"Genre: {movie['genre']}, "
              f"Length: {movie['running_length']}, "
              f"Year: {movie['year']}, "
              f"Rating: {movie['rating']}, "
              f"Description: {short_descr}")
    print()
    return


def movie_rating(movies):
    """ Display movies based on rating given by user """
    user_rating = input("Rating: ")
    if not re.match(r"^[1-5]$", user_rating):
        print(f"Rating must be between 1 and 5\n")
        return

    for movie in movies:
        if int(movie["rating"]) >= int(user_rating):
            print(f"Title: {movie['title']}, "
                  f"Genre: {movie['genre']}, "
                  f"Length: {movie['length']}, "
                  f"Year: {movie['year']}, "
                  f"Rating: {movie['rating']}, "
                  f"Description: {movie['description']}")
    print()
    return


def movie_title(movies):
    """ Display movies that match (fully or partially) the title given by user """
    user_title = input("Title: ").lower()

    if 1 > len(user_title) > 32:
        print(f"Title must be between 1 and 32 characters\n")
        return

    found_movies = [movie for movie in movies if user_title in movie["title"].lower()]

    if found_movies:
        for movie in found_movies:
            print(f"Title: {movie['title']}, "
                  f"Genre: {movie['genre']}, "
                  f"Length: {movie['length']}, "
                  f"Year: {movie['year']}, "
                  f"Rating: {movie['rating']}, "
                  f"Description: {movie['description']}\n")
    else:
        print("There are no movies.\n")
    return


def movie_genre(movies):
    """ Display movies that match (fully or partially) the genre given by user """
    user_genre = input("Genre: ")
    if not re.match(r"^[A-Za-z ]+$", user_genre):
        print("Genre must have at least one character\n")
        return

    found_genres = [movie for movie in movies if user_genre in movie["genre"]]

    if found_genres:
        for movie in found_genres:
            print(f"Title: {movie['title']}, "
                  f"Genre: {movie['genre']}, "
                  f"Length: {movie['length']}, "
                  f"Year: {movie['year']}, "
                  f"Rating: {movie['rating']}, "
                  f"Description: {movie['description']}")
    else:
        print("There are no movies")
    print()
    return
