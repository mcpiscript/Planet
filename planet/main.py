"""


Copyright (C) 2022  Alexey Pavlov

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


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Planet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Planet")

        self.setWindowIcon(QIcon("assets/logo128.png"))

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        tabs.addTab(self.play_tab(), "Play")
        tabs.addTab(self.features_tab(),  "Features")

        self.setCentralWidget(tabs)
        
        self.setGeometry(387,  221,  100,  100)

    def play_tab(self) -> QWidget:
        layout = QGridLayout()

        namelabel = QLabel("Planet Launcher")
        font = namelabel.font()
        font.setPointSize(30)
        namelabel.setFont(font)
        namelabel.setAlignment(Qt.AlignHCenter)

        usernamelabel = QLabel("Username")

        usernameedit = QLineEdit()
        usernameedit.setPlaceholderText("StevePi")

        distancelabel = QLabel("Render Distance")

        distancebox = QComboBox()
        distancebox.addItems(["Far", "Normal", "Short", "Tiny"])
        distancebox.setCurrentText("Short")

        profilelabel = QLabel("Profile")

        self.profilebox = QComboBox()
        self.profilebox.addItems(
            ["Vanilla MCPi", "Modded MCPi", "Modded MCPE", "Optimized MCPE", "Custom"]
        )
        self.profilebox.setCurrentText("Modded MCPE")
        
        
        self.showlauncher = QRadioButton("Hide Launcher")
        

        playbutton = QPushButton("Play")

        layout.addWidget(namelabel, 0, 0,  2, 6)

        layout.addWidget(usernamelabel, 2, 0)
        layout.addWidget(usernameedit, 2, 4, 1, 2)

        layout.addWidget(distancelabel, 3, 0)
        layout.addWidget(distancebox, 3, 4, 1, 2)

        layout.addWidget(profilelabel, 4, 0)
        layout.addWidget(self.profilebox, 4, 4, 1, 2)
        
        layout.addWidget(self.showlauncher,  5, 4,  1,  2)

        layout.addWidget(playbutton, 7, 5)

        widget = QWidget()

        widget.setLayout(layout)

        return widget
        
    
    def features_tab(self) -> QWidget:
        
        layout = QVBoxLayout()
        
        for feature in launcher.DEFAULT_FEATURES:
            checkbox = QCheckBox(feature)
            if launcher.DEFAULT_FEATURES[feature]:
                checkbox.setCheckState(Qt.Checked)
            else:
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
        fakelayout.addWidget(scroll,  0, 0)

        
        
        widget = QWidget()

        widget.setLayout(fakelayout)

        return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Planet()
    window.show()

    app.exec()
