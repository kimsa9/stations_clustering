import pandas as pd
from cluster_project.dbscan_clustering import geo_clustering_dbscan
from cluster_project.adress_clustering import process_adress, clustering_street_names, apply_clustering_to_stations

if __name__ == "__main__":

    path = "data/Brisbane_CityBike.json"
    df = pd.read_json(path)

    ## clustering by geographic density

    # Min distance between two stations in km
    min_dist = 0.25

    # Min number of stations in a cluster
    min_stations = 2

    df_new = geo_clustering_dbscan(df, min_dist=min_dist, min_samples=min_stations)
    print("Number of clusters from dbscan:", len(df_new['cluster'].unique()))

    df_new.to_csv("output/geo_cluster.csv", index = None)

    ## Clustering by street name
    documents = df['address'].tolist()
    num_clusters = 25

    df_new = clustering_street_names(documents, num_clusters)

    df_new.to_csv("output/street_names_cluster.csv", index = None)



