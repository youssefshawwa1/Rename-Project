import requests

# get your free API key from here: http://omdbapi.com/

api_key='a19cd23b'
items_list = {"Title",
"Year",
"Rated",
"Released",
"Runtime",
"Genre",
"Director",
"Writer",
"Actors",
"Plot",
"Language",
"Country",
"Poster",
"imdbRating",
"imdbVotes",
"imdbID",
"Type"}
def tvMovieapi(movie_TV_name, year):
	try:
		url=f"http://omdbapi.com/?apikey={api_key}&t={movie_TV_name}"

		response=requests.get(url)
		movie_TV_details=response.json()
		movie_tv_object = dict()
		if "Title" in items_list:
			for items in items_list:
				movie_tv_object[items] = movie_TV_details[items]
		else: print(f"Did Not Get Any Details about {movie_TV_name} {year}")
	except:
			for items in items_list:
				movie_tv_object[items] = ''
			print(f"Did Not Get Any Details about {movie_TV_name} {year}")
	return movie_tv_object
