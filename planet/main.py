#!/usr/bin/python3
"""

Planet is an improved launcher for Minecraft Pi Edition: Reborn, inspired by gMCPIL, jMCPIL, MCPIL and MCPIL-R.

Copyright (C) 2022  Alexey Pavlov
Copyright (C) 2022  Red-Exe-Engineer
Copyright (C) 2022  Bigjango13

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""


# Built-in modules import

import sys
import os
import random
from datetime import date
import json
import pathlib
import gettext

LOCALE = os.getenv("LANG", "en")

# Define the path used for later
absolute_path = pathlib.Path(__file__).parent.absolute()

# ran only if it's in a deb file
if str(absolute_path).startswith("/usr/bin"):
    absolute_path = "/usr/lib/planet-launcher/"

# Make the launcher import local files
sys.path.append(absolute_path)
if os.path.exists("/usr/lib/planet-launcher/"):
    sys.path.append("/usr/lib/planet-launcher/")


try:
    _ = gettext.translation(
        "main", localedir=str(absolute_path) + "/assets/translations/", languages=[LOCALE]
    ).gettext
except:
    _ = gettext.translation(
        "main", localedir=str(absolute_path) + "/assets/translations/", languages=["en"]
    ).gettext

# Local imports
import launcher
from splashes import SPLASHES

# PyQt5 imports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *


# Additional imports
import qdarktheme  # Dark style for PyQt5
import pypresence  # Discord RPC
from PIL import Image
import darkdetect

import editpi as mcpiedit
import mcpit

# Load dark theme
dark_stylesheet = qdarktheme.load_stylesheet()

USER = os.getenv("USER")  # Get the username, used for later

# Create the mods directory if it does not exist
if not os.path.exists(f"/home/{USER}/.planet-launcher/mods"):
    os.makedirs(f"/home/{USER}/.planet-launcher/mods")

if not os.path.exists(f"/home/{USER}/.minecraft-pi/overrides/images/mob/"):
    os.makedirs(f"/home/{USER}/.minecraft-pi/overrides/images/mob/")

# if os.path.exists(f"/home/{USER}/.gmcpil.json"):
#    with open(f"/home/{USER}/.gmcpil.json") as f:
#        DEFAULT_FEATURES = json.loads(f.read())["features"]
# else:
# TODO: Add a tab with a button to import features from gMCPIL

if darkdetect.isDark():
    theme = "dark"
else:
    theme = "light"


class ConfigPluto(QDialog):
    """Startup configurator for Planet. Based on QDialog."""

    def __init__(self):
        super().__init__()
        # Remove the window bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        layout = QVBoxLayout()  # Real layout used by the widger
        titlelayout = QGridLayout()  # Layout for the title

        # Load the logo pixmap
        logopixmap = QPixmap(f"{absolute_path}/assets/img/full/logo512.png").scaled(
            100, 100, Qt.KeepAspectRatio
        )

        # Create the name label
        namelabel = QLabel("Pluto Wizard")

        logolabel = QLabel()  # label used for the logo
        logolabel.setPixmap(logopixmap)  # Load the pixmap into the label
        logolabel.setAlignment(Qt.AlignRight)  # Align right

        font = namelabel.font()  # This font is just used to set the size
        font.setPointSize(30)
        namelabel.setFont(font)  # Apply the font to the label
        namelabel.setAlignment(Qt.AlignLeft)  # Align left

        titlelayout.addWidget(logolabel, 0, 0)  # Add the logo into the layout
        titlelayout.addWidget(namelabel, 0, 1)  # Add the name into the layout

        titlewidget = QWidget()  # Fake widget that takes the title layout
        titlewidget.setLayout(titlelayout)  # Set the layout

        # Label with information
        info_label = QLabel(
            _(
                'Please select the executable you downloaded.\nIf you installed a DEB, please select the "Link" option'
            )
        )

        self.executable_btn = QPushButton(_("Select executable"))  # Button for AppImage
        self.executable_btn.clicked.connect(
            self.get_appimage
        )  # Connect to the function

        self.premade_btn = QPushButton(
            _("Link /usr/bin/minecraft-pi-reborn-client")
        )  # Button for Pre-installed debs
        self.premade_btn.clicked.connect(self.link_appimage)  # Connect to the function

        #self.flatpak_btn = QPushButton(_("Link flatpak"))  # Button for linking flatpak
        #self.flatpak_btn.clicked.connect(self.link_flatpak)  # Connect to the function

        # Adding things to widgets
        layout.addWidget(titlewidget)
        layout.addWidget(info_label)
        layout.addWidget(self.executable_btn)
        layout.addWidget(self.premade_btn)
        #layout.addWidget(self.flatpak_btn)

        self.setLayout(layout)

    # Functions below are related to window movement

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.moveFlag = False
        self.setCursor(Qt.ArrowCursor)

    def get_appimage(self):
        self.hide()  # Hide the dialog
        # Open the file dialog
        self.filename = QFileDialog.getOpenFileName(
            self,
            _("Select executable"),
            "/",
            "Executable files (*.AppImage *.bin *.sh *)",
        )

    def link_appimage(self):
        self.hide()  # hide the dialog
        # Link the executable with the AppImage
        os.symlink(
            "/usr/bin/minecraft-pi-reborn-client",
            f"/home/{USER}/.planet-launcher/minecraft.AppImage",
        )
        self.filename = list()  # Make a fake list
        self.filename.append(
            False
        )  # Append False to the fake list. See end of file for more info

    def link_flatpak(self):
        script_text = (
            "#!/bin/bash\nflatpak run com.thebrokenrail.MCPIReborn $1"
        )  # Script contents
        with open(
            f"/home/{USER}/.planet-launcher/minecraft.AppImage", "w"
        ) as file:  # Open the file
            file.write(script_text)  # Write the script text

        self.filename = list()  # Fake list. See function above for more info
        self.filename.append(False)


class Planet(QMainWindow):
    """Main window class. Contains tabs and everything"""

    launchfeatures = dict()  # Dictionary for custom features
    env = os.environ.copy()  # ENV variables

    def __init__(self):
        super().__init__()
        self.center()

        try:
            RPC = pypresence.Presence(
                787496148763541505
            )  # Try to initialize pypresence and find Discord
            RPC.connect()  # Connect to Discord
            # Set the RPC Status
            RPC.update(
                state=_("Launched with Planet Launcher"),
                details=_("Minecraft Pi Edition: Reborn"),
                large_image=random.choice(
                    ["revival", "logo"]
                ),  # Randomly select the logo
                small_image=random.choice(
                    ["heart", "portal", "multiplayer", "logo", "revival"]
                ),  # Randomly select the tiny image
            )
        except:
            print(
                _("Unable to initalize Discord RPC. Skipping.")
            )  # If it fails, e.g Discord is not found, skip. This doesn't matter much.

        if not os.path.exists(
            f"/home/{USER}/.planet-launcher/config.json"
        ):  # Config file does not exist.

            # Set the configuration variable
            self.conf = {
                "username": "StevePi",
                "options": launcher.get_features_dict(
                    f"/home/{USER}/.planet-launcher/minecraft.AppImage"
                ),
                "hidelauncher": True,
                "profile": "Modded MCPE",
                "render_distance": "Short",
                "theme": theme,
                "discord_rpc": True,
                "version": "extended_2.3.2",
            }

            with open(
                f"/home/{USER}/.planet-launcher/config.json", "w"
            ) as file:  # Write it to the configuration file
                file.write(json.dumps(self.conf))
        else:
            with open(
                f"/home/{USER}/.planet-launcher/config.json"
            ) as file:  # Else, it exists: Read from it.
                self.conf = json.loads(file.read())

        self.setWindowTitle(_("Planet"))  # Set the window title

        self.setWindowIcon(
            QIcon(f"{absolute_path}/assets/img/full/logo512.png")
        )  # Set the window icon

        self.widget = QWidget()
        self.layout = QStackedLayout()

        tabs = QTabWidget()  # Create the tabs
        tabs.setTabPosition(QTabWidget.North)  # Select the tab position.
        tabs.setMovable(True)  # Allow tab movement.

        # Tab part. Please check every function for more info
        play_tab = tabs.addTab(self.play_tab(), _("Play"))  # Add the play tab
        tabs.setTabIcon(
            play_tab, QIcon(f"{absolute_path}/assets/img/full/logo512.png")
        )  # Set the icon for the tab
        features_tab = tabs.addTab(
            self.features_tab(), _("Features")
        )  # Add the features tab
        tabs.setTabIcon(
            features_tab, QIcon(f"{absolute_path}/assets/img/full/heart512.png")
        )  # set the icon for the tab
        servers_tab = tabs.addTab(self.servers_tab(), _("Servers"))  # Servers tab
        tabs.setTabIcon(
            servers_tab, QIcon(f"{absolute_path}/assets/img/full/portal512.png")
        )  # Set the icon
        # mods_tab = tabs.addTab(self.custom_mods_tab(), "Mods")
        # tabs.setTabIcon(mods_tab, QIcon(f"{absolute_path}/assets/portal512.png"))
        settings_tab = tabs.addTab(self.settings_tab(), _("Settings"))  # Changelog tab
        tabs.setTabIcon(
            settings_tab, QIcon(f"{absolute_path}/assets/img/full/wrench512.png")
        )

        self.layout.addWidget(tabs)

        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)  # Set the central widget to the tabs

        self.setGeometry(
            600, 900, 200, 200
        )  # Set the window geometry. Doesn't do much effect from my observations, unfortunartely

        self.usernameedit.setText(
            self.conf["username"]
        )  # Set the username text to the configuration's variant
        self.profilebox.setCurrentText(self.conf["profile"])  # See top comment
        self.distancebox.setCurrentText(
            self.conf["render_distance"]
        )  # See top comments

        for feature in self.features:
            try:
                if self.conf["options"][feature]:
                    self.features[feature].setCheckState(
                        Qt.Checked
                    )  # Set to checked if the configuration has it to true
                else:
                    self.features[feature].setCheckState(
                        Qt.Unchecked
                    )  # Else, set it unchecked
            except KeyError:  # May happen on downgrades or upgrades of the Reborn version
                pass

        # Hide launcher/Show it depending on the config
        self.showlauncher.setChecked(self.conf["hidelauncher"])

        # Set the features
        self.set_features()

    def play_tab(self) -> QWidget:
        """The main tab, with the main functionality"""
        layout = QGridLayout()  # The layout

        titlelayout = QGridLayout()  # The layout for the title

        # Load the logo pixmap
        logopixmap = QPixmap(f"{absolute_path}/assets/img/full/logo512.png").scaled(
            100, 100, Qt.KeepAspectRatio  # Scale it, but keep the aspect ratio
        )

        logolabel = QLabel()  # Label for the pixmap
        logolabel.setPixmap(logopixmap)  # apply the pixmap onto the label
        logolabel.setAlignment(Qt.AlignRight)  # Align the label

        namelabel = QLabel()  # Label for the title

        # Ester eggs
        if date.today().month == 4 and date.today().day == 1:
            namelabel.setText(
                _("Banana Launcher")
            )  # If the date is april fish, show the banana easter egg
        else:
            if random.randint(1, 100) == 1:
                namelabel.setText(_("Pluto Launcher"))  # a 1/100, Pluto launcher
            else:
                namelabel.setText(_("Planet Launcher"))  # Else, just set it normal

        font = namelabel.font()  # Font used
        font.setPointSize(30)  # Set the font size
        namelabel.setFont(font)  # Aplly the font onto the label
        namelabel.setAlignment(Qt.AlignLeft)  # Align the label

        splashlabel = QLabel(
            f'<font color="gold">{random.choice(SPLASHES)}</font>'
        )  # Label for splash. Uses QSS for color
        splashlabel.adjustSize()  # Adjust the size just in case
        splashlabel.setAlignment(Qt.AlignHCenter)  # Align the label

        usernamelabel = QLabel(
            _("Username")
        )  # Label that is used to direct the line edit

        self.usernameedit = QLineEdit()  # Line Edit for username
        self.usernameedit.setPlaceholderText(_("StevePi"))  # Set ghost value

        distancelabel = QLabel(
            _("Render Distance")
        )  # Label that is used to direct the combo box

        self.distancebox = QComboBox()
        self.distancebox.addItems(["Far", "Normal", "Short", "Tiny"])  # Set the values
        self.distancebox.setCurrentText("Short")  # Set the default option

        profilelabel = QLabel(
            _("Profile")
        )  # Label that is used to direct the combo box

        self.profilebox = QComboBox()
        self.profilebox.addItems(
            [
                "Vanilla MCPi",
                "Modded MCPi",
                "Modded MCPE",
                "Optimized MCPE",
                "Custom",
            ]  # Add  items into the combo box
        )
        self.profilebox.setCurrentText("Modded MCPE")  # Set the current selection

        self.showlauncher = QRadioButton(
            _("Hide Launcher")
        )  # RadioButton used for hiding the launcher

        self.versionbox = QComboBox()

        # versions = json.loads(web.get_versions())["versions"]

        # version_list = list()

        # for version in versions:
        #   version_list.append(versions[version])

        # version_name_list = list()

        # for version in version_list:
        # version_name_list.append(version["name"])

        # self.versionbox.addItems(version_name_list)  # Set the values
        # self.versionbox.setCurrentText("Short")  # Set the default option

        self.playbutton = QPushButton("Play")  # The most powerful button

        self.playbutton.setCheckable(True)  # Allow checking it
        self.playbutton.clicked.connect(
            self.launch
        )  # Connect it to the executing function

        # Add widgets into the title layout
        titlelayout.addWidget(logolabel, 0, 0)
        titlelayout.addWidget(namelabel, 0, 1)

        titlewidget = QWidget()
        titlewidget.setLayout(titlelayout)  # Apply the layout onto a fake widget

        layout.addWidget(
            titlewidget, 0, 0, 2, 5
        )  # Apply that widget onto the main layout

        # All other widgets are applied here
        layout.addWidget(splashlabel, 2, 0, 1, 6)

        layout.addWidget(usernamelabel, 3, 0)
        layout.addWidget(self.usernameedit, 3, 4, 1, 2)

        layout.addWidget(distancelabel, 4, 0)
        layout.addWidget(self.distancebox, 4, 4, 1, 2)

        layout.addWidget(profilelabel, 5, 0)
        layout.addWidget(self.profilebox, 5, 4, 1, 2)

        layout.addWidget(self.showlauncher, 6, 4)

        # layout.addWidget(self.versionbox, 8, 0, 1, 3)

        layout.addWidget(self.playbutton, 8, 4, 1, 2)

        widget = QWidget()

        widget.setLayout(layout)  # Apply the layout onto the main widget

        return widget

    def features_tab(self) -> QWidget:

        layout = QVBoxLayout()

        self.features = dict()  # Dictionary used for storing checkboxes for features
        default_features = launcher.get_features_dict(  # Get default feature list
            f"/home/{USER}/.planet-launcher/minecraft.AppImage"
        )

        for feature in default_features:  # Loop in default features
            checkbox = QCheckBox(feature)  # For each feature, create a checkbox
            # TODO: Fix the error if newer features are added here, or check for them in self.conf
            if default_features[feature]:  # Check if it's checked. If so, check it
                checkbox.setCheckState(Qt.Checked)
            else:
                checkbox.setCheckState(Qt.Unchecked)

            checkbox.clicked.connect(self.set_features)  # Connect saving function

            self.features[feature] = checkbox  # Add the checkbox into the list

            layout.addWidget(checkbox)  # Add the checkbox into the layout

        fakewidget = QWidget()  # Create a fake widget to apply the layout on
        fakewidget.setLayout(layout)  # Apply the layoutonto

        scroll = QScrollArea()  # Add a scoll area

        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOn
        )  # Shoe the vertical scroll bar
        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )  # Hide the horizontak scroll bar
        scroll.setWidgetResizable(
            True
        )  # Allow window resizing and fix itt with the scrollbar
        scroll.setWidget(fakewidget)  # Set the main widget into the scrollbar

        fakelayout = QGridLayout()
        fakelayout.addWidget(scroll, 0, 0)  # Apply the scrollbar onto the layout

        widget = QWidget()

        widget.setLayout(fakelayout)

        return widget

    def servers_tab(self) -> QWidget:
        widget = QWidget()
        layout = QGridLayout()

        self.serversedit = QTextEdit()  # Create a text editing area

        if not os.path.exists(f"/home/{USER}/.minecraft-pi/servers.txt"):
            with open(f"/home/{USER}/.minecraft-pi/servers.txt", 'w') as servers:
                servers.write("pbptanarchy.tk")

        self.serversedit.textChanged.connect(
            self.save_servers
        )  # Connect on change to the save function
        with open(f"/home/{USER}/.minecraft-pi/servers.txt", 'r') as servers:
            self.serversedit.setPlainText(
                servers.read()
            )  # Set the text of the text editing area

        infolabel = QLabel(  # Label with information about the server format
            _(
                'Servers are stored in the format of <font color="gold">IP: </font><font color="blue">Port</font>'
            )
        )

        layout.addWidget(self.serversedit, 0, 0)  # Add the widgets
        layout.addWidget(infolabel, 6, 0)

        widget.setLayout(layout)
        return widget

    def custom_mods_tab(self) -> QWidget:
        layout = QVBoxLayout()

        for mod in os.listdir(
            f"/home/{USER}/.planet-launcher/mods/"
        ):  # Loop in every mod in the mod directory
            checkbox = QCheckBox(mod)  # Create a checkbox with the mod name
            checkbox.setCheckState(Qt.Unchecked)  # Set it to unchecked

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

    def changelog_widget(self):
        web_engine = QWebView()  # Create a webview object
        web_engine.load(
            QUrl().fromLocalFile(f"{absolute_path}/assets/misc/changelog.html")
        )  # Load the local file
        # TODO: Use two different tabs for the webview

        return web_engine

    def settings_widget(self):
        widget = QWidget()

        layout = QGridLayout()

        skin_label = QLabel(_("Set the skin"))

        self.skin_button = QPushButton(_("Select Skin"))
        self.skin_button.clicked.connect(self.select_skin)

        config_label = QLabel(_("Reset config"))

        self.delete_config_button = QPushButton(_("Delete config"))
        self.delete_config_button.clicked.connect(self.delete_config)

        appimage_label = QLabel(_("Delete executable"))

        self.delete_appimage_button = QPushButton(_("Delete"))
        self.delete_appimage_button.clicked.connect(self.delete_appimage)
        
        mcpit_install_label = QLabel(_("Install texture pack"))
     
        self.import_mcpit_button = QPushButton(_("Select file"))
        self.import_mcpit_button.clicked.connect(self.install_texture_pack)
        
        mcpit_delete_label = QLabel(_("Delete texture pack"))
        
        self.delete_mcpit_button = QPushButton(_("Delete"))
        self.delete_mcpit_button.clicked.connect(mcpit.erase_pack)

        layout.addWidget(skin_label, 0, 0)
        layout.addWidget(self.skin_button, 0, 1)

        layout.addWidget(config_label, 1, 0)
        layout.addWidget(self.delete_config_button, 1, 1)

        layout.addWidget(appimage_label, 2, 0)
        layout.addWidget(self.delete_appimage_button, 2, 1)
        
        layout.addWidget(mcpit_install_label)
        layout.addWidget(self.import_mcpit_button,  3, 1)
        
        layout.addWidget(mcpit_delete_label)
        layout.addWidget(self.delete_mcpit_button,  4, 1)

        widget.setLayout(layout)

        return widget

    def settings_tab(self):
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.South)

        settings_tab = tabs.addTab(self.settings_widget(), _("General"))
        changelog_tab = tabs.addTab(self.changelog_widget(), _("Changelog"))
        editor_tab = tabs.addTab(mcpiedit.NBTEditor(), _("MCPIEdit"))

        tabs.setTabIcon(
            settings_tab, QIcon(f"{absolute_path}/assets/img/full/wrench512.png")
        )  # Set the icon

        tabs.setTabIcon(
            changelog_tab, QIcon(f"{absolute_path}/assets/img/full/git.png")
        )  # Set the icon

        tabs.setTabIcon(
            editor_tab, QIcon(f"{absolute_path}/assets/img/full/mcpiedit.png")
        )  # Set the icon

        return tabs

    def import_gmcpil(self):
        with open(f"/home/{USER}/.gmcpil.json") as f:
            gmcpil_features = json.loads(f.read())["features"]
            for feature in gmcpil_features:
                try:
                    if gmcpil_features[feature]:
                        self.features[feature].setCheckState(
                            Qt.Checked
                        )  # Set to checked if the configuration has it to true
                        self.conf["options"][feature] = True
                    else:
                        self.features[feature].setCheckState(
                            Qt.Unchecked
                        )  # Else, set it unchecked
                        self.conf["options"][feature] = False
                except KeyError:  # May happen on downgrades or upgrades of the Reborn version
                    pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.movePosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.moveFlag:
            self.move(event.globalPos() - self.movePosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.moveFlag = False
        self.setCursor(Qt.ArrowCursor)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_features(self):
        for feature in self.features:
            if self.features[feature].isChecked():
                self.launchfeatures[feature] = True
            else:
                self.launchfeatures[feature] = False

    def save_profile(self):
        self.set_features()
        self.conf["username"] = self.usernameedit.text()
        self.conf["options"] = self.launchfeatures
        self.conf["render_distance"] = self.distancebox.currentText()
        self.conf["profile"] = self.profilebox.currentText()
        self.conf["hidelauncher"] = self.showlauncher.isChecked()

        with open(f"/home/{USER}/.planet-launcher/config.json", "w") as file:
            file.write(json.dumps(self.conf))

    def save_servers(self):
        with open(f"/home/{USER}/.minecraft-pi/servers.txt", "w") as file:
            file.write(self.serversedit.toPlainText())

    def select_skin(self):
        filename = QFileDialog.getOpenFileName(
            self, _("Select skin file"), "/", "PNG files (*.png)"
        )
        if not filename == "":
            with open(
                f"/home/{USER}/.minecraft-pi/overrides/images/mob/char.png", "w"
            ) as skin:
                skin.write("quick placeholder")

            Image.open(filename[0]).crop((0, 0, 64, 32)).convert("RGBA").save(
                f"/home/{USER}/.minecraft-pi/overrides/images/mob/char.png"
            )
            
    def install_texture_pack(self):
        pack = QFileDialog.getOpenFileName(
            self, _("Select pack file"), "/", "mcpit files (*.mcpit);;PePack files (*.zip *.pepack)"
        )
        if pack[1] == "mcpit files (*.mcpit)":
            mcpit.mcpit_install(pack[0],  False)
        else:
            mcpit.pepack_install(pack[0])
        

    def delete_config(self):
        dialog = QMessageBox()
        dialog.setWindowTitle(_("Are you sure you want to reset?"))
        dialog.setText(
            _(
                "Are you sure you want to delete the config? This action is unrecoverable."
            )
        )
        dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Abort)
        dialog.setIcon(QMessageBox.Warning)

        button = dialog.exec()

        if button == QMessageBox.Ok:

            os.remove(f"/home/{USER}/.planet-launcher/config.json")
            self.hide()
            sys.exit()

    def delete_appimage(self):
        dialog = QMessageBox()
        dialog.setWindowTitle(_("Are you sure you want to reset?"))
        dialog.setText(
            _(
                "Are you sure you want to delete the AppImage? This action is unrecoverable."
            )
        )
        dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Abort)
        dialog.setIcon(QMessageBox.Warning)

        button = dialog.exec()

        if button == QMessageBox.Ok:

            os.remove(f"/home/{USER}/.planet-launcher/minecraft.AppImage")
            self.hide()
            sys.exit()

    def launch(self):
        self.save_profile()

        if self.profilebox.currentText().lower() == "vanilla mcpi":
            self.launchfeatures = launcher.get_features_dict(
                f"/home/{USER}/.planet-launcher/minecraft.AppImage"
            )
            for feature in self.launchfeatures:
                self.launchfeatures[feature] = False
        elif self.profilebox.currentText().lower() == "modded mcpi":
            self.launchfeatures = launcher.get_features_dict(
                f"/home/{USER}/.planet-launcher/minecraft.AppImage"
            )
            self.launchfeatures["Touch GUI"] = False
        elif self.profilebox.currentText().lower() == "modded mcpe":
            self.launchfeatures = launcher.get_features_dict(
                f"/home/{USER}/.planet-launcher/minecraft.AppImage"
            )
        elif self.profilebox.currentText().lower() == "optimized mcpe":
            self.launchfeatures = launcher.get_features_dict(
                f"/home/{USER}/.planet-launcher/minecraft.AppImage"
            )
            self.launchfeatures["Fancy Graphics"] = False
            self.launchfeatures["Smooth Lightning"] = False
            self.launchfeatures["Animated Water"] = False
            self.launchfeatures['Disable "gui_blocks" Atlas'] = False

        self.env = launcher.set_username(self.env, self.usernameedit.text())
        self.env = launcher.set_options(self.env, self.launchfeatures)
        self.env = launcher.set_render_distance(
            self.env, self.distancebox.currentText()
        )

        if self.showlauncher.isChecked() == True:
            self.hide()
            launcher.run(
                self.env, f"/home/{USER}/.planet-launcher/minecraft.AppImage"
            ).wait()
        else:
            launcher.run(self.env, f"/home/{USER}/.planet-launcher/minecraft.AppImage")
        self.show()


if __name__ == "__main__":

    apppath = str()

    app = QApplication(sys.argv)
    if os.path.exists(f"/home/{USER}/.planet-launcher/config.json"):
        with open(f"/home/{USER}/.planet-launcher/config.json") as file:
            app.setPalette(qdarktheme.load_palette(json.loads(file.read())["theme"]))
    else:
        app.setPalette(qdarktheme.load_palette(theme))

    if not os.path.exists(f"/home/{USER}/.planet-launcher/minecraft.AppImage"):
        pluto = ConfigPluto()
        pluto.show()
        pluto.exec()
        if pluto.filename[0] == "":
            sys.exit(-1)
        elif pluto.filename[0] == False:
            print(_("Using /usr/bin as an executable."))
        else:
            with open(pluto.filename[0], "rb") as appimage:
                with open(
                    f"/home/{USER}/.planet-launcher/minecraft.AppImage", "wb"
                ) as out:
                    out.write(appimage.read())
                    os.chmod(f"/home/{USER}/.planet-launcher/minecraft.AppImage", 0o755)

    window = Planet()
    window.show()

    app.exec()
