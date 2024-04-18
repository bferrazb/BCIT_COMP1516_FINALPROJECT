# Author: Bruno Ferraz

import json


def read_movies(filepath):
    """ Reads movies from a JSON file and returns a list """
    try:
        with open(filepath, 'r') as json_file:
            movies = json.load(json_file)
            return movies
    except FileNotFoundError:
        print("The movie database does not exist.")
        return []


def write_movies(movies, filepath):
    """ Writes movies to a JSON file """
    with open(filepath, 'w') as json_file:
        json.dump(movies, json_file, indent=4)
        print("List of movies saved successfully")
