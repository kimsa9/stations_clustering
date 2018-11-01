from folium import plugins
import folium

def plot_stations_clusters(df_new):
    """
    Plot the stations on a map with a color for each cluster
    :param df_new: dataframe with longitude, latitude and cluster number
    :return: the figure
    """
    # convert to (n, 2) nd-array format for heatmap
    stationArr =  df_new[['latitude', 'longitude']].values.tolist()

    m = folium.Map(location=[df_new['latitude'].mean(), df_new['longitude'].mean()],
                        zoom_start = 14, tiles = 'Cartodb Positron')

    colors = ['black', 'red', 'blue', 'green', 'purple', 'orange', 'darkred',
                 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue',
                 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen',
                 'gray', 'black', 'lightgray', 'yellow', 'brown', 'red',]
    # plot heatmap
    for point in range(0, len(stationArr)):
        num_cluster = df_new.iloc[point]['cluster']
        folium.CircleMarker(stationArr[point], radius=2, color=colors[int(num_cluster)+1]).add_to(m)

    return m