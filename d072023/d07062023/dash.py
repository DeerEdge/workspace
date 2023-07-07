from PyQt5 import QtWidgets

class dash_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.tab = tab

    def control_dashboard(self):
        self.natural_features_label = QtWidgets.QLabel(self.tab)
        self.natural_features_label.setText("Natural Features:")
        self.natural_features_label.move(20, 20)

        self.activities_label = QtWidgets.QLabel(self.tab)
        self.activities_label.setText("Activities:")
        self.activities_label.move(20, 40)

        self.popular_label = QtWidgets.QLabel(self.tab)
        self.popular_label.setText("Popular:")
        self.popular_label.move(20, 60)
