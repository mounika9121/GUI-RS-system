"""
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QAction, QPlainTextEdit, QGridLayout
from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic.properties import QtWidgets, QtCore
from dependencies.ssh_connect import SSHInterface


class App(QDialog):

    def __init__(self):

        super().__init__()
        self.title = 'SSHInterface'
        self.left = 150
        self.top = 150
        self.width = 400
        self.height = 450
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.qwidget = QWidget()

        # Create textboxs
        self.ServerInfoBox = QGroupBox(self)
        self.ServerInfoBox.setTitle('Server Info')
        self.lineEditHostName = QLineEdit(self)
        # self.lineEditPort = QLineEdit(self)

        # horizontal layout
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.lineEditHostName)
        # self.horizontal_layout.addWidget(self.lineEditPort)
        # self.horizontal_layout_1.addWidget(self.textbox4)
        self.horizontal_layout.addWidget(self.ServerInfoBox)

        # Vertical layout
        self.UserInfoBox = QGroupBox(self)
        self.UserInfoBox.setTitle('User Info')
        self.CommandBox = QGroupBox(self)
        self.CommandBox.setTitle('Run the command')
        self.lineEditUsername = QLineEdit(self)
        self.lineEditPassword = QLineEdit(self)
        self.lineEditCommand = QLineEdit(self)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.lineEditUsername)
        self.vertical_layout.addWidget(self.lineEditPassword)
        self.vertical_layout.addWidget(self.lineEditCommand)
        self.vertical_layout.addWidget(self.UserInfoBox)

        self.ServerInfoBox.setGeometry(35, 10, 300, 73)
        self.UserInfoBox.setGeometry(35, 82, 300, 90)
        self.CommandBox.setGeometry(35, 171, 300, 230)
        self.lineEditHostName.setGeometry(50, 50, 150, 20)
        # self.lineEditPort.setGeometry(205, 50, 40, 20)
        self.lineEditUsername.setGeometry(110, 105, 100, 20)
        self.lineEditPassword.setGeometry(110, 140, 100, 20)
        self.lineEditCommand.setGeometry(50, 247, 150, 20)

        # Create Labels
        self.nameLabelHostName = QLabel(self)
        # self.nameLabelPort = QLabel(self)
        self.nameLabelUsername = QLabel(self)
        self.nameLabelPassword = QLabel(self)
        self.nameLabelcommand = QLabel(self)
        self.nameLabelResponse = QLabel(self)
        self.nameLabelDefaultText = QLabel(self)
        self.nameLabelHostName.setText("HostName(IPaddress)")
        # self.nameLabelPort.setText("Port")
        self.nameLabelUsername.setText("Username: ")
        self.nameLabelPassword.setText("Password: ")
        self.nameLabelcommand.setText("Enter the command: ")
        self.nameLabelResponse.setText("Response:")
        # self.nameLabelDefaultText.setText("22")
        self.nameLabelHostName.move(50, 29)
        # self.nameLabelPort.move(207, 29)
        self.nameLabelUsername.move(50, 105)
        self.nameLabelPassword.move(50, 140)
        self.nameLabelcommand.move(50, 230)
        self.nameLabelResponse.move(50, 270)
        # self.nameLabelDefaultText.move(207, 53)

        # Creating push buttons
        self.ConnectButton = QPushButton("Connect", self)
        self.CancelButton = QPushButton("Cancel", self)
        self.ConnectButton.clicked.connect(self.ConnectButton_action)
        self.CancelButton.clicked.connect(self.CancelButton_action)
        self.ConnectButton.setGeometry(260, 410, 50, 25)
        self.CancelButton.setGeometry(320, 410, 50, 25)

        # Creating text field
        self.plaintextResponse = QPlainTextEdit(self)
        self.plaintextResponse.insertPlainText("You can write text here.\n")

        self.plaintextResponse.move(50, 290)
        self.plaintextResponse.resize(200, 100)

        # Creating Radio Buttons
        self.ManualButton = QRadioButton(self)
        self.ManualButton.setText("Manual")
        self.ManualButton.move(50, 195)

        # defaulty enable the radio button
        self.ManualButton.setChecked(True)

        self.RealTimeButton = QRadioButton(self)
        self.RealTimeButton.setText("Real Time")
        self.RealTimeButton.move(150, 195)

        self.show()

    def ConnectButton_action(self):
        try:
            self.hostname = self.lineEditHostName.text()
            # self.port = self.lineEditPort.text()
            self.username = self.lineEditUsername.text()
            self.password = self.lineEditPassword.text()
            self.command = self.lineEditCommand.text()

            response = self.plaintextResponse.appendPlainText(self.hostname)
            response = self.plaintextResponse.appendPlainText(self.username)
            response = self.plaintextResponse.appendPlainText(self.password)
            response = self.plaintextResponse.appendPlainText(self.command)

            print("HostName: {} ".format(self.hostname))
            print("UserName: {} and Password: {}".format(self.username, self.password))
            print("Command: {}".format(self.command))
            print("Response: {}".format(response))
        except Exception as e:
            QMessageBox.about(self, "Error", str(e))

    def CancelButton_action(self):
        quit = QAction("Quit", self)
        cancel = quit.triggered.connect(self.closeEvent)
        cancel.addAction(quit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QAction, QPlainTextEdit, QGridLayout, QMenu
from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic.properties import QtWidgets, QtCore
from dependencies.ssh_connect import SSHInterface


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'SSHInterface'
        self.left = 150
        self.top = 150
        self.width = 400
        self.height = 470
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.qwidget = QWidget()

        # Create textboxs
        self.ServerInfoBox = QGroupBox(self)
        self.ServerInfoBox.setTitle('Server Info')
        self.lineEditHostName = QLineEdit(self)
        # self.lineEditPort = QLineEdit(self)

        # horizontal layout
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.lineEditHostName)
        # self.horizontal_layout.addWidget(self.lineEditPort)
        # self.horizontal_layout_1.addWidget(self.textbox4)
        self.horizontal_layout.addWidget(self.ServerInfoBox)

        # Vertical layout
        self.UserInfoBox = QGroupBox(self)
        self.UserInfoBox.setTitle('User Info')
        self.CommandBox = QGroupBox(self)
        self.CommandBox.setTitle('Run the command')
        self.ResponseBox = QGroupBox(self)
        self.ResponseBox.setTitle('')
        self.lineEditUsername = QLineEdit(self)
        self.lineEditPassword = QLineEdit(self)
        self.lineEditCommand = QLineEdit(self)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.lineEditUsername)
        self.vertical_layout.addWidget(self.lineEditPassword)
        self.vertical_layout.addWidget(self.lineEditCommand)
        self.vertical_layout.addWidget(self.UserInfoBox)
        self.vertical_layout.addWidget(self.ResponseBox)

        self.ServerInfoBox.setGeometry(35, 10, 300, 73)
        self.UserInfoBox.setGeometry(35, 82, 300, 90)
        self.CommandBox.setGeometry(35, 171, 300, 100)
        self.ResponseBox.setGeometry(35, 277, 300, 135)
        self.lineEditHostName.setGeometry(50, 50, 150, 20)
        # self.lineEditPort.setGeometry(205, 50, 40, 20)
        self.lineEditUsername.setGeometry(110, 105, 100, 20)
        self.lineEditPassword.setGeometry(110, 140, 100, 20)
        self.lineEditCommand.setGeometry(50, 237, 150, 20)

        # Create Labels
        self.nameLabelHostName = QLabel(self)
        # self.nameLabelPort = QLabel(self)
        self.nameLabelUsername = QLabel(self)
        self.nameLabelPassword = QLabel(self)
        self.nameLabelcommand = QLabel(self)
        self.nameLabelResponse = QLabel(self)
        self.nameLabelDefaultText = QLabel(self)
        self.nameLabelHostName.setText("HostName(IPaddress)")
        # self.nameLabelPort.setText("Port")
        self.nameLabelUsername.setText("Username: ")
        self.nameLabelPassword.setText("Password: ")
        self.nameLabelcommand.setText("Enter the command: ")
        self.nameLabelResponse.setText("Response:")
        # self.nameLabelDefaultText.setText("22")
        self.nameLabelHostName.move(50, 29)
        # self.nameLabelPort.move(207, 29)
        self.nameLabelUsername.move(50, 105)
        self.nameLabelPassword.move(50, 140)
        self.nameLabelcommand.move(50, 220)
        self.nameLabelResponse.move(50, 280)

        self.RunButton = QPushButton("Run", self)
        # self.RunButton.clicked.connect(self.RunButton_action)
        self.RunButton.setGeometry(210, 236, 60, 22)

        self.CopyButton = QPushButton("Copy", self)
        self.CopyButton.setGeometry(260, 330, 50, 25)
        # self.CopyButton.clicked.connect(self.CopyButton_Action)

        self.ClearResponse = QPushButton("Clear Response", self)
        self.ClearResponse.setGeometry(100, 420, 90, 25)

        self.Clear = QPushButton("Clear All", self)
        self.Clear.setGeometry(200, 420, 50, 25)

        # Creating text field
        self.plaintextResponse = QPlainTextEdit(self)
        self.plaintextResponse.insertPlainText("You can write text here.\n")

        self.plaintextResponse.move(50, 300)
        self.plaintextResponse.resize(200, 100)

        # Creating Radio Buttons
        self.ManualButton = QRadioButton(self)
        self.ManualButton.setText("Manual")
        self.ManualButton.move(50, 195)

        # defaulty enable the radio button
        self.ManualButton.setChecked(True)

        self.RealTimeButton = QRadioButton(self)
        self.RealTimeButton.setText("Real Time")
        self.RealTimeButton.move(150, 195)

        self.show()

    def RunButton_action(self, ip, user, pwd):
        self.ip = ip
        self.username = user
        self.password = pwd


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())