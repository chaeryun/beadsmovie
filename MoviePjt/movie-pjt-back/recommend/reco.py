import io
import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from scipy import spatial
import numpy as np

def vote_count(n=5):
    df = pd.read_json('movie.json')
    df3 = df.copy()
    df4 = df3.sort_values('vote_count', ascending=False).head(n)
    return df4.pk.tolist()
#print(vote_count(5))



def popularity(n=5):
    df = pd.read_json('movie.json')
    df3 = df.copy()
    df4 = df3.sort_values('popularity', ascending=False).head(n)
    return df4
# print(popularity(10))



def vote_average(n=5):
    df = pd.read_json('movie.json')
    df3 = df.copy()
    df4 = df3.sort_values('vote_average', ascending=False).head(n)
    return df4.pk.tolist()
#print(vote_average(5))


# 장르별 영화 추천
def genre_build_chart(genre_id):
    dict1 = {
    "28": "액션",
    "12": "모험",
    "16": "애니메이션",
    "35": "코미디",
    "80": "범죄",
    "99": "다큐멘터리",
    "18": "드라마",
    "10751": "가족",
    "14": "판타지",
    "36": "역사",
    "27": "공포",
    "10402": "음악",
    "9648": "미스터리",
    "10749": "로맨스",
    "878": "SF",
    "10770": "TV 영화",
    "53": "스릴러",
    "10752": "전쟁",
    "37": "서부"
    }
    genre = dict1[str(genre_id)]
    df3 = pd.read_json('./recommend/movie.json')
    df = df3.copy()
    percentile=0.88
    df['year'] = pd.to_datetime(df['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
    s = df.apply(lambda x: pd.Series(x['genres']), axis=1).stack().reset_index(level=1, drop=True)
    s.name = 'genre'
    gen_md = df.drop('genres', axis=1).join(s)
    df3 = gen_md[gen_md['genre'] == genre]
    vote_counts = df3[df3['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = df3[df3['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)
    qualified = df3[(df3['vote_count'] >= m) & (df3['vote_count'].notnull()) & (df3['vote_average'].notnull())][['title','pk','vote_count','vote_average','popularity']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    qualified['sc'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
    qualified = qualified.sort_values('sc', ascending=False).head(10)
    a = qualified.pk.tolist()
    a.reverse()
    return a
    return qualified.pk.tolist()



# Detail 영화 추천
def get_recommendations(pk):
    df3 = pd.read_json('./recommend/movie.json')
    df = df3.copy()
    title = df.loc[df['pk'] == int(pk)]
    title = title.iloc[0]['title']
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2),
    min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(df['overview'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    df = df.reset_index()
    titles = df['pk']
    indices = pd.Series(df.index, index=df['title'])
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    result = titles.iloc[movie_indices].head(10)
    return result.tolist()

# 최근 인기영화
def top_movies(n=10):
    df3 = pd.read_json('./recommend/movie.json')
    df = df3.copy()
    a = df.query('"2022-01-01"<= release_date <= "2022-05-31"')
    df4 = a.sort_values('popularity', ascending=False).head(n)
    return df4.pk.tolist()

