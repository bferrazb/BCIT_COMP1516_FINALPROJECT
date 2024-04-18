# Author: Bruno Ferraz

import file_io
import actions
import sys


def user_input():
    """ Prompts the user for an input and returns that input """
    command = (
        input(f"Enter an action:\n"
              f"Add Movie (a)\n"
              f"Delete Movie (d)\n"
              f"View Movies Summary (s)\n"
              f"Search Movie by Rating (r)\n"
              f"Search Movie by Title (t)\n"
              f"Search Movie by Genre (g)\n"
              f"Quit (q)\n"))

    return command.lower()


def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        sys.exit(0)
    filepath = sys.argv[1]
    movies = file_io.read_movies(filepath)

    # RUNNING PROGRAM:
    command = user_input()
    while command != "q":

        # ADDING A MOVIE:
        if command == "a":
            actions.add_movie(movies)
            file_io.write_movies(movies, filepath)

        # DELETING MOVIE:
        if command == "d":
            del_title = input("Title: ")

            # VALIDATING ENTRY:
            try:
                if len(del_title) > 32:
                    raise ValueError("Title must have a maximum of 32 characters.")
            except ValueError as err:
                print(err)

            actions.delete_movie(del_title, movies)
            file_io.write_movies(movies, filepath)

        # DISPLAY SUMMARY OF MOVIES:
        if command == "s":
            actions.movie_summary(movies)

        # SEARCH MOVIES BY RATING:
        if command == "r":
            actions.movie_rating(movies)

        # SEARCH MOVIES BY TITLE:
        if command == "t":
            actions.movie_title(movies)

        # SEARCH MOVIES BY GENRE:
        if command == "g":
            actions.movie_genre(movies)

        command = user_input()

    # QUITTING MOVIE MANAGER & SAVING FILE:
    file_io.write_movies(movies, filepath)
    print("Quitting Movie Manager...")
    sys.exit(0)


if __name__ == "__main__":
    main()
