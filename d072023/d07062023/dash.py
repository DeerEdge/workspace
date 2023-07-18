from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore, QtWidgets
import sqlite3
from d072023.d07062023 import create_widgets

class dash_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.dash_tab = tab
        self.control_dashboard()

    def control_dashboard(self):
        self.groupbox = QtWidgets.QGroupBox(self.dash_tab)
        self.groupbox.setObjectName("GroupBox_Dash")
        self.groupbox.resize(210, 540)
        self.groupbox.move(15, 40)

        self.filters_label = QtWidgets.QLabel(self.groupbox)
        self.filters_label.setText("Filter By:")
        self.filters_label.setObjectName("Filters_Label")
        self.filters_label.move(20, 20)

        self.state_label = QtWidgets.QLabel(self.groupbox)
        self.state_label.setText("State:")
        self.state_label.setObjectName("State_Label")
        self.state_label.move(10, 61)

        self.state_dropdown = QtWidgets.QComboBox(self.groupbox)
        self.state_dropdown.setObjectName("State_Dropdown")
        self.state_dropdown.addItem("No Preference")
        self.state_dropdown.addItem("Alaska")
        self.state_dropdown.addItem("Arizona")
        self.state_dropdown.addItem("Arkansas")
        self.state_dropdown.addItem("California")
        self.state_dropdown.addItem("Colorado")
        self.state_dropdown.addItem("Florida")
        self.state_dropdown.addItem("Hawaii")
        self.state_dropdown.addItem("Idaho")
        self.state_dropdown.addItem("Indiana")
        self.state_dropdown.addItem("Kentucky")
        self.state_dropdown.addItem("Maine")
        self.state_dropdown.addItem("Michigan")
        self.state_dropdown.addItem("Minnesota")
        self.state_dropdown.addItem("Missouri")
        self.state_dropdown.addItem("Montana")
        self.state_dropdown.addItem("Nevada")
        self.state_dropdown.addItem("New Mexico")
        self.state_dropdown.addItem("North Dakota")
        self.state_dropdown.addItem("North Carolina")
        self.state_dropdown.addItem("Ohio")
        self.state_dropdown.addItem("Oregon")
        self.state_dropdown.addItem("South Carolina")
        self.state_dropdown.addItem("South Dakota")
        self.state_dropdown.addItem("Tennessee")
        self.state_dropdown.addItem("Texas")
        self.state_dropdown.addItem("Utah")
        self.state_dropdown.addItem("Virginia")
        self.state_dropdown.addItem("Washington")
        self.state_dropdown.addItem("West Virginia")
        self.state_dropdown.addItem("Wyoming")
        self.state_dropdown.resize(130, 40)
        self.state_dropdown.move(70, 50)

        self.features_label = QtWidgets.QLabel(self.groupbox)
        self.features_label.setText("Aspects:")
        self.features_label.setObjectName("Features_Label")
        self.features_label.move(10, 111)

        self.features_dropdown = QtWidgets.QComboBox(self.groupbox)
        self.features_dropdown.setObjectName("Features_Dropdown")
        self.features_dropdown.addItem("No Preference")
        self.features_dropdown.addItem("Forest")
        self.features_dropdown.addItem("Mountainous")
        self.features_dropdown.addItem("Lake/River")
        self.features_dropdown.addItem("Ocean")
        self.features_dropdown.addItem("Desert")
        self.features_dropdown.resize(130, 40)
        self.features_dropdown.move(70, 100)

        self.activities_label = QtWidgets.QLabel(self.groupbox)
        self.activities_label.setText("Activities:")
        self.activities_label.move(10, 161)

        self.activities_dropdown = QtWidgets.QComboBox(self.groupbox)
        self.activities_dropdown.setObjectName("Activities_Dropdown")
        self.activities_dropdown.addItem("No Preference")
        self.activities_dropdown.addItem("Bicycling")
        self.activities_dropdown.addItem("Boating")
        self.activities_dropdown.addItem("Diving")
        self.activities_dropdown.addItem("Camping")
        self.activities_dropdown.addItem("Climbing")
        self.activities_dropdown.addItem("Equestrianism")
        self.activities_dropdown.addItem("Fishing")
        self.activities_dropdown.addItem("Hiking")
        self.activities_dropdown.addItem("Hunting")
        self.activities_dropdown.addItem("Swimming")
        self.activities_dropdown.addItem("Skiing/Snowboarding")
        self.activities_dropdown.resize(130, 40)
        self.activities_dropdown.move(70, 150)

        self.wheelchair_checkbox = QtWidgets.QCheckBox(self.groupbox)
        self.wheelchair_checkbox.setText("Wheelchair Accessible")
        self.wheelchair_checkbox.setObjectName("Wheelchair_CheckBox")
        self.wheelchair_checkbox.move(10, 200)

        self.pet_checkbox = QtWidgets.QCheckBox(self.groupbox)
        self.pet_checkbox.setText("Pet Friendly")
        self.pet_checkbox.setObjectName("Pet_CheckBox")
        self.pet_checkbox.move(10, 230)

        self.map_container = QtWidgets.QGroupBox(self.dash_tab)
        self.map_container.setGeometry(QtCore.QRect(240, 40, 400, 300))
        self.maps_objects = self.create_QScrollArea("dash_tab", "maps_QScrollArea", "vertical_layout", 835, 85, 360, 595)
        self.maps = self.maps_objects[0]
        self.maps_layout = self.maps_objects[1]
        self.maps_scrollArea = self.maps_objects[2]

        self.populate_with_all()

    def connect_and_retrieve_all(self, db_file, table_name):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        cur = conn.cursor()
        SQLString = """SELECT * FROM sqlite_master"""
        cur.execute(SQLString)

        rows = cur.fetchall()
        for row in rows:
            print(row)

    def populate_with_all(self):
        self.connect_and_retrieve_all('new_file', 'PARK_NAMES')

    def create_QScrollArea(self, container, object_name, layout, x_coordinate, y_coordinate, fixed_width, min_length):
        self.scrollArea_object_container = QtWidgets.QWidget()
        if container == "dash_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.dash_tab)
        elif container == "dashboard_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.dashboard_tab)
        elif container == "maps_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.maps_tab)
        elif container == "points_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.points_tab)
        elif container == "rewards_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.rewards_tab)
        elif container == "admin_statistics_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.admin_statistics_tab)
        self.QScrollArea.setFixedWidth(fixed_width)
        self.QScrollArea.setFixedHeight(min_length)
        self.QScrollArea.move(x_coordinate, y_coordinate)
        self.QScrollArea.setWidgetResizable(True)
        self.QScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        if layout == "vertical_layout":
            self.scroll_vertical_layout = QtWidgets.QVBoxLayout(self.scrollArea_object_container)
            self.scrollArea_object_container.setLayout(self.scroll_vertical_layout)
            return [self.scrollArea_object_container, self.scroll_vertical_layout, self.QScrollArea]
        elif layout == "grid_layout":
            self.scroll_grid_layout = QtWidgets.QGridLayout(self.scrollArea_object_container)
            self.scrollArea_object_container.setLayout(self.scroll_grid_layout)
            self.QScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            return [self.scrollArea_object_container, self.scroll_grid_layout, self.QScrollArea]
