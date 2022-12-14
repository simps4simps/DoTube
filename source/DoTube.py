from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
import youtube_dl
import os
import ffmpeg

class Mainwindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.height = 10
        # Main Window Properties
        self.setFixedHeight(400)
        self.setFixedWidth(1000)
        self.counter = 0
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setObjectName("Mainwindow")
        self.setStyleSheet("""
            #Mainwindow{
                background: #191919;
            }
        """)
        self.center()

        # Define Tools
        self.exit_button = QtWidgets.QPushButton("", clicked=lambda: self.quitprogram())
        self.exit_button.setIcon(QtGui.QIcon("../svg/exit.svg"))
        self.exit_button.setStyleSheet("""
            QPushButton{
                background: #212121;
                border: 1px solid #212121;
                border-radius: 10px;
                width: 20px;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:hover{
                border: 1px solid #f0f0f0;
            }
        """)
        self.mini = QtWidgets.QPushButton("", clicked=lambda: self.minimize())
        self.mini.setIcon(QtGui.QIcon("../svg/min.svg"))
        self.mini.setStyleSheet("""
                            QPushButton{
                                background: #212121;
                                border: 1px solid #212121;
                                border-radius: 10px;
                                width: 20px;
                                padding: 10px;
                                margin: 5px;
                            }
                            QPushButton:hover{
                                border: 1px solid #f0f0f0;
                            }
                        """)
        
        self.entry_label = QtWidgets.QLabel('Enter the video URL here :')
        self.entry_label.setStyleSheet("""
                            QLabel{
                                color: #ffffff;
                                width: 20px;
                                padding: 20px;
                                font-size: 30px;
                                margin-left: -20px;
                            }
                        """)
        
        self.entry = QtWidgets.QLineEdit()
        self.entry.setStyleSheet("""
                            QLineEdit{
                                background: #212121;
                                border: 1px solid #ff3030;
                                border-radius: 10px;
                                padding: 10px;
                                font-size: 20px;
                            }
                            QLineEdit:hover{
                                border: 1px solid #f0f0f0;
                            }
                        """)
        self.submit = QtWidgets.QPushButton("Download", clicked=lambda: self.download())
        self.submit.setStyleSheet("""
                            QPushButton{
                                background: #ff3030;
                                border: 1px solid #ff3030;
                                border-radius: 10px;
                                width: 20px;
                                padding: 15px;
                                margin: 5px;
                                font-size: 15px;
                            }
                            QPushButton:hover{
                                border: 1px solid #f0f0f0;
                            }
                        """)
        self.status = QtWidgets.QLabel('')
        self.status.setStyleSheet("""
                            QLabel{
                                color: #ff3030;
                                width: 20px;
                                padding: 20px;
                                font-size: 15px;
                            }
                        """)
        
        # Hbox And Frame
        self.frame1 = QtWidgets.QFrame(self)
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.vbox2 = QtWidgets.QVBoxLayout(self)
        self.framespace = QtWidgets.QFrame(self)
        
        
        # Adding Items To Layout
        self.vbox2.addWidget(self.frame1)
        self.frame1.setStyleSheet('border: 1px solid gray; border-radius: 10px;')
        self.frame1.setFixedHeight(25)
        self.frame1.setFixedWidth(1000)
        self.setLayout(self.vbox)
        self.hbox.addWidget(self.exit_button)
        self.hbox.addWidget(self.mini)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.entry_label)
        self.vbox.addWidget(self.entry)
        self.vbox.addWidget(self.submit)
        self.vbox.addWidget(self.status)
        self.vbox.addWidget(self.framespace)
        self.vbox.setContentsMargins(0,0,0,0)
        self.hbox.setContentsMargins(3, 0, 3, 3)
        self.hbox.setAlignment(QtCore.Qt.AlignTop)
        widthI = 800
        self.vbox.setAlignment(QtCore.Qt.AlignCenter)
        self.entry.setFixedWidth(widthI)
        self.oldpos = self.frame1.pos()
        self.show()

    def quitprogram(self):
        sys.exit()

    def smallscreen(self):
        self.setWindowState(QtCore.Qt.WindowNoState)
        self.full_Screen.setIcon(QtGui.QIcon("../svg/fullscreen.svg"))
        self.counter = 0

    def minimize(self):
        self.showMinimized()

    def center(self):
        frame_g = self.frameGeometry()
        dg = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_g.moveCenter(dg)
        self.move(frame_g.topLeft())

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        self.oldpos = event.pos()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if self.frame1.underMouse() == True:
            x = event.globalX()
            y = event.globalY()
            x_w = self.oldpos.x()
            y_w = self.oldpos.y()
            self.move(x-x_w,y-y_w)
            
    def download(self):
        try:
            self.status.setText('Downloading please dont close the app when it freezes!')
            self.url = self.entry.text()

            ydl_opts = {}
            channel = 1
            while (channel == int(1)):
                link_of_the_video = self.url
                zxt = link_of_the_video.strip()
            
                dwl_vid()
            
            self.status.setText('Download completed!')
        except:
            self.status.setText('Oops! Something went wrong. Maybe your URL?')
            
    def dwl_vid():
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([zxt])
            
        
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DoTou = Mainwindow()
    
    sys.exit(app.exec_())