from PyQt6.QtWidgets import QWidget, QTextBrowser, QGridLayout, QLabel, QPushButton, QApplication, QLineEdit, \
    QMessageBox, QVBoxLayout
from PyQt6.QtCore import pyqtSlot, Qt


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.dezi_label = QLabel("Dezimalsystem: Zahl 0 - 9999", self)
        self.deziLineEdit = QLineEdit(self)
        self.meldung1 = QLabel("", self)

        self.hexa_label = QLabel("Hexadezimalsystem: sechsstellig", self)
        self.hexaLineEdit = QLineEdit(self)
        self.meldung2 = QLabel("", self)

        self.bin_label = QLabel("Binärzahlen: ", self)
        self.binLineEdit = QLineEdit(self)
        self.meldung3 = QLabel("", self)

        self.char_label = QLabel("Buchstaben: ", self)
        self.charLineEdit = QLineEdit(self)
        self.meldung4 = QLabel("", self)

        self.lower_label = QLabel("Groß- & Kleinbuchstaben: ", self)
        self.lowerLineEdit = QLineEdit(self)
        self.meldung5 = QLabel("", self)

        self.login_button = QPushButton("Check", self)
        self.login_button.clicked.connect(self.check)


        layout = QGridLayout(self)
        layout.addWidget(self.dezi_label, 1, 1)
        layout.addWidget(self.deziLineEdit, 1, 2)
        layout.addWidget(self.meldung1, 1, 3)
        layout.addWidget(self.hexa_label, 2, 1)
        layout.addWidget(self.hexaLineEdit, 2, 2)
        layout.addWidget(self.meldung2, 2, 3)
        layout.addWidget(self.bin_label, 3, 1)
        layout.addWidget(self.binLineEdit, 3, 2)
        layout.addWidget(self.meldung3, 3, 3)
        layout.addWidget(self.char_label, 4, 1)
        layout.addWidget(self.charLineEdit, 4, 2)
        layout.addWidget(self.meldung4, 4, 3)
        layout.addWidget(self.lower_label, 5, 1)
        layout.addWidget(self.lowerLineEdit, 5, 2)
        layout.addWidget(self.meldung5, 5, 3)

        layout.addWidget(self.login_button)

    def check(self):
        dezimal = self.deziLineEdit.text()
        hexa = self.hexaLineEdit.text()
        bin = self.binLineEdit.text()
        char = self.charLineEdit.text()
        lower= self.lowerLineEdit.text()

        if dezimal == "":
            self.meldung1.setText("Fehler (Feld leer)")
        elif not dezimal.isdigit() or int(dezimal) < 0 or int(dezimal) > 9999:
            self.meldung1.setText("Ungültig")
        else:
            self.meldung1.setText("Richtig")


        if hexa == "":
            self.meldung2.setText("Fehler (Feld leer)")
        elif not all(c in "0123456789ABCDEFabcdef" for c in hexa) or len(hexa) != 6:
            self.meldung2.setText("Ungültig")
        else:
            self.meldung2.setText("Richtig")


        if bin == "":
            self.meldung3.setText("Fehler (Feld leer)")
        elif not all(c in "01" for c in bin) or len(bin) < 2 or len(bin) > 10:
            self.meldung3.setText("Ungültig")
        else:
            self.meldung3.setText("Richtig")


        if char == "":
            self.meldung4.setText("Fehler (Feld leer)")
        elif not char.isalpha():
            self.meldung4.setText("Ungültig")
        else:
            self.meldung4.setText("Richtig")


        if lower == "":
            self.meldung5.setText("Fehler (Feld leer)")
        elif not any(c.islower() for c in lower) or not any(c.isupper() for c in lower):
            self.meldung5.setText("Ungültig")
        else:
            self.meldung5.setText("Richtig")




