from math import radians, cos, sin, asin, sqrt
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import DBSCAN
import pandas as pd

def geo_clustering_dbscan(df, min_dist = 0.6, min_samples = 3):
    """
    Find isolated tanks and the groups of tanks
    :param df: dataframe with the geocoordinates
    :param min_dist: minimum distance in km between two stations in the same cluster
    :param min_samples: minumum number of stations in a cluster
    :return: dataframe with the cluster number associated to each station
    """
    X = df[['latitude', 'longitude']].copy()
    distance_matrix = squareform(pdist(X, (lambda u, v: haversine(u, v))))

    db = DBSCAN(eps=min_dist, min_samples=min_samples, metric='precomputed')
    y_db = db.fit_predict(distance_matrix)

    X['cluster'] = y_db

    res = pd.merge(df, X, how="left", on=['longitude', 'latitude'])

    return res


def haversine(lonlat1, lonlat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lat1, lon1 = lonlat1
    lat2, lon2 = lonlat2
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r