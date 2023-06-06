movie_name = input("название фильма: ")
cinema_name = input("название кинотеатра: ")
time = input("время: ")



text = "Билет на %s в %s на %s забронирован." % (movie_name, cinema_name, time)

print(text)