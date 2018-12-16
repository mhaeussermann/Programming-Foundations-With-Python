# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#avatar.show_trailer()

synecdoche = media.Movie("Synecdoche, New York",
                         "A theater director is mounting the play of his life",
                         "https://upload.wikimedia.org/wikipedia/en/6/6a/Synecdoche%2C_New_York_poster.jpg",
                         "https://www.youtube.com/watch?v=XIizh6nYnTU")
#synecdoche.show_trailer()

ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("The Hunger Games",
                           "The Games Will Change Everyone",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
movies = [toy_story, synecdoche, ratatouille, hunger_games, midnight_in_paris, avatar]
fresh_tomatoes.open_movies_page(movies)
