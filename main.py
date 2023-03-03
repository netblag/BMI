from PyQt6 import QtCore, QtGui, QtWidgets
from window import Ui_BMI
import mysql.connector


class UiEvent(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BMI()
        self.ui.setupUi(self)
        self.ui.btn_calc.clicked.connect(self.bmi_calculator)
        self.db_cursor = self.db_connection()

    def bmi_calculator(self):
        try:
            name = self.ui.lineEdit_name.text()
            weight = float(self.ui.lineEdit_2_weight.text())
            height = float(self.ui.lineEdit_3_height.text())
            bmi = round(weight / (height/100)**2, 2)
            self.ui.label_bmi.setText(str(bmi))
            self.insert_db(name, weight, height, bmi)
        except:
            pass

    def db_connection(self):
        self.conn = mysql.connector.connect(
            host='HOSTNAME',
            user='root',
            password='PASSWORD',
            database='bmi'
        )
        db_cursor = self.conn.cursor()
        return db_cursor

    def insert_db(self, name, weight, height, bmi):
        self.db_cursor.execute("""
                        INSERT INTO person_info(name,weight,height,bmi)
                        VALUSE (%s,%s,%s,%s,)""", [name, weight, height, bmi])
        self.conn.commit()
        self.db_cursor.fetchone()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UiEvent()
    window.show()
    sys.exit(app.exec())
