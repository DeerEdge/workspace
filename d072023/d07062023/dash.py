from PyQt5 import QtWidgets

class dash_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.dash_tab = tab
        self.control_dashboard()

    def control_dashboard(self):
        self.groupbox = QtWidgets.QGroupBox(self.dash_tab)
        self.groupbox.setObjectName("GroupBox_Dash")
        self.groupbox.resize(200, 540)
        self.groupbox.move(20, 40)

        self.natural_features_label = QtWidgets.QLabel(self.groupbox)
        self.natural_features_label.setObjectName("Natural_Features_Text_Label")
        self.natural_features_label.setText("Natural Features:")
        self.natural_features_label.move(20, 20)

        self.activities_label = QtWidgets.QLabel(self.groupbox)
        self.activities_label.setObjectName("Activities_Text_Label")
        self.activities_label.setText("Activities:")
        self.activities_label.move(23, 160)

        self.popularCheckBox = QtWidgets.QCheckBox(self.groupbox)
        self.popularCheckBox.setText("Popular")
        self.popularCheckBox.move(40, 290)

        self.national_forest = QtWidgets.QCheckBox("National Forest", self.groupbox)
        self.national_forest.move(40, 40)

        self.lakeshore = QtWidgets.QCheckBox("Lake/Lakeshore", self.groupbox)
        self.lakeshore.move(40, 60)

        self.ocean = QtWidgets.QCheckBox("Ocean", self.groupbox)
        self.ocean.move(40, 80)

        self.mountainous = QtWidgets.QCheckBox("Mountainous", self.groupbox)
        self.mountainous.move(40, 100)

        self.desert = QtWidgets.QCheckBox("Desert", self.groupbox)
        self.desert.move(40, 120)

        self.activity_hiking = QtWidgets.QCheckBox("Hiking", self.groupbox)
        self.activity_hiking.move(40, 180)

        self.activity_biking = QtWidgets.QCheckBox("Biking", self.groupbox)
        self.activity_biking.move(40, 200)

        self.activity_boating = QtWidgets.QCheckBox("Boating", self.groupbox)
        self.activity_boating.move(40, 220)

        self.scroll_area = QtWidgets.QScrollArea(self.dash_tab)
        self.scroll_area.setObjectName("Scroll_Area")
        self.scroll_area.resize(565, 500)
        self.scroll_area.move(250, 60)
        self.scroll_area.setWidgetResizable(True)

        self.container = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.container)
        lay = QtWidgets.QVBoxLayout(self.container)
        lay.setContentsMargins(10, 10, 0, 0)
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            text = letter * 100
            label = QtWidgets.QLabel(text)
            lay.addWidget(label)
        lay.addStretch()




print('hello')