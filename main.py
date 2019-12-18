# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Wed Dec  4 11:13:43 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

import time
import sys
import PIL
from PySide2 import QtCore, QtGui, QtWidgets
from mss import mss
from PIL import Image
from PIL import ImageGrab
from PIL import ImageFilter



# TODO : Set a path for the screenshots (hardcoded or user given?)
# TODO : Add a blur slider for the value + blur functionality
# TODO : Resize screen based on window would be nice
# TODO : Add About info



# About

Author = "Ioan-Andrei Nistor"
Contact = "ioan.andrei.nistor@gmail.com"
StyleSheetFile = "darkOrange.css"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("CompositionTool")
        MainWindow.resize(1280, 805)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowOpacity(1.0)
        with open(StyleSheetFile, "r") as sh:
            MainWindow.setStyleSheet(sh.read())

        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.ActivePhoto = ""
        self.firstScreen = "D:\\PublicRepo\\Screenshot1.png"
        self.secondScreen = "D:\\PublicRepo\\Screenshot2.png"

        self.themelocation = "D:\\PublicRepo\\darktheme.css"

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        with open(StyleSheetFile, "r") as sh:
            self.centralwidget.setStyleSheet(sh.read())

        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setEnabled(True)
        self.photo.setGeometry(QtCore.QRect(0, 33, 1280, 711))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap(""))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.tutorialLabel = QtWidgets.QLabel(self.centralwidget)
        self.tutorialLabel.setEnabled(True)
        self.tutorialLabel.setGeometry(QtCore.QRect(585, 10, 1081, 711))
        self.tutorialLabel.setText("Click screenshot to start !")
        self.tutorialLabel.setScaledContents(False)

        self.mirrorButton = QtWidgets.QPushButton(self.centralwidget)
        self.mirrorButton.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.mirrorButton.clicked.connect(self.mirrorImage)
        self.mirrorButton.setObjectName("mirrorButton")

        self.blurButton = QtWidgets.QPushButton(self.centralwidget)
        self.blurButton.setGeometry(QtCore.QRect(110, 0, 91, 31))
        self.blurButton.setObjectName("blurButton")
        self.blurButton.clicked.connect(self.blurImage)

        self.griddButton = QtWidgets.QPushButton(self.centralwidget)
        self.griddButton.setGeometry(QtCore.QRect(200, 0, 91, 31))
        self.griddButton.setObjectName("griddButton")
        self.griddButton.clicked.connect(self.gridDisplay)

        self.display1Button = QtWidgets.QPushButton(self.centralwidget)
        self.display1Button.setGeometry(QtCore.QRect(1130, 0, 71, 31))
        self.display1Button.setAutoDefault(True)
        self.display1Button.setDefault(True)
        self.display1Button.setObjectName("display1Button")
        self.display1Button.clicked.connect(self.changeDisplay1)

        self.display2Button = QtWidgets.QPushButton(self.centralwidget)
        self.display2Button.setGeometry(QtCore.QRect(1200, 0, 71, 31))
        self.display2Button.setObjectName("display2Button")
        self.display2Button.clicked.connect(self.changeDisplay2)

        self.photo_grid = QtWidgets.QLabel(self.centralwidget)
        self.photo_grid.setEnabled(True)
        self.photo_grid.setVisible(False)
        self.photo_grid.setGeometry(QtCore.QRect(0, 33, 1280, 711))
        self.photo_grid.setMouseTracking(False)
        self.photo_grid.setAutoFillBackground(False)
        self.photo_grid.setText("")
        self.photo_grid.setPixmap(QtGui.QPixmap("grid2.png"))
        self.photo_grid.setScaledContents(True)
        self.photo_grid.setObjectName("photo_grid")

        self.screenshotButton = QtWidgets.QPushButton(self.centralwidget)
        self.screenshotButton.setGeometry(QtCore.QRect(550, 0, 181, 31))
        self.screenshotButton.setObjectName("screenshotButton")
        self.screenshotButton.clicked.connect(self.grabScreenshot)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statustext = QtWidgets.QLabel(self.centralwidget)
        self.statustext.setText("")
        self.statustext.setScaledContents(True)
        self.statustext.setGeometry(5, 753, 500, 20)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        with open(StyleSheetFile, "r") as sh:
            self.menubar.setStyleSheet(sh.read())
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 30))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")


        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.menubar)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.menuFile.addAction(self.actionFile)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        # Disable all buttons first for better UX

        self.griddButton.setVisible(False)
        self.mirrorButton.setVisible(False)
        self.blurButton.setVisible(False)
        self.display1Button.setVisible(False)
        self.display2Button.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Composition Tool", None, -1))

        self.mirrorButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Mirror the image vertically", None, -1))
        self.mirrorButton.setText(QtWidgets.QApplication.translate("MainWindow", "Mirror", None, -1))

        self.blurButton.setText(QtWidgets.QApplication.translate("MainWindow", "Blur ", None, -1))
        self.blurButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Blur image", None,
                                                                    -1))
        self.griddButton.setText(QtWidgets.QApplication.translate("MainWindow", "Grid", None, -1))
        self.griddButton.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Displays the rule of third grid", None, -1))

        self.display1Button.setText(QtWidgets.QApplication.translate("MainWindow", "Display 1", None, -1))
        self.display1Button.setToolTip(QtWidgets.QApplication.translate("MainWindow", "View display 1 screenshot", None, -1))
        self.display2Button.setToolTip(QtWidgets.QApplication.translate("Mainwindow", "View display 2 screenshot", None, -1))
        self.display2Button.setText(QtWidgets.QApplication.translate("MainWindow", "Display 2", None, -1))

        self.screenshotButton.setText(QtWidgets.QApplication.translate("MainWindow", "Screenshot", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionFile.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.menuAbout.setTitle(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))



    def grabScreenshot(self):

        """
        Grabbing screenshots from both display 1 and 2
        """

        self.griddButton.setVisible(True)
        self.mirrorButton.setVisible(True)
        self.blurButton.setVisible(True)
        self.display1Button.setVisible(True)
        self.display2Button.setVisible(True)
        self.tutorialLabel.setVisible(False)

        print ("Grabbing Screenshot")
        print ("Showing Buttons now")

        with mss() as sct:
            monitor = sct.monitors[1]
            sct_img = sct.grab(monitor)
            # Convert to PIL/Pillow Image
            screenshots = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
            screenshots.save("Screenshot1.png", "PNG")

            # 2nd Display Screen shot

            monitor = sct.monitors[2]
            sct_img = sct.grab(monitor)
            # Convert to PIL/Pillow Image
            screenshots = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
            screenshots.save("Screenshot2.png", "PNG")
        self.photo.setPixmap(QtGui.QPixmap(self.firstScreen))
        self.statustext.setText("Added display 1 as work display for now")
        self.ActivePhoto = "Screenshot1.png" # Set Photo as display 1 so we dont get callstack error when mirrroring

    def blurImage(self):

        """
        Grabbing active photo and blurring it  + saving it on disk
        """

        print ("--Blurring Main Image--")
        self.blurButton.setDown(True)
        im = Image.open(self.ActivePhoto)
        blurred_image = im.filter(ImageFilter.GaussianBlur(1))
        blurred_image.save(self.ActivePhoto)
        self.photo.setPixmap(QtGui.QPixmap(self.ActivePhoto))


    def changeDisplay1(self):

        """
        Changing main display to Display 1
        """

        print ("--Changing to display 1--")
        self.display1Button.setDown(True)
        self.display2Button.setDown(False)
        self.statustext.setText("Changed to Display 1")
        self.photo.setPixmap(QtGui.QPixmap(self.firstScreen))
        self.ActivePhoto = self.firstScreen


    def changeDisplay2(self):

        """
        Changing main display to Display 2
        """

        print ("--Changing to display 2--")
        self.display1Button.setDown(False)
        self.display2Button.setDown(True)
        self.statustext.setText("Changed to display 2")
        self.photo.setPixmap(QtGui.QPixmap(self.secondScreen))
        self.ActivePhoto = self.secondScreen

    def mirrorImage(self):

        """
        Mirroring image and saving it on disk
        """

        im = Image.open(self.ActivePhoto)
        out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        out.save(self.ActivePhoto)
        self.photo.setPixmap(QtGui.QPixmap(self.ActivePhoto))
        print ("Flipped image")


    def gridDisplay(self):

        """
        Toggling grid display on/off and switching of the button UI
        """

        if self.griddButton.isCheckable():
            self.photo_grid.setVisible(False)
            self.griddButton.setCheckable(False)
            self.griddButton.setDown(False)
            self.statustext.setText("Hide Grid")
        else:
            self.griddButton.setCheckable(True)
            self.photo_grid.setVisible(True)
            self.griddButton.setDown(True)
            self.statustext.setText("Display Grid - Rule of thirds")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
