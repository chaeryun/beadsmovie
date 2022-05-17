import simplejson

from movie.models import Movie
from movie.serializers import MovieSerializer

# TODO:
# 1. 경로와 파일명들 변수화
# 2. 에러 발생 로그찍어 보관
# 3. tmdb에 api 요청부분 추가
# 4. 스케쥴러 등록

f = open('/home/iireh/code/S06P31C201/MoviePjt/movie-pjt-back/db_schema.json', mode='rt')
movies = simplejson.load(f)
f.close()

f = open('/home/iireh/code/S06P31C201/MoviePjt/movie-pjt-back/db_genre_kr.json', mode='rt')
genres = simplejson.load(f)
f.close()

genre_dict = dict()
for genre in genres:
    genre_dict[genre['name']] = genre

is_added = dict()
unique_movies = list()
for movie in movies:
    if not is_added.get(movie['pk'], False):
        is_added[movie['pk']] = True

        movie_id = movie.pop('pk')
        movie = movie.pop('fields')
        movie['_id'] = movie_id
        genres = list()
        for genre in movie['genres']:
            genres.append(genre_dict[genre])
        movie['genres'] = genres
        unique_movies.append(movie)

f = open('/home/iireh/code/S06P31C201/MoviePjt/movie-pjt-back/db_schema_unique.json', mode='wt')
simplejson.dump(unique_movies, f, ensure_ascii=False, indent=' '*4)
f.close()

objs = list()
movies = unique_movies
for movie in movies:
    serializer = MovieSerializer(data=movie)
    if serializer.is_valid():
        objs.append(serializer.create(serializer.validated_data))
    else:
        print(serializer.initial_data)
        print(serializer.errors)
Movie.objects.bulk_create(objs)


