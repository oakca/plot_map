import pandas as pd
import folium as fo
from folium.features import DivIcon


def create_map(data):
    # get average coordinates
    avg_lat = data['lat'].mean()
    avg_lon = data['lon'].mean()

    # add color column
    color = {'producer': '#ff0000', 'consumer': ' #00ff00', 'split': '#000000'}
    data = (data.assign(node_color=data['node_type'])
                .replace({'node_color': color}))

    # create map
    m = fo.Map(location=[avg_lat, avg_lon],
               zoom_start=8)

    for i in range(0, len(data)):
        # draw colorful circles
        fo.CircleMarker([data['lat'][i], data['lon'][i]],
                        radius=20,
                        # popup=data['node_id'][i],
                        color=data['node_color'][i],
                        fill_color=data['node_color'][i]).add_to(m)

        # draw node ids
        fo.Marker([data['lat'][i], data['lon'][i]],
                  icon=DivIcon(icon_size=(20, 30),
                               icon_anchor=(0, 0),
                               html='<div style="font-size: 16pt">%s</div>'
                               % data['node_id'][i])).add_to(m)

    return m


if __name__ == '__main__':
    # read data
    data = pd.read_csv('data/node_list.csv')

    # choose map name & create map & save
    map_name = 'map'
    map = create_map(data)
    map.save('map/'+map_name+'.html')
