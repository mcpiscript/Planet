"""


Copyright (C) 2022  Alexey Pavlov
Copyright (C) 2022  Red-Exe-Engineer

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""


import sys
import launcher
from splashes import SPLASHES
import os
import random
from datetime import date
import json
import pathlib


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *

import qdarktheme


dark_stylesheet = qdarktheme.load_stylesheet()

USER = os.getenv("USER")

if not os.path.exists(f"/home/{USER}/.planet-launcher/mods"):
    os.makedirs(f"/home/{USER}/.planet-launcher/mods")

# if os.path.exists(f"/home/{USER}/.gmcpil.json"):
#    with open(f"/home/{USER}/.gmcpil.json") as f:
#        DEFAULT_FEATURES = json.loads(f.read())["features"]
# else:
# TODO: Add a tab with a button to import features from gMCPIL
DEFAULT_FEATURES = launcher.get_features_dict()


class Planet(QMainWindow):

    launchfeatures = dict()
    env = os.environ.copy()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Planet")

        self.setWindowIcon(QIcon("assets/logo512.png"))

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        play_tab = tabs.addTab(self.play_tab(), "Play")
        tabs.setTabIcon(play_tab, QIcon("assets/logo512.png"))
        features_tab = tabs.addTab(self.features_tab(), "Features")
        tabs.setTabIcon(features_tab, QIcon("assets/heart512.png"))
        mods_tab = tabs.addTab(self.custom_mods_tab(), "Mods")
        tabs.setTabIcon(mods_tab, QIcon("assets/portal512.png"))
        changelog_tab = tabs.addTab(self.changelog_tab(), "Changelog")
        tabs.setTabIcon(changelog_tab, QIcon("assets/pi512.png"))

        self.setCentralWidget(tabs)

        self.setGeometry(600, 800, 200, 200)

        self.set_features()

    def play_tab(self) -> QWidget:
        layout = QGridLayout()

        titlelayout = QGridLayout()

        logopixmap = QPixmap("assets/logo512.png").scaled(100, 100, Qt.KeepAspectRatio)

        logolabel = QLabel()
        logolabel.setPixmap(logopixmap)
        logolabel.setAlignment(Qt.AlignRight)

        namelabel = QLabel()

        if date.today().month == 4 and date.today().day == 1:
            namelabel.setText("Banana Launcher")
        else:
            if random.randint(1, 100) == 1:
                namelabel.setText("Pluto Launcher")
            else:
                namelabel.setText("Planet Launcher")

        font = namelabel.font()
        font.setPointSize(30)
        namelabel.setFont(font)
        namelabel.setAlignment(Qt.AlignLeft)

        splashlabel = QLabel(f'<font color="gold">{random.choice(SPLASHES)}</font>')
        splashlabel.adjustSize()
        splashlabel.setAlignment(Qt.AlignHCenter)

        usernamelabel = QLabel("Username")

        self.usernameedit = QLineEdit()
        self.usernameedit.setPlaceholderText("StevePi")

        distancelabel = QLabel("Render Distance")

        self.distancebox = QComboBox()
        self.distancebox.addItems(["Far", "Normal", "Short", "Tiny"])
        self.distancebox.setCurrentText("Short")

        profilelabel = QLabel("Profile")

        self.profilebox = QComboBox()
        self.profilebox.addItems(
            ["Vanilla MCPi", "Modded MCPi", "Modded MCPE", "Optimized MCPE", "Custom"]
        )
        self.profilebox.setCurrentText("Modded MCPE")

        self.showlauncher = QRadioButton("Hide Launcher")

        self.playbutton = QPushButton("Play")

        self.playbutton.setCheckable(True)
        self.playbutton.clicked.connect(self.launch)

        titlelayout.addWidget(logolabel, 0, 0)
        titlelayout.addWidget(namelabel, 0, 1)

        titlewidget = QWidget()
        titlewidget.setLayout(titlelayout)

        layout.addWidget(titlewidget, 0, 0, 2, 5)

        layout.addWidget(splashlabel, 2, 0, 1, 6)

        layout.addWidget(usernamelabel, 3, 0)
        layout.addWidget(self.usernameedit, 3, 4, 1, 2)

        layout.addWidget(distancelabel, 4, 0)
        layout.addWidget(self.distancebox, 4, 4, 1, 2)

        layout.addWidget(profilelabel, 5, 0)
        layout.addWidget(self.profilebox, 5, 4, 1, 2)

        layout.addWidget(self.showlauncher, 6, 4, 1, 2)

        layout.addWidget(self.playbutton, 8, 5)

        widget = QWidget()

        widget.setLayout(layout)

        return widget

    def features_tab(self) -> QWidget:

        layout = QVBoxLayout()

        self.features = dict()

        for feature in DEFAULT_FEATURES:
            checkbox = QCheckBox(feature)
            if DEFAULT_FEATURES[feature]:
                checkbox.setCheckState(Qt.Checked)
            else:
                checkbox.setCheckState(Qt.Unchecked)

            checkbox.clicked.connect(self.set_features)

            self.features[feature] = checkbox

            layout.addWidget(checkbox)

        fakewidget = QWidget()
        fakewidget.setLayout(layout)

        scroll = QScrollArea()

        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(fakewidget)

        fakelayout = QGridLayout()
        fakelayout.addWidget(scroll, 0, 0)

        widget = QWidget()

        widget.setLayout(fakelayout)

        return widget

    def custom_mods_tab(self) -> QWidget:
        layout = QVBoxLayout()

        for mod in os.listdir(f"/home/{USER}/.planet-launcher/mods/"):
            checkbox = QCheckBox(mod)
            checkbox.setCheckState(Qt.Unchecked)

            layout.addWidget(checkbox)

        fakewidget = QWidget()
        fakewidget.setLayout(layout)

        scroll = QScrollArea()

        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(fakewidget)

        fakelayout = QGridLayout()
        fakelayout.addWidget(scroll, 0, 0)

        widget = QWidget()

        widget.setLayout(fakelayout)

        return widget

    def changelog_tab(self):
        web = QWebView()
        web.load(
            QUrl().fromLocalFile(
                f"{pathlib.Path(__file__).parent.absolute()}/assets/changelog.html"
            )
        )
        print(f"{pathlib.Path(__file__).parent.absolute()}/assets/changelog.html")
        return web

    def set_features(self):
        for feature in self.features:
            if self.features[feature].isChecked():
                self.launchfeatures[feature] = True
            else:
                self.launchfeatures[feature] = False

    def launch(self):
        self.env = launcher.set_username(self.env, self.usernameedit.text())
        self.env = launcher.set_options(self.env, self.launchfeatures)
        self.env = launcher.set_render_distance(
            self.env, self.distancebox.currentText()
        )

        print(self.env)
        self.hide()
        launcher.run(self.env)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setPalette(qdarktheme.load_palette("dark"))

    window = Planet()
    window.show()

    app.exec()
