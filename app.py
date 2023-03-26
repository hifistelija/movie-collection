MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ").strip().title()
    director = input("Enter the movie director: ").strip().title()
    year = input("Enter the movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


def movie_list():
    for movie in movies:
        print_movie(movie)


def find_movie():
    movie_to_find = input("Enter a movie title to search for: ")

    for movie in movies:
        if movie["title"].lower() == movie_to_find.lower():
            print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


user_options = {
    "a": add_movie,
    "l": movie_list,
    "f": find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command. Please ty again")

        selection = input(MENU_PROMPT)


menu()
