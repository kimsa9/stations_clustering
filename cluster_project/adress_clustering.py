from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.feature_extraction import text
import pandas as pd

def clustering_adress(documents, num_clusters):
    """
    :param documents: list of street names
    :param num_clusters: number of cluster to find
    :return:the dataframe with each cluster associated to each station
    """
    my_stop_words = text.ENGLISH_STOP_WORDS.union(['st', 'rd', 'dr', 'tce', 'park', 'mall', 'bridge', 'sir'])

    vectorizer = TfidfVectorizer(stop_words=my_stop_words, lowercase=True)
    X = vectorizer.fit_transform(documents)

    model = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)

    Y = vectorizer.transform(documents)
    prediction = model.predict(Y)

    df_ = pd.DataFrame(documents, columns = ['name'])
    df_['cluster'] = prediction

    df = pd.merge(df, df_, how='left', on='address')

    return df.sort_values(by = "number")