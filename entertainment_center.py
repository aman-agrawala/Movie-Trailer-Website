# Note: This file will generate the "Fresh Tomatoes Movie Trailers" website.

"""Here we import the two required files in order to display our website.
The first file is the media.py and the second is the fresh_tomatoes.py"""
import media
import fresh_tomatoes

""" Here I create all the individual instances of the movie class located
in the media.py file. The first arguement, is the movie title, the second
is the URL to the movie's poster and the third is the movie's youtube URL.
The URLs to the poster and the youtube trailer were found online. """
toy_story = media.movies(
    'Toy Story',
    "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_ab.jpg",
    "https://youtu.be/KYz2wyBy3kc",
    "A cowboy doll is profoundly threatened and jealous when a new spaceman \
    figure supplants him as top toy in a boy's room.", "1995", "8.3")
finding_nemo = media.movies(
    "Finding Nemo",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcSoStMb2jeN136xQhf2g3ROpTB \
    9Dker9IlfGbMbwYB3ruC9VcOj",
    "https://youtu.be/wZdpNglLbt8",
    "After his son is captured in the Great Barrier Reef and taken to Sydney, \
    a timid clownfish sets out on a journey to bring him home.",
    "2003", "8.2")
fight_club = media.movies(
    "Fight Club",
    "http://ia.media-imdb.com/images/M/ \
    MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_UY1200_CR88,0,630,1200_AL\
    _.jpg",
    "https://youtu.be/SUXWAEX2jlg",
    "An insomniac office worker, looking for a \
    way to change his life, crosses paths with a devil-may-care soap maker,\
    forming an underground fight club that evolves into something much, much\
    more...", "1999", "8.9")
zodiac = media.movies(
    "Zodiac",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcS7R4yN5HeBG_ \
    4P_nF54K1Uu0TZktfkCJA_g3vP0r5sVoGUnh-9MGgo7w",
    "https://youtu.be/ZVipbvDWbJI",
    "A San Francisco cartoonist becomes an amateur detective \
    obsessed with tracking down the Zodiac killer.", "2007", "7.7")
gone_girl = media.movies(
    "Gone Girl",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcTwcWs6CK22NdvXZH0C \
    bigLxoV-N3GIJypphImFYYv1vG_VKXTQ",
    "https://youtu.be/Ym3LB0lOJ0o",
    "With his wife's disappearance having become the focus of an \
    intense media circus, a man sees the spotlight turned on him \
    when it's suspected that he may not be innocent.", "2014", "8.2")
prisoners = media.movies(
    "Prisoners",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcRy7VMNTnbV4-j2REB3q\
    RecfOSuxKRWIu0AT5QUk_Bu6etiiN6E",
    "https://youtu.be/sfRckdHq--c",
    "When Keller Dover's daughter and her friend go missing, he \
    takes matters into his own hands as the police pursue \
    multiple leads and the pressure mounts. But just how far \
    will this desperate father go to protect his family?", "2013", "8.1")

""" Finally we create a list of all the previously created instances of
the movie class. This list is the input to the open_movies_page function
located in fresh_tomatoes.py. Calling the open_movies_page function is
what generates the website. Therefore, the easiest way to generate the
website would be to run this file."""
movie_list = [toy_story, finding_nemo, fight_club, zodiac,
              gone_girl, prisoners]
fresh_tomatoes.open_movies_page(movie_list)
