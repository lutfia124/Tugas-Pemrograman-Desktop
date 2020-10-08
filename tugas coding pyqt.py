import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

#membuat fungsi utk menentukan layout window
def window_go():
   #inisialisasi pyqt
   app = QApplication(sys.argv)
   window = QWidget()

   #menyiapkan label, menempelkan label ke window
   #settext, dan posisi
   textLabel = QLabel(window)
   label = [None]*15
   baris = 50
   for i in range(1,11):
      baris = baris + 15
      label[i] = QLabel(window)
      label[i].setText("Hello World!" + str(i))
      label[i].move(10,baris)
   
   #menentukan ukuran window, + title dan menampilkan
   window.setGeometry(50,50,320,300)
   window.setWindowTitle("PyQt5 Example")
   window.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   window_go()

