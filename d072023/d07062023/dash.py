from PyQt5 import QtWidgets

class dash_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.dash_tab = tab
        self.control_dashboard()

    def control_dashboard(self):
        self.groupbox = QtWidgets.QGroupBox(self.dash_tab)
        self.groupbox.setObjectName("GroupBox_Dash")
        self.groupbox.resize(210, 540)
        self.groupbox.move(20, 40)

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








        self.scroll_area = QtWidgets.QScrollArea(self.dash_tab)
        self.scroll_area.setObjectName("Scroll_Area")
        self.scroll_area.resize(565, 500)
        self.scroll_area.move(250, 60)
        self.scroll_area.setWidgetResizable(True)

        container = QtWidgets.QWidget()
        self.scroll_area.setWidget(container)

        lay = QtWidgets.QVBoxLayout(container)
        lay.setContentsMargins(10, 10, 0, 0)
        for letter in "ABCDE":
            text = letter * 100
            label = QtWidgets.QLabel(text)
            lay.addWidget(label)
        lay.addStretch()

