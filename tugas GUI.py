import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()

   #menyiapkan label, menempelkan label ke window
   #settext, dan posisi
   textLabel = QLabel(window)
   textLabel.setText("Kotak Angka")
   textLabel.move(5,5)
   for i in range(5):
       label2 = QPushButton(window)
       #mengubah ukuran button
       label2.resize(30,30)
       #mengubah style/tampilan
       #settext
       label2.setStyleSheet("background-color : skyblue; color:red; font-size:25px; font:Times New Roman")
       label2.setText(str(i+1))
       #mengubah posisi button
       label2.move(35*(i),20)
       
   #menentukan ukuran window, + title dan menampilkan
   window.setGeometry(50,50,320,300)
   window.setWindowTitle("PyQt5 Example")
   window.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window_go()

