# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

her = media.Movie("Her",
                  "A Spike Jonze love story.",
                  "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
                  "https://www.youtube.com/watch?v=XsQqMwacZQw")


synecdoche = media.Movie("Synecdoche, New York",
                         "A theater director struggles with his work.",
                         "https://upload.wikimedia.org/wikipedia/en/6/6a/Synecdoche%2C_New_York_poster.jpg",
                         "https://www.youtube.com/watch?v=XIizh6nYnTU")


drive = media.Movie("Drive",
                    "There are no clean getaways.",
                    "https://upload.wikimedia.org/wikipedia/en/1/13/Drive2011Poster.jpg",
                    "https://www.youtube.com/watch?v=KBiOF3y1W0Y")

anomalisa = media.Movie("Anomalisa",
                        "Welcome to the Kaufman surreal-neorealism tale in a dull world of sameness.",
                        "https://upload.wikimedia.org/wikipedia/en/0/0f/Anomalisa_poster.jpg",
                        "https://www.youtube.com/watch?v=WQkHA3fHk_0")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "You can erase someone from your mind. Getting them out of your heart is another story.",
                               "https://upload.wikimedia.org/wikipedia/en/a/a4/Eternal_Sunshine_of_the_Spotless_Mind.png",
                               "https://www.youtube.com/watch?v=rb9a00bXf-U")

children = media.Movie("Children of Men",
                       "The Future's a thing of the past.",
                       "https://static.rogerebert.com/uploads/movie/movie_poster/children-of-men-2007/large_pGksHILD8UljwU1J3ZLPPRgyvF8.jpg",
                       "https://www.youtube.com/watch?v=2VT2apoX90o")


isle = media.Movie("Isle of Dogs",
                   "Welcome to the Isle of Dogs.",
                   "https://upload.wikimedia.org/wikipedia/en/2/23/IsleOfDogsFirstLook.jpg",
                   "https://www.youtube.com/watch?v=dt__kig8PVU")

whiplash = media.Movie("Whiplash",
                       "The road to greatness can take you to the edge",
                       "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                       "https://www.youtube.com/watch?v=Df1xkYYbYrY")

arrival = media.Movie("Arrival",
                       "Why are they here?",
                       "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
                       "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

movies = [her, synecdoche, drive, anomalisa, eternal_sunshine, isle]
fresh_tomatoes.open_movies_page(movies)
