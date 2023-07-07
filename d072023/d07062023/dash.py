from PyQt5 import QtWidgets

class dash_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.dash_tab = tab

    def control_dashboard(self):
        self.natural_features_label = QtWidgets.QLabel(self.dash_tab)
        self.natural_features_label.setObjectName("Natural_Features_Text_Label")
        self.natural_features_label.setText("Natural Features:")
        self.natural_features_label.move(40, 20)

        self.activities_label = QtWidgets.QLabel(self.dash_tab)
        self.activities_label.setObjectName("Activities_Text_Label")
        self.activities_label.setText("Activities:")
        self.activities_label.move(40, 160)

        self.popularCheckBox = QtWidgets.QCheckBox(self.dash_tab)
        self.popularCheckBox.setText("Popular")
        self.popularCheckBox.move(40, 290)

        self.national_forest = QtWidgets.QCheckBox("National Forest", self.dash_tab)
        self.national_forest.move(40, 40)

        self.lakeshore = QtWidgets.QCheckBox("Lake/Lakeshore", self.dash_tab)
        self.lakeshore.move(40, 60)

        self.ocean = QtWidgets.QCheckBox("Ocean", self.dash_tab)
        self.ocean.move(40, 80)

        self.mountainous = QtWidgets.QCheckBox("Mountainous", self.dash_tab)
        self.mountainous.move(40, 100)

        self.desert = QtWidgets.QCheckBox("Desert", self.dash_tab)
        self.desert.move(40, 120)

        self.activity_hiking = QtWidgets.QCheckBox("Hiking", self.dash_tab)
        self.activity_hiking.move(40, 180)

        self.activity_biking = QtWidgets.QCheckBox("Biking", self.dash_tab)
        self.activity_biking.move(40, 200)

        self.activity_boating = QtWidgets.QCheckBox("Boating", self.dash_tab)
        self.activity_boating.move(40, 220)

        self.groupbox = QtWidgets.QGroupBox(self.dash_tab)
        self.groupbox.setObjectName("GroupBox_Dash")
        self.groupbox.resize(200, 200)
        self.groupbox.move(20, 20)


