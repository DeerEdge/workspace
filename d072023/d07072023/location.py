from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
import folium
import io
import sys
class maps_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.maps_tab = tab
        self.control_maps()

    def control_maps(self):
        layout = QtWidgets.QVBoxLayout(self.maps_tab)


        coordinate = (39.82836, -98.57948)
        m = folium.Map(
            title = "Golden Gate",
            zoom_start= 4,
            location = coordinate,
        )

        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QtWebEngineWidgets.QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
        self.maps_tab.setLayout(layout)


