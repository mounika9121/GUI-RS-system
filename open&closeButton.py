"""
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction


class window(QMainWindow):
    def __init__(self):

        super().__init__()

    def createUI(self):


        self.setGeometry(500, 300, 300, 300)

        self.setWindowTitle("window")


        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)

        menubar = self.menuBar()
        fmenu = menubar.addMenu("File")
        fmenu.addAction(quit)

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

main = QApplication(sys.argv)
window = window()
window.createUI()
window.show()
sys.exit(main.exec_())

import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize

class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440, 240))
        self.setWindowTitle("PyQt5 Textarea example")

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("You can write text here.\n")
        self.b.move(10,10)
        self.b.resize(400,200)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        layout.addWidget(QPushButton('1'), 0, 0)
        layout.addWidget(QPushButton('2'), 0, 1)
        layout.addWidget(QPushButton('3'), 0, 2)
        layout.addWidget(QPushButton('4'), 1, 0)
        layout.addWidget(QPushButton('5'), 1, 1)
        layout.addWidget(QPushButton('6'), 1, 2)
        layout.addWidget(QPushButton('7'), 2, 0)
        layout.addWidget(QPushButton('8'), 2, 1)
        layout.addWidget(QPushButton('9'), 2, 2)

        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""
import sys
from tkinter import filedialog

from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QWidget

"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

"""
"""
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication)
from PyQt5.QtGui import QColor
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QGroupBox, QGridLayout)

class QGroupBoxTest(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    gb = QGroupBox()
    gb.setTitle('QGroupBox title')

    appLayout = QGridLayout()
    appLayout.addWidget(gb, 0, 0)
    self.setLayout(appLayout)

    self.setWindowTitle('QGroupBox test window')
    self.setGeometry(300, 300, 300, 200)

if __name__ == "__main__":

  import sys

  app = QApplication(sys.argv)
  test = QGroupBoxTest()
  test.show()

  sys.exit(app.exec_())

import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize

class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440, 240))
        self.setWindowTitle("PyQt5 Clipboard example")

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Use your mouse to copy text to the clipboard.\nText can be copied from any application.\n")
        self.b.move(10,10)
        self.b.resize(400,200)

        QApplication.clipboard().dataChanged.connect(self.clipboardChanged)

    # Get the system clipboard contents
    def clipboardChanged(self):
        text = QApplication.clipboard().text()
        print(text)
        self.b.insertPlainText(text + '\n')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )
from tkinter import *
root = Tk()

def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

pathlabel = Label(root)
pathlabel.pack()
"""
"""
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'MyApp'
        self.left, self.top, self.width, self.height = 10, 10, 800, 800
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Create textbox for index number 1
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Insert something:')
        self.nameLabel.move(20, 80)

        self.textbox_index1 = QLineEdit(self)
        self.textbox_index1.move(20, 100)
        self.textbox_index1.resize(280, 40)

        # Create a button in the window
        self.buttonC1 = QPushButton('Clear', self)
        self.buttonC1.move(300, 119)

        # connect buttons "CLEAR" to function
        self.buttonC1.clicked.connect(self.textbox_index1.clear)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()

        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
