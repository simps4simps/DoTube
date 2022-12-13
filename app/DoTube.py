from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
from pytube import YouTube

class Mainwindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.height = 10
        # Main Window Properties
        self.setGeometry(100, 100, 1000, 600)
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
        self.full_Screen = QtWidgets.QPushButton("", clicked=lambda: self.fullscreen())
        self.full_Screen.setIcon(QtGui.QIcon("../svg/fullscreen.svg"))
        self.full_Screen.setStyleSheet("""
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
        
        # Hbox And Frame
        self.frame1 = QtWidgets.QFrame(self)
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.framespace = QtWidgets.QFrame(self)
        
        # Adding Items To Layout
        self.vbox.addWidget(self.frame1)
        self.frame1.setFixedHeight(self.height)
        self.setLayout(self.vbox)
        self.hbox.addWidget(self.exit_button)
        self.hbox.addWidget(self.full_Screen)
        self.hbox.addWidget(self.mini)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.entry_label)
        self.vbox.addWidget(self.entry)
        self.vbox.addWidget(self.submit)
        self.vbox.addWidget(self.framespace)
        self.vbox.setContentsMargins(0,0,0,0)
        self.hbox.setContentsMargins(3, 0, 3, 3)
        self.hbox.setAlignment(QtCore.Qt.AlignTop)
        self.oldpos = self.frame1.pos()
        self.show()

    def quitprogram(self):
        sys.exit()

    def fullscreen(self):
        if self.counter == 0:
            self.setWindowState(QtCore.Qt.WindowMaximized)
            self.full_Screen.setIcon(QtGui.QIcon("../svg/small.svg"))
            self.counter = 1
        else:
            self.smallscreen()

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
        self.url = self.entry.text()
        ytl = YouTube(url=self.url)
        vid = ytl.streams.get_by_itag('22')
        vid.download()
        print('downloaded')
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DoTou = Mainwindow()
    
    sys.exit(app.exec_())