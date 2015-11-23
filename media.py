"""Here I import webbrowser.py file in order to open the URL
to the youtube trailer for the movies in the show_trailer function.
This was something that I did for my own knowledge and was not
required for the project.
"""
import webbrowser

"""Here I create the movies class which inherits from the object class.
The __init__ construction takes in 7 arguements: self (the instance of
the class movies), movie_title (a string that is the title of the movie),
movie_poster_images (a string of the URL to the movie poster image found
online), movie_trailer_URL (a string of the URL to the youtube trailer
for the movie), movie_description (a string that describes the plot of
the movie), release_date (a string that contains the date the movie was
released) and IMDB_Rating(a string that contains IMDB's rating of the
movie). The instance variables title, poster_image_url and trailer_youtube_url
were named after the same variables found in the fresh_tomatoes.py in order
for python to recognize the variables. The names of the remaining variables
were chosen.
"""


class movies(object):
    def __init__(self, movie_title, movie_poster_images, movie_trailer_URL,
                 movie_description, release_date, IMDB_Rating):
        self.title = movie_title
        self.poster_image_url = movie_poster_images
        self.trailer_youtube_url = movie_trailer_URL
        self.movie_description = movie_description
        self.date = release_date
        self.rating = IMDB_Rating

    """The show_trailer function takes in an instance of the movies class
    and uses the instance variable trailer_youtube_url to open a webbrowser
    to display the youtube trailer."""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
