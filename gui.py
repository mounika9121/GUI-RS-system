# Built-in module
import sys

from ssh_connect import SSHInterface
#Third-party modules
from PyQt5.QtGui import QFont
from PyQt5 import QtGui, Qt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDialog, QApplication, \
    QWidget, QPushButton, QLineEdit, QLabel, \
    QRadioButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QPlainTextEdit, QTextEdit, QFileDialog


class GUIConnector(QDialog):

      def __init__(self):
          super().__init__()
          self.title='SSHInterface'

          # Desktop positions
          self.x=100
          self.y=100
          self.width=400
          self.height=500
          self.initUI()

      def initUI(self):
          # Widget
          self.setWindowTitle(self.title)
          self.setGeometry(self.x,self.y,self.width,self.height)
          self.setWindowIcon(QtGui.QIcon("logo.png"))
          self.qwidget = QWidget()

          #Create textboxs
          self.ServerInfoBox = QGroupBox(self)
          self.ServerInfoBox.setTitle('Server Info')
          self.lineEditHostName = QLineEdit(self)
          #self.lineEditPort = QLineEdit(self)

          #horizontal layout
          self.horizontal_layout = QHBoxLayout()
          self.horizontal_layout.addWidget(self.lineEditHostName)
          #self.horizontal_layout.addWidget(self.lineEditPort)
          #self.horizontal_layout_1.addWidget(self.textbox4)
          self.horizontal_layout.addWidget(self.ServerInfoBox)

          #Vertical layout
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
          #self.lineEditPort.setGeometry(205, 50, 40, 20)
          self.lineEditUsername.setGeometry(110, 105, 100, 20)
          self.lineEditPassword.setGeometry(110, 140, 100, 20)
          self.lineEditCommand.setGeometry(50, 237, 150, 20)

          #Create Labels
          self.nameLabelHostName =  QLabel(self)
          #self.nameLabelPort = QLabel(self)
          self.nameLabelUsername = QLabel(self)
          self.nameLabelPassword = QLabel(self)
          self.nameLabelcommand = QLabel(self)
          self.nameLabelResponse = QLabel(self)
          self.nameLabelDefaultText = QLabel(self)
          self.nameLabelHostName.setText("HostName(IPaddress)")
          #self.nameLabelPort.setText("Port")
          self.nameLabelUsername.setText("Username: ")
          self.nameLabelPassword.setText("Password: ")
          self.nameLabelcommand.setText("Enter the command: ")
          self.nameLabelResponse.setText("Response:")
          #self.nameLabelDefaultText.setText("22")
          self.nameLabelHostName.move(50, 29)
          #self.nameLabelPort.move(207, 29)
          self.nameLabelUsername.move(50, 105)
          self.nameLabelPassword.move(50, 140)
          self.nameLabelcommand.move(50, 220)
          self.nameLabelResponse.move(50, 280)

          # Run button
          self.RunButton = QPushButton("Run", self)
          self.RunButton.setGeometry(210, 236, 60, 22)
          self.RunButton.clicked.connect(self.action_run)

          self.CopyButton = QPushButton("Copy", self)
          self.CopyButton.setGeometry(260, 330, 50, 25)
          self.CopyButton.clicked.connect(self.copy_response)

          self.ClearResponse = QPushButton("Clear Response", self)
          self.ClearResponse.setGeometry(100 , 420, 90, 25)
          #self.ClearResponse.clicked.connect(self.resp.clear)
          self.Clear = QPushButton("Clear All", self)
          self.Clear.setGeometry(200, 420, 50, 25)

          # Clear the data from hostname, username, password, command textbox's

          self.Clear.clicked.connect(self.lineEditHostName.clear)
          self.Clear.clicked.connect(self.lineEditUsername.clear)
          self.Clear.clicked.connect(self.lineEditPassword.clear)
          self.Clear.clicked.connect(self.lineEditCommand.clear)
          self.Clear.clicked.connect(self.lineEditUsername.clear)

          #Creating text field
          self.LineTextResponce = QTextEdit(self)
          self.LineTextResponce.insertPlainText("You can write text here.\n")
          self.LineTextResponce.move(50, 300)
          self.LineTextResponce.resize(200, 100)

          #Creating Radio Buttons
          self.ManualButton = QRadioButton(self)
          self.ManualButton.setText("Manual")
          self.ManualButton.move(50, 195)

          # defaulty enable the radio button
          self.ManualButton.setChecked(True)

          self.RealTimeButton = QRadioButton(self)
          self.RealTimeButton.setText("Real Time")
          self.RealTimeButton.move(150, 195)

          #Browser push button
          self.BrowserButton = QPushButton("Browse", self)
          self.BrowserButton.setGeometry(260, 360, 50, 25)
          self.BrowserButton.clicked.connect(self.browse_response)

          self.show()

      def action_run(self):
          ip = self.lineEditHostName.text()
          user = self.lineEditUsername.text()
          pwd = self.lineEditPassword.text()

          command = self.lineEditCommand.text()

          conn = SSHInterface(ip, user, pwd)
          conn.connect()
          self.resp = conn.runCommand(command)
          print(self.resp)
          
          self.LineTextResponce.setPlainText(self.resp)

          """
          self.plaintextResponse.appendPlainText(self.ip)
          self.plaintextResponse.appendPlainText(self.user)
          self.plaintextResponse.appendPlainText(self.pwd)
          self.plaintextResponse.appendPlainText(self.command)
          print("HostName: {} ".format(self.ip))
          print("UserName: {} and Password: {}".format(self.user, self.pwd))
          print("Command: {}".format(self.command))
          print("Response: {}".format(self.LineTextResponce))
                    
          """


      def copy_response(self):
          resp = self.LineTextResponce.toPlainText()
          print("*"*100)
          print(resp)
          print("*"*100)
          f = open('response.log', 'w')
          f.write(resp)
          f.close()

      def browse_response(self):
          """
          #resp = self.LineTextResponce.toPlainText()
          #print(resp)
          f = open('C:\\Users\\M.Mounika\\Desktop\\selenium\\task\dependencies\\response.log', 'w')
          for line in f:
              x = line.split(",")
              print(x[0], '\t', x[1])
          """
          filename = QFileDialog.getOpenFileName(self, 'Open File', '\home')

          if filename[0]:
              f = open(filename[0], 'r')

              with f:
                  data = f.read()
                  self.LineTextResponce.setText(data)
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=GUIConnector()
    sys.exit(app.exec_())