from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
import folium
import io
import csv
import pandas as pd
import sys
class maps_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.maps_tab = tab
        self.control_maps()

    def control_maps(self):
        df = pd.read_csv('nationalparks.csv', usecols=['longitude', 'latitude', 'details',])
        df.columns = ['Longitude', 'Latitude', 'Name']


        map = folium.Map(location=[df.Latitude.mean(), df.Longitude.mean()],
                         zoom_start=6,
                         control_scale=True)
        folium.Marker(location=[df.Latitude.mean(), df.Longitude.mean()]).add_to(map)








