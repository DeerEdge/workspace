from PyQt5 import QtWidgets
from d072023.d07062023 import *
from d072023.d07072023 import *
from d072023.d07082023 import *
from d072023.d07092023 import *
from d072023.d07102023 import *

class ui_main_window(object):
    def setup_window(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(850, 650)

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.resize(850, 650)
        self.central_widget.setObjectName("display")

        self.tab_widget = QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.resize(850, 650)

        self.dash_tab = QtWidgets.QWidget()
        self.dash_tab.setObjectName("tab1")

        self.maps_tab = QtWidgets.QWidget()
        self.maps_tab.setObjectName("tab2")

        self.saved_tab = QtWidgets.QWidget()
        self.saved_tab.setObjectName("tab3")

        self.widget = QtWidgets.QWidget(self.dash_tab)

        self.tab_widget.addTab(self.dash_tab, "Dashboard")
        self.tab_widget.addTab(self.maps_tab, "Maps")
        self.tab_widget.addTab(self.saved_tab, "Saved")
        self.control_dashboard()

    def control_dashboard(self):
        self.natural_features_label = QtWidgets.QLabel(self.dash_tab)
        self.natural_features_label.setText("Natural Features:")
        self.natural_features_label.move(20, 20)

        self.activities_label = QtWidgets.QLabel(self.dash_tab)
        self.activities_label.setText("Activities:")
        self.activities_label.move(20, 40)

        self.popular_label = QtWidgets.QLabel(self.dash_tab)
        self.popular_label.setText("Popular:")
        self.popular_label.move(20, 60)








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = ui_main_window()
    ui.setup_window(main_window)
    main_window.show()
    sys.exit(app.exec_())