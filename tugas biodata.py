import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QFormLayout, QRadioButton 

if __name__ == "__main__":
    #inisialisasi pyqt
    #ukuran window dan judul 
    app = QApplication (sys.argv)
    window = QWidget()
    window.setGeometry(50, 50, 800, 300)
    window.setWindowTitle("BIODATA")

    #menyiapkan label dan menampilkan text, menentukan warna dan ukuran font
    label = QLabel(window)
    label.setText ("Input Biodata")
    label.setStyleSheet("background-color: #00FFFF; color: black; font: bold 20px")

    #untuk membuat line edit  
    Line1 = QLineEdit()
    Line2 = QLineEdit()
    Line3 = QLineEdit()

    #untuk menyiapkan form layout 
    tabel = QFormLayout()
    tabel.addRow(label)
    tabel.addRow("Nama", Line1)
    tabel.addRow("Address", Line2)
    tabel.addRow(" ", Line3)

    #menyiapkan box layout 
    box1 = QCheckBox("Makan")
    box2 = QCheckBox("Tidur")
    box3 = QCheckBox("Main")
    tabel.addRow("Hobby", box1)
    tabel.addWidget(box2)
    tabel.addWidget(box3)

    #menyiapkan radiobutton 
    button = QRadioButton("Pelajar")
    button2 = QRadioButton("Pegawai")
    button3 = QRadioButton("Wiraswasta")
    tabel.addRow("Status", button)
    tabel.addWidget(button2)
    tabel.addWidget(button3)

    window.setLayout(tabel)

    window.show()
    app.exec_()
