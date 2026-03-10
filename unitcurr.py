from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:#171d1c;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.froml = QtWidgets.QComboBox(self.centralwidget)
        self.froml.setGeometry(QtCore.QRect(100, 280, 121, 41))
        self.froml.setStyleSheet("font: 57 18pt \"LEMON MILK Medium\";\n"
"border:2px solid orange;\n"
"background-color:white;\n"
"border-radius:7px;")
        self.froml.setObjectName("froml")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 741, 71))
        self.label.setStyleSheet("background-color:white;\n"
"font: 75 italic 24pt \"LEMON MILK Bold\";\n"
"border:2px solid orange;\n"
"border-radius:20px;")
        self.label.setObjectName("label")
        self.tol = QtWidgets.QComboBox(self.centralwidget)
        self.tol.setGeometry(QtCore.QRect(560, 270, 121, 41))
        self.tol.setStyleSheet("font: 57 18pt \"LEMON MILK Medium\";\n"
"border:2px solid orange;\n"
"background-color:white;\n"
"border-radius:7px;")
        self.tol.setObjectName("tol")
        
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(350, 140, 421, 51))
        self.input.setStyleSheet("border:3px solid white;\n"
"font: 75 20pt \"UD Digi Kyokasho NP-B\";\n"
"color:white;")
        self.input.setText("")
        self.input.setObjectName("input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 411, 81))
        self.label_2.setStyleSheet("background-color:light black;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 230, 121, 41))
        self.label_3.setStyleSheet("background-color:light black;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 220, 111, 41))
        self.label_4.setStyleSheet("background-color:light black;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 410, 221, 81))
        self.label_5.setStyleSheet("background-color:light black;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 420, 351, 61))
        self.label_6.setStyleSheet("border:3px solid white;\n"
"font: 75 18pt \"LEMON MILK Bold\";\n"
"color:white;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(310, 340, 141, 41))
        self.convert.setStyleSheet("background-color:white;\n"
"font: 75 12pt \"LEMON MILK Bold\";\n"
"border:2px solid orange;\n"
"border-radius:15px;")
        self.convert.setObjectName("convert")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.currencies = [
            "USD", "INR", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", 
            "CNY", "HKD", "NZD", "SEK", "KRW", "SGD", "NOK", "MXN", 
            "ZAR", "BRL", "TRY", "RUB", "AED", "SAR", "THB", "IDR"
        ]
        
        self.froml.addItems(self.currencies)
        self.tol.addItems(self.currencies)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "        Currency Converter"))
        self.label_2.setText(_translate("MainWindow", "Enter amount :"))
        self.label_3.setText(_translate("MainWindow", "From"))
        self.label_4.setText(_translate("MainWindow", "TO"))
        self.label_5.setText(_translate("MainWindow", "result:"))
        self.convert.setText(_translate("MainWindow", "Convert"))
        self.convert.clicked.connect(self.currency)
        
    def currency(self):
        rates = {
            "USD": (1.0, "$"), "INR": (82.90, "₹"), "EUR": (0.92, "€"), "JPY": (149.50, "¥"),
            "GBP": (0.79, "£"), "AUD": (1.53, "A$"), "CAD": (1.35, "C$"), "CHF": (0.88, "CHF"),
            "CNY": (7.19, "¥"), "HKD": (7.82, "HK$"), "NZD": (1.65, "NZ$"), "SEK": (10.45, "kr"),
            "KRW": (1335.0, "₩"), "SGD": (1.34, "S$"), "NOK": (10.60, "kr"), "MXN": (17.05, "$"),
            "ZAR": (18.90, "R"), "BRL": (4.98, "R$"), "TRY": (31.50, "₺"), "RUB": (92.50, "₽"),
            "AED": (3.67, "د.إ"), "SAR": (3.75, "﷼"), "THB": (35.80, "฿"), "IDR": (15600.0, "Rp")
        }
        
        try:
            am = float(self.input.text())
        except ValueError:
            self.label_6.setText("Invalid Input")
            return
            
        b = self.froml.currentText()
        c = self.tol.currentText()
        
        rate_from = rates[b][0]
        rate_to = rates[c][0]
        symbol = rates[c][1]
        
        amount_in_usd = am / rate_from
        final_amount = amount_in_usd * rate_to
        
        self.label_6.setText(f"{symbol}{final_amount:.2f}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())