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
    return df4.pk.tolist()
#print(popularity(10))



def vote_average(n=5):
    df = pd.read_json('movie.json')
    df3 = df.copy()
    df4 = df3.sort_values('vote_average', ascending=False).head(n)
    return df4.pk.tolist()
#print(vote_average(5))


def genre_build_chart(genre):
    df3 = pd.read_json('movie.json')
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
    return qualified.pk.tolist()
#print(genre_build_chart('로맨스'))




def get_recommendations(pk):
    df3 = pd.read_json('movie.json')
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

<<<<<<< HEAD
# print(get_recommendations('414906'))
=======
#print(get_recommendations('634649'))
#print(get_recommendations('414906'))
#print(get_recommendations('99861'))
>>>>>>> ce985f11 (adsfd)
